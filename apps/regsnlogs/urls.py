from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^travels$', views.travels),
    url(r'^logout$', views.logout),
    url(r'^travels/add_plan$', views.add_plan),
    url(r'^travels/add_plan/(?P<id>\d+)$', views.plan_time),
    url(r'^travels/(?P<id>\d+)/(?P<tid>\d+)$', views.join_plan),
    url(r'^travels/destination/(?P<id>\d+)$', views.destination),
]
