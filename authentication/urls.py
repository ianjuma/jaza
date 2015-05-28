from django.conf.urls import patterns, url, include
from rest_framework_nested import routers
from authentication.views import AccountViewSet

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

accounts_router = routers.NestedSimpleRouter(
    router, r'accounts', lookup='account'
)


urlpatterns = patterns(
    '',
    url(r'^account', include(router.urls, namespace='api')),
    url(r'^accounts', include(accounts_router.urls, namespace='api'))
)
