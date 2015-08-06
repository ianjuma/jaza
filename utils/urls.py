from django.conf.urls import url

from utils.views import (CrunchView, SleuthAgentTopUpView,
                         SleuthGetAgentBalanceView)

urlpatterns = [
    url('^crunch/$', CrunchView.as_view()),
    url('^sleuth/topup$', SleuthAgentTopUpView.as_view()),
    url('^sleuth/balance$', SleuthGetAgentBalanceView.as_view())
]
