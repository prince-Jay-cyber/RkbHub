from django.shortcuts import render, redirect
from .models import Song, BlogPost, Artist, Event
from .forms import SubmittedSongForm
from .forms import SubscriberForm
from .models import HeroBanner
from .models import Video
from .models import Album
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import get_object_or_404


def home(request):
    featured_songs = Song.objects.filter(is_featured=True, status='published').order_by('-created_at')[:6]
    latest_songs = Song.objects.filter(status='published').order_by('-created_at')[:8]
    latest_blogs = BlogPost.objects.filter(is_published=True).order_by('-date_posted')[:3]
    latest_events = Event.objects.filter(is_active=True).order_by('-event_date')[:3]   
    hero = HeroBanner.objects.filter(is_active=True).last() 
    latest_videos = Video.objects.order_by('-uploaded_at')[:4]
    top_albums = Album.objects.order_by('-views')[:5]
    artists = Artist.objects.all()[:6]  # or filter featured

    return render(request, 'rkb/home.html', {
        'featured_songs': featured_songs,
        'latest_songs': latest_songs,
        'latest_blogs': latest_blogs,
        'latest_events': latest_events,
        'hero': hero,
        'latest_videos': latest_videos,
        'top_albums': top_albums,
        'artists': artists,
    })

def all_songs(request):
    songs = Song.objects.filter(status='published').order_by('-created_at')
    return render(request, 'rkb/all_songs.html', {'songs': songs})

def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'rkb/artist.html', {'artists': artists})

def blog_list(request):
    blog_posts = BlogPost.objects.filter(is_published=True).order_by('-date_posted')
    return render(request, 'rkb/blog.html', {'blog_posts': blog_posts})

def event_list(request):
    events = Event.objects.order_by('-event_date') 
    return render(request, 'rkb/events.html', {'events': events})

def submit_song(request):
    success = False
    if request.method == 'POST':
        form = SubmittedSongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            success = True
            form = SubmittedSongForm()
    else:
        form = SubmittedSongForm()
    return render(request, 'rkb/submit_song.html', {'form': form, 'success': success})

def subscribe(request):
    success = False
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = SubscriberForm()
    else:
        form = SubscriberForm()
    return render(request, 'rkb/subscribe.html', {'form': form, 'success': success})

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # You can handle saving or emailing here
        # Example: send email (optional setup)
        send_mail(
            subject=f"New message from {name}",
            message=message,
            from_email=email,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
            fail_silently=True,
        )

        messages.success(request, "Your message has been sent!")
        return redirect('contact')

    return render(request, 'rkb/contact.html')

def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    return render(request, 'rkb/artist_detail.html', {'artist': artist})