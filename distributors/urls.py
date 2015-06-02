from django.conf.urls import patterns, url, include
from rest_framework_nested import routers
from distributors.views import DistributorViewSet


router = routers.SimpleRouter()
router.register(r'distributors', DistributorViewSet)


urlpatterns = patterns(
    '',
    url(r'^distributors', include(router.urls, namespace='api.distributors'))
)

# index route last - angular overwrite all endpoints - avoid 404?
# no need for include function