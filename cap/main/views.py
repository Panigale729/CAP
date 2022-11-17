from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm

# Create your views here.


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('room')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('room')
            else:
                messages.info(request, 'Username OR password is incorrect')

        return render(request, 'main/login.html', {

        })

def register(request):
    if request.user.is_authenticated:
        return redirect('room')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, f'Account was created for {user}')

                return redirect('login')

        return render(request, 'main/register.html', {
            'form': form,
        })
    
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def room(request):
    return render(request, 'main/room.html')