from django import forms
from .models import SubmittedSong, Subscriber


class SubmittedSongForm(forms.ModelForm):
    class Meta:
        model = SubmittedSong
        fields = ['full_name', 'artist_name', 'email', 'song_title', 'cover_art', 'audio_file', 'message']

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email',
                'class': 'form-control'
            }),
        }