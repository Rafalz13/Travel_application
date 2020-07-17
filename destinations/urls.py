from django.urls import path
from . import views

urlpatterns = [
    path('', views.dest, name='destinations'),
    path('dodaj', views.dodaj, name='dodaj'),
    path('add_hist',views.add_hist, name='add_hist')
]