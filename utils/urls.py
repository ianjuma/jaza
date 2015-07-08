from django.conf.urls import url

from utils import views

urlpatterns = [
    url('^utils/uploadFile/$', views.FileUploadView.as_view(), name='upload'),
    url('^hydra/$', views.NumQueuedCallsView.as_view(), name='hydra'),
    url('^sleuth/$', views.SleuthView.as_view(), name='sleuth'),
    url('^crunch/$', views.CrunchView.as_view(), name='crunch'),
]
