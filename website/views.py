from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .form import SignUpForm, FormProfile
from .models import Convidado, Convite, Imagen

# Create your views here.
def home(request):
    imagens = Imagen.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        #password = request.POST['password']

        user = authenticate(request, username=username, password='a<Ow4£8v>@78')
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('home')
    else:
        return render(request, 'login.html', {'imagens':imagens})

def index(request):
    imagens = Imagen.objects.all()
    if request.user.is_authenticated:
        convites = Convite.objects.all()
        convidados = Convidado.objects.filter(convidado=request.user)

        return render(request, 'index.html', {'convites':convites, 'convidados':convidados,'imagens':imagens})
    else:
        return redirect('home')

def profile(request):
    imagens = Imagen.objects.all()
    if request.user.is_authenticated:
        convidado = Convidado.objects.filter(convidado=request.user)
        return render(request, 'profile.html', {'convidado':convidado, 'imagens':imagens})
    else:
        return redirect('home')

def customer_profile(request):
    imagens = Imagen.objects.all()
    if request.user.is_authenticated:
        convidado = Convidado.objects.filter(convidado=request.user)
        costumer_profi = Convidado.objects.get(convidado=request.user)
        form = FormProfile(request.POST or None, instance=costumer_profi)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, 'profile_edit.html', {'form':form, 'convidado':convidado, 'imagens':imagens})
    else:
        return redirect('profile')

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect(home)
    else:
        return redirect('home')
