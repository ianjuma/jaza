from django.conf.urls import patterns, url
from authentication.views import Login, Logout
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = patterns(
    '',
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^logout/$', Logout.as_view(), name='logout'),
)

urlpatterns = format_suffix_patterns(urlpatterns=urlpatterns)
