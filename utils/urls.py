from django.conf.urls import url

from utils.views import (CrunchView, SleuthUserTopUpView,
                         SleuthGetUserBalanceView)

urlpatterns = [
    url('^crunch/$', CrunchView.as_view()),
    url('^sleuth/topup$', SleuthUserTopUpView.as_view()),
    url('^sleuth/balance$', SleuthGetUserBalanceView.as_view())
]
