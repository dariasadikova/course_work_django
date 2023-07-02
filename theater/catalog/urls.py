from django.urls import path
from . import views
from django.urls import re_path


urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^plays/$', views.PlayListView.as_view(), name='plays'),
    re_path(r'^play/(?P<pk>\d+)$', views.PlayDetailView.as_view(), name='play-detail'),

    re_path(r'^actors/$', views.ActorListView.as_view(), name='actors'),
    re_path(r'^actor/(?P<pk>\d+)$', views.ActorDetailView.as_view(), name='actor-detail'),
    re_path('addplay/', views.add_play, name='add-play-admin'),
    
]
