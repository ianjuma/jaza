from django.conf.urls import patterns, url
from views import product_list, product_detail, distributor_products

urlpatterns = patterns(
    '',
    url(r'^products/$', product_list, name='product_list'),
    url(r'^myProducts/$', distributor_products, name='my_product_list'),
    url(r'^products/(?P<pk>[0-9]+)$', product_detail, name='product_detail'),
)