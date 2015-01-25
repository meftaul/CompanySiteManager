from django.conf.urls import patterns, url
from en import views


urlpatterns = patterns('',

    url(r'^$', 'en.views.home', name='home'),
    url(r'^member/(?P<member_id>\d+)/$', 'en.views.detail', name='detail'),
    url(r'^service/(?P<service_id>\d+)/$', 'en.views.service', name='service'),
    url(r'^clients/$', 'en.views.clients', name='clients'),
    url(r'^contact/$', 'en.views.contact', name='contact'),
    url(r'^advantage/$', 'en.views.advantage', name='advantage'),
    url(r'^about/$', 'en.views.about', name='about'),

)



