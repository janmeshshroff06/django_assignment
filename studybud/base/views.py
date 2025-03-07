from django.shortcuts import render
from .models import Room

# Create your views here.
rooms = [
    {'id': 1, 'name': 'Lets learn Python!'},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Frontend Development'}, 
]

def home(request):
    rooms = Room.objects.all()
    return render(request, 'base/home.html', {'rooms': rooms})

def room(request, pk):
    room = Room.objects.get(id=pk)
    return render(request, 'base/room.html', {'room': room})

