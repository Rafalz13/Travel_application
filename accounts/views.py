from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Zły login lub hasło')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        #sprawdzanie czy hasła sa takie same
        if password1 == password2:

            #sprawdzanie czy dany użytkownik juz istnieje
            #messages - wyswietlanie na stronie, przy print tylko w konsoli
            if User.objects.filter(username=username).exists():
                messages.info(request,'Nazwa już istnieje')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email już istnieje')
                return redirect(request,'register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                messages.info(request,'Użytkownik utworzony')
                return redirect('login')
        else:
            messages.info(request,'hasła się różnią..')
            return redirect('register')
        #powrot do strony glownej
        return redirect('/')

    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')