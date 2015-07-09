from django.conf.urls import url

from utils import views

urlpatterns = [
    url('^crunch/$', views.CrunchView.as_view(), name='crunch'),
]
