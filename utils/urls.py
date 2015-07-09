from django.conf.urls import url

from utils.views import CrunchView

urlpatterns = [
    url('^crunch/$', CrunchView.as_view()),
]
