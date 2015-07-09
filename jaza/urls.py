from django.conf.urls import patterns, url, include
from rest_framework_nested import routers
from jaza.views import IndexView, LoginView
# from utils.views import CrunchView

from authentication.views import UserViewSet
from django.contrib import admin
admin.autodiscover()

router = routers.SimpleRouter()
router.register(r'accounts', UserViewSet)

urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^accounts/login', LoginView.as_view(), name='login'),
    # url(r'^api/v1/', CrunchView.as_view()),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/', include('agents.urls')),
    url(r'^api/v1/', include('distributors.urls')),
    url(r'^api/v1/', include('authentication.urls')),
    url(r'^api/v1/', include('products.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
handler404 = 'views.handle_page_not_found_404'

# index route last - angular overwrite all endpoints - avoid 404?
# TODO: fix app route url(r'^.*$', IndexView.as_view(), name='index')
# TODO: cleaner routes with class based views