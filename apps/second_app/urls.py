from django.conf.urls import url
from . import views    

urlpatterns = [
    url(r'^dashboard$', views.dashboard), 
    url(r'^addTravel$', views.addTravel),
    url(r'^home$', views.home),
    url(r'^create$', views.create),
    url(r'^join/(?P<id>\d+)$', views.join),
    url(r'^unjoin/(?P<id>\d+)$', views.unjoin),
    url(r'^show/(?P<id>\d+)$', views.showUser),
]