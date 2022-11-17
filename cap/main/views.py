from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def room(request):
    return render(request, 'main/room.html')

def login(request):
    return render(request, 'main/login.html')

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'main/register.html', {
        'form': form,
    })