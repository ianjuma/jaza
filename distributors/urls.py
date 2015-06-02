from django.conf.urls import patterns, url
from views import distributor_detail, distributor_list


urlpatterns = patterns(
    '',
    url(r'^distributors/$', distributor_list, name='distributor_list'),
    url(r'^distributors/(?P<pk>[0-9]+)$', distributor_detail, name='distributor_detail'),
)

# index route last - angular overwrite all endpoints - avoid 404?
# no need for include function