from django import forms
from .models import Room

class CreateRoomForm(forms.ModelForm):
    campaign = forms.ModelChoiceField(queryset=Campaign.objects.all(), required=True)

    class Meta:
        model = Room
        fields = ['password', 'campaign']

class JoinRoomForm(forms.Form):
    room_id = forms.UUIDField()
    password = forms.CharField(widget=forms.PasswordInput)