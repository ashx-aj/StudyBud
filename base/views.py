from django.shortcuts import render
from .models import Room
from .forms import Roomform
# Create your views here.

def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request,'base/home.html',context)


def room(request,rid):
    room = Room.objects.get(id=rid)
    context = {'room': room }
    return render(request,'base/room.html',context)

def createRoom(request):
    form =Roomform()
    context = {"form": form}
    return render(request,'base/room_form.html',context)