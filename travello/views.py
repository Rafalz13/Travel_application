from django.shortcuts import render
from .models import Attractions
from django.contrib.auth.models import User

def index(request):
    #pobieranie z bazy danych rekordow
    dests = Attractions.objects.all()

    #liczba obiektów, atrakcji i użytkowników
    user_num = User.objects.count()
    dests_num = Attractions.objects.count()
    #do jakiej strony pod jaka zmienną
    return render(request, 'index.html', {'dests':dests, 'user_num':user_num, 'dests_num': dests_num})

