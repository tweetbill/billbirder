"""
A minimalist wrapper for Sunlight's Real-time Congress API
"""
import json
import os
import urllib
import httplib2

BASE_URL = "http://api.realtimecongress.org/api/v1/%s.json?"

class RealTimeCongress(object):
    """
    A Real-time Congress client.
    """
    def __init__(self, apikey=None, cache=None):
    	self.apikey = apikey or os.environ.get('SUNLIGHT_API_KEY')
        self.http = httplib2.Http(cache)

    def fetch(self, collection, **kwargs):
    	"""
    	Request data. Return JSON.
    	"""
    	kwargs['apikey'] = self.apikey
    	url = BASE_URL % collection
    	url += urllib.urlencode(kwargs)
    	r, c = self.http.request(url)
    	return json.loads(c)

    def bills(self, **kwargs):
    	"""
    	Fetch bills
    	"""
    	return self.fetch('bills', **kwargs)

    def votes(self, **kwargs):
    	"""
    	Fetch votes
    	"""
    	return self.fetch('votes', **kwargs)


