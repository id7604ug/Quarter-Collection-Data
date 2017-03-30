from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^quarter/$', views.quarter_detail, name='quarter_detail'),
    url(r'^editquarter/(?P<pk>\d+)/$', views.edit_quarter, name='edit_quarter'),
]
