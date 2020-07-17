from django.urls import path
from . import views

# views.login - funkcja login
urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')

]