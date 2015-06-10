from django.conf.urls import patterns, url
from views import transaction_list, transaction_detail

urlpatterns = patterns(
    '',
    url(r'^transaction/$', transaction_list, name='transaction_list'),
    url(r'^transaction/(?P<pk>[0-9]+)$', transaction_detail, name='transaction_detail'),
)