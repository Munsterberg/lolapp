from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.scrim, name='scrim'),
    url(r'^(?P<scrim_id>\d+)/$', views.scrim_detail, name='scrim_detail'),
]
