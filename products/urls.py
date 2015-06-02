from django.conf.urls import patterns, url, include
from rest_framework_nested import routers
from products.views import ProductViewSet


router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)


urlpatterns = patterns(
    '',
    url(r'^products', include(router.urls, namespace='api.products'))
)