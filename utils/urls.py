from django.conf.urls import url

from utils.views import (CrunchView, SleuthAgentTopUpView,
                         SleuthGetAgentBalanceView)

urlpatterns = [
    url('^crunch/$', CrunchView.as_view()),
    url('^sleuth/$', SleuthAgentTopUpView.as_view()),
    url('^sleuth/$', SleuthGetAgentBalanceView.as_view())
]
