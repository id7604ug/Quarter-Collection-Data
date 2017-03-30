from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^quarter/(?P<pk>\d+)/$', views.quarter_detail, name='quarter_detail'),
]
