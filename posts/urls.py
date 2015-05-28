from django.conf.urls import patterns, url, include
from rest_framework_nested import routers
from authentication.views import AccountViewSet
from posts.views import PostViewSet, AccountPostsViewSet


router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'posts', PostViewSet)

accounts_router = routers.NestedSimpleRouter(
    router, r'accounts', lookup='account'
)
accounts_router.register(r'posts', AccountPostsViewSet)


urlpatterns = patterns(
    '',
    url(r'^posts', include(router.urls, namespace='api'))
)

# index route last - angular overwrite all endpoints - avoid 404?
# no need for include function