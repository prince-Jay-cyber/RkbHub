from django.contrib import admin
from .models import Artist, FeaturedMusic, Song, Event, BlogPost, AdPromotion, SubmittedSong, Subscriber
from .models import Genre
from .models import HeroBanner
from .models import SiteSettings
from .models import Video
from .models import Album

admin.site.site_header = "RKB Music Admin"
admin.site.site_title = "RKB Music Admin Portal"
admin.site.index_title = "Welcome to the RKB Music Admin Portal"

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'stage_name', 'genre', 'country', 'age', 'created_at')
    search_fields = ('full_name', 'stage_name', 'genre', 'country')
    list_filter = ('genre', 'country')



@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'genre', 'release_date', 'is_featured', 'status')
    list_filter = ('genre', 'is_featured', 'status')
    search_fields = ('title', 'artist__full_name', 'artist__stage_name', 'genre', 'tags')
    autocomplete_fields = ['artist']


@admin.register(FeaturedMusic)
class FeaturedMusicAdmin(admin.ModelAdmin):
    list_display = ('song', 'featured_on', 'start_date', 'end_date', 'display_order')
    list_filter = ('start_date', 'end_date')
    search_fields = ('song__title',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'location', 'is_active')
    list_filter = ('is_active', 'event_date')
    search_fields = ('title', 'description', 'location')


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted', 'is_published')
    list_filter = ('is_published', 'date_posted')
    search_fields = ('title', 'description', 'tags')

@admin.register(AdPromotion)
class AdPromotionAdmin(admin.ModelAdmin):
    list_display = ('title', 'sponsor_name', 'start_date', 'end_date', 'is_active', 'display_order')
    list_filter = ('is_active', 'start_date', 'end_date')
    search_fields = ('title', 'sponsor_name', 'caption')


class SubmittedSongAdmin(admin.ModelAdmin):
    list_display = ['song_title', 'artist_name', 'email', 'submitted_at', 'is_reviewed']
    list_filter = ['is_reviewed']


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_on')
    search_fields = ('email',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(HeroBanner)
class HeroBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    list_filter = ['is_active']


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['site_name', 'updated_at']

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist_name', 'uploaded_at']


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist', 'genre', 'views']