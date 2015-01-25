from django.conf.urls import patterns, url
from ger import views


urlpatterns = patterns('',

    url(r'^$', 'ger.views.home', name='ger_home'),
    url(r'^member/(?P<member_id>\d+)/$', 'ger.views.detail', name='ger_detail'),
    url(r'^service/(?P<service_id>\d+)/$', 'ger.views.service', name='ger_service'),
    url(r'^clients/$', 'ger.views.clients', name='ger_clients'),
    url(r'^contact/$', 'ger.views.contact', name='ger_contact'),
    url(r'^advantage/$', 'ger.views.advantage', name='ger_advantage'),
    url(r'^about/$', 'ger.views.about', name='ger_about'),

)



