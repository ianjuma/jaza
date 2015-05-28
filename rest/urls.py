from django.conf.urls import patterns, url, include
from django.contrib import admin
from rest.views import IndexView


urlpatterns = patterns(
    '',
    url(r'^api/v1/', include('authentication.urls')),
    url(r'^api/v1/', include('posts.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('^.*$', IndexView.as_view(), name='index')
)

# index route last - angular overwrite all endpoints - avoid 404?
# no need for include function