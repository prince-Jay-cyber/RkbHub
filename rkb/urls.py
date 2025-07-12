from django.urls import path
from . import views
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('songs/', views.all_songs, name='all_songs'),
    path('artists/', views.artist_list, name='artist_list'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blogs/', views.blog_list),
    path('events/', views.event_list, name='event_list'),
    path('event/', views.event_list),
    path('submit-song/', views.submit_song, name='submit_song'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('contact/', views.contact_view, name='contact'),
    path('artist/<int:pk>/', views.artist_detail, name='artist_detail'),


  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
