import json
import urllib
import urllib2
from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import TestCase

from bills.utils.rtc import RealTimeCongress

BASE_URL = "http://api.realtimecongress.org/api/v1/bills.json?"

class BillTest(TestCase):

	def setUp(self):
		self.rtc = RealTimeCongress(settings.SUNLIGHT_API_KEY)

	def check_response(self, url, data):
		real = json.load(urllib2.urlopen(url))
		self.assertEqual(real, data)

	def test_bill_list(self):
		# just get the latest 20 bills
		bills = self.rtc.bills()
		url = BASE_URL + urllib.urlencode({ 
			'apikey': settings.SUNLIGHT_API_KEY
		})
		self.check_response(url, bills)

	def test_bill_search(self):
		bills = self.rtc.bills(search="china")
		url = BASE_URL + urllib.urlencode({
			'apikey': settings.SUNLIGHT_API_KEY,
			'search': 'china'
		})
		self.check_response(url, bills)

	def test_bill_search_view(self):
		url = reverse('bills_bill_search')
		bills = self.rtc.bills(search="china")
		response = self.client.get(url + '?q=china')
		



