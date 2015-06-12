from django.conf.urls import patterns, url, include
from rest_framework_nested import routers
from rest.views import IndexView

from authentication.views import AccountViewSet
from django.contrib import admin
admin.autodiscover()

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = patterns(
    '',
    # url(r'^.*$', IndexView.as_view(), name='index'),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/', include('agents.urls')),
    url(r'^api/v1/', include('distributors.urls')),
    url(r'^api/v1/', include('authentication.urls')),
    url(r'^api/v1/', include('products.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
# index route last - angular overwrite all endpoints - avoid 404?
# TODO: fix app route
# TODO: cleaner routes with class based views