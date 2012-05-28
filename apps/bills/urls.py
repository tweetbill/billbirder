from django.conf.urls import patterns, url
from bills.views import bill_list

urlpatterns = patterns('',
    url(r'^$', bill_list, name="bills_bill_list"),
)