from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Room, Participant
from .forms import CreateRoomForm, JoinRoomForm

def create_room(request):
    if request.method == 'POST':
        form = CreateRoomForm(request.POST)
        if form.is_valid():
            room - form.save(commit=False)
            room.host = request.user
            room.save()
            Participant.objects.create(user=request.user, room=room)
            return redirect('master_room', room_id=room.id)
    else:
        form = CreateRoomForm()
    return render(request, 'create_room.html', {'form': form})

@login_required
def join_room(request):
    if request.method == 'POST':
        form = JoinRoomForm(request.POST)
        if form.is_valid():
            room = get_object_or_404(Room, id=form.cleaned_data['room_id'])
            if room.password == form.cleaned_data['password']:
                Participant.objects.create(user=request.user, room=room)
                return redirect('player_room', room_id=room.id)
    else:
        form = JoinRoomForm()
    return render(request, 'join_room.html', {'form': form})