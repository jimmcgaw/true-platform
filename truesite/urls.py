from django.conf.urls.defaults import *

urlpatterns = patterns('truesite.views',
    (r'^$', 'index'),
    (r'^design/$', 'design'),
    (r'^integration/$', 'integration'),
    (r'^marketing/$', 'marketing'),
    (r'^contact/$', 'contact'),
)