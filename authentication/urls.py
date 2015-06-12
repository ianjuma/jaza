from django.conf.urls import patterns, url
from authentication.views import AuthToken, Login, Logout, AuthView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = patterns(
    '',
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^logout/$', Logout.as_view(), name='logout'),
    url(r'^token/$', AuthToken.as_view(), name='token'),
    url(r'^auth/$', AuthView.as_view(), name='auth-view'),
)

urlpatterns = format_suffix_patterns(urlpatterns=urlpatterns)
