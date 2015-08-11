from django.conf.urls import url

from utils.views import (CrunchView, SleuthUserTopUpView,
                         SleuthGetUserBalanceView)

urlpatterns = [
    url('^crunch/$', CrunchView.as_view()),
    url('^/billing/add$', SleuthUserTopUpView.as_view()),
    url('^/billing/balance$', SleuthGetUserBalanceView.as_view())
]
