from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.utils import simplejson as json

from bills.models import FollowedBill
from bills.utils.rtc import RealTimeCongress

rtc = RealTimeCongress(settings.SUNLIGHT_API_KEY, cache)

def bill_list(request, **kwargs):
    """
    A filterable list of bills

    Context:
      bills: a list of bills matching search params
    """
    bills = rtc.bills(**request.GET)
    if request.user.is_authenticated():
        following = set(request.user.bills.values_list('id', flat=True))
        for bill in bills.get('bills', []):
            if bill.get('bill_id') in following:
                bill['following'] = True
            else:
                bill['following'] = False
    return TemplateResponse(request, 'bills/bill_list.html', bills)


def bill_detail(request, bill_id):
    """
    Details on a bill

    Context:
      bill: this bill, as JSON
      following: Boolean, whether or not user follows this bill
    """
    context = {}
    user = request.user

    bills = rtc.bills(bill_id=bill_id)
    try:
        context['bill'] = bills['bills'][0]
    except IndexError, KeyError:
        raise Http404('Bill Not Found')

    if request.user.is_authenticated():
        followed = list(user.bills.values_list('id', flat=True))
        context['following'] = bill_id in followed

    return TemplateResponse(request, 'bills/bill_detail.html', context)


@login_required
def follow_bill(request, bill_id):
    """
    Follow a bill. Ideally, this should be ajax.
    """
    if not request.method == "POST":
        return HttpResponseBadRequest()

    next = request.POST.get('next')
    if not next:
        next = reverse('bills_bill_detail', args=[bill_id])

    bill, created = FollowedBill.objects.get_or_create(id=bill_id)
    action = request.POST.get('action', 'follow')
    if action.lower() == "follow":
        bill.followers.add(request.user)
    else:
        bill.followers.remove(request.user)
    return redirect(next)


def bill_search(request):
    query = request.GET.get('q', None)
    page = request.GET.get('page', 1)
    bills = []
    if query:
        bills = rtc.bills(search=query, page=page).get('bills', [])
    return TemplateResponse(request, 'bills/bill_list.html', {
        'bills': bills,
        'page' : page,
        'query': query
    })


