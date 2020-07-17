from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='profil'),
    path('add_hist', views.add_hist, name='add_hist'),
    path('rank', views.rank, name='rank')
]