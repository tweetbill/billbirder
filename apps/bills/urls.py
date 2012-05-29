from django.conf.urls import patterns, url
from bills import views

urlpatterns = patterns('',
    url(r'^$', views.bill_list, name="bills_bill_list"),

    url(r'^search/$',
    	views.bill_search,
    	name="bills_bill_search"),

    url(r'^(?P<bill_id>[-\w]+)/$', 
    	views.bill_detail, 
    	name="bills_bill_detail"),

    url(r'^(?P<bill_id>[-\w]+)/follow/$', 
    	views.follow_bill, 
    	name="bills_bill_follow"),
)