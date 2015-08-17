from django.conf.urls import url

from utils.views import (CrunchProductStatsView, CrunchAgentStatsView,
                         SleuthUserTopUpView, SleuthGetUserBalanceView)

urlpatterns = [
    url('^crunch/agents/(?P<pk>[0-9]+)$', CrunchAgentStatsView.as_view()),
    url('^crunch/products/(?P<pk>[0-9]+)$', CrunchProductStatsView.as_view()),
    url('^/billing/add$', SleuthUserTopUpView.as_view()),
    url('^/billing/balance$', SleuthGetUserBalanceView.as_view())
]
