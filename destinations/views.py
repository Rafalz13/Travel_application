from django.shortcuts import render, redirect
from django.contrib import messages
from travello.models import Attractions, History
from django.contrib.auth.models import User, auth
from django.db.models import Q

def dest(request):
    dests = Attractions.objects.all()           #wszystkie obiekty
    dests_num = Attractions.objects.count()     #liczba obiektów  tabeli
    user_num = User.objects.count()

#szukanie po zarejestrowanych punktach
    query1 = request.GET.get("q_nam")
    query2 = request.GET.get("q_aut")
    query3 = request.GET.get("q_cit")
    query4 = request.GET.get("q_voi")

    #mechanizm wyszukiwania - za bardzo manualnie- sprawdzic szukanie po kilku polach
    if query1:          #kiedy name jest wpisany
        if query2:      #kiedy autor jest wpisany
            if query3:  #kiedy miasto jest wpisane
                dests = dests.filter(Q(name__icontains=query1) |
                                     Q(author__icontains=query2)|
                                     Q(city__icontains=query3)
                                     )
            else:
                dests = dests.filter(Q(name__icontains=query1) |
                                     Q(author__icontains=query2))


        else:
            dests = dests.filter(Q(name__icontains=query1))

    if query2:          #kiedy autor jest wpisany
        if query1:      #kiedy name jest wpisany
            if query3:  #kiedy miasto jest wpisane
                dests = dests.filter(Q(name__icontains=query1) |
                                     Q(author__icontains=query2)|
                                     Q(city__icontains=query3)
                                     )
            else:
                dests = dests.filter(Q(name__icontains=query1) |
                                     Q(author__icontains=query2))


        else:
            dests = dests.filter(Q(author__icontains=query2))

    if query3:          #kiedy miasto jest wpisany
        if query1:      #kiedy name jest wpisany
            if query2:  #kiedy autor jest wpisane
                dests = dests.filter(Q(author__icontains=query3) |
                                     Q(name__icontains=query1)|
                                     Q(city__icontains=query2)
                                     )
            else:
                dests = dests.filter(Q(city__icontains=query3) |
                                     Q(name__icontains=query1))


        else:
            dests = dests.filter(Q(city__icontains=query3))

    if query4:
        dests = dests.filter(Q(voivodeship__icontains=query4))


    return render(request, 'destinations.html', {'dests' : dests, 'dests_num': dests_num, 'user_num': user_num})


#zdjecia po dodaniu sa defaultowo, w panelu dodaja się do pic\ - jakos to ogarnąć
def dodaj(request):
    if request.method == 'POST':
        name = request.POST['name']
        author = request.POST['author']
        city = request.POST['city']
        street = request.POST['street']
        voivodeship = request.POST['voivodeship']
        price = request.POST['price']
        img = request.POST['img']

        desc = request.POST['desc']
        duration = request.POST['duration']
        num_people = request.POST['num_people']
        offer = request.POST['offer']


        if name is None:
            messages.info(request, 'Nazwa niepełna')
            return redirect('/')
        else:
            attraction = Attractions(name=name, author=author, city=city, street=street, voivodeship=voivodeship, duration=duration, num_people=num_people, img="pics/"+img, desc=desc, offer=offer, price=price)
            attraction.save();

            messages.info(request, 'Oferta utworzona')
            return redirect('destinations')
    return redirect('/')

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