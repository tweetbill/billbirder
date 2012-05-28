from django.conf import settings
from django.core.cache import cache
from django.template.response import TemplateResponse

from bills.utils.rtc import RealTimeCongress

rtc = RealTimeCongress(settings.SUNLIGHT_API_KEY, cache)

def bill_list(request, **kwargs):
	"A filterable list of bills"
	bills = rtc.bills(**request.GET)
	return TemplateResponse(request, 'bills/bill_list.html', bills)


def bill_detail(request, bill_id):
	pass


def follow_bill(request, bill_id):
	pass
