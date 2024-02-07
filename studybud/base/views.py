from django.shortcuts import render
from .forms import RoomForm
from .models import Room

# Create your views here.

rooms = [
    {'id':1, 'name':'Lets learn Python'},
    {'id':2, 'name':'Design with me'},
    {'id':3, 'name':'Front end developer'},
]



def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context )


def room(request, pk):
    print(pk)
    # room = None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    room = Room.objects.get(id = pk)
    context = {'room':room}
    return render(request, 'base/room.html', context)



def createRoom(request):
    form = RoomForm
    context = {'form':form}
    return render(request, 'base/room_base.html', context )