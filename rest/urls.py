from django.conf.urls import patterns, url, include
from rest.views import IndexView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^api/v1/', include('agents.urls')),
    url(r'^api/v1/', include('distributors.urls')),
    url(r'^api/v1/', include('products.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('^.*$', IndexView.as_view(), name='index')
)

# index route last - angular overwrite all endpoints - avoid 404?
#