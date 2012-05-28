from django.conf import settings
from django.core.cache import cache
from django.views.generic import ListView, DetailView

from bills.utils.rtc import RealTimeCongress

rtc = RealTimeCongress(settings.SUNLIGHT_API_KEY)

class BillList(ListView):
    """
    Base class for a list of bills. This may be filtered.
    """

    def get_queryset(self):
    	bills = rtc.bills(**self.request.GET)
    	return bills


class BillDetail(DetailView):
	pass
