from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.contrib.auth.models import User, auth
from travello.models import History
from django.contrib import messages
from django.db.models import Max

def home(request):
    #do sekcji historia
    hist = History.objects.all()

    #unika duplikatów, do sekcji 'zaliczone'
    zal =History.objects.values('name', 'city', 'user', 'voivodeship', 'date').annotate(max_id=Max('id'))

    return render(request, 'profil.html', {'hist':hist, 'zal': zal})


def rank (request):
    users= History.objects.all()
    zal = History.objects.values('id', 'name', 'city', 'user', 'voivodeship', 'date').annotate(max_id=Max('user'))


    # dict_user = {}
    # for usr in zal:
    #     num = 0
    #     username = usr
    #     for usr2 in zal:
    #         if usr2 == username:
    #             num +=1
    #     dict_user = {'num': num, 'usr':usr}

    return render(request, 'rank.html',{'users':users,'zal': zal})

#zapis do tabeli History
def add_hist(request):
    user = request.POST['user']
    name = request.POST['name']
    city = request.POST['city']
    voivodeship = request.POST['voivodeship']
    date = request.POST['date']

    history = History(user=user, name=name, city=city, voivodeship=voivodeship, date=date)
    history.save();
    messages.info(request, 'Oferta utworzona')
    return redirect('profil')
