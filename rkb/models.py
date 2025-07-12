from django.db import models

# Create your models here.
class Artist(models.Model):
    full_name = models.CharField(max_length=100)
    stage_name = models.CharField(max_length=100, blank=True, help_text="Also known as")
    profile_image = models.ImageField(upload_to='artist_profiles/', blank=True, null=True)
    age = models.PositiveIntegerField()
    genre = models.CharField(max_length=100)
    biography = models.TextField(blank=True)
    country = models.CharField(max_length=100, blank=True)
    facebook_link = models.URLField(blank=True)
    twitter_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.stage_name or self.full_name
    
class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    cover_art = models.ImageField(upload_to='song_covers/', blank=True, null=True)
    audio_file = models.FileField(upload_to='songs/')
    genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True, blank=True)
    release_date = models.DateField()
    tags = models.CharField(max_length=200, help_text="Comma-separated tags", blank=True)
    download_link = models.URLField(blank=True)
    streaming_link = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False)
    views = models.PositiveIntegerField(default=0)
    status = models.CharField(
        max_length=10,
        choices=[('draft', 'Draft'), ('published', 'Published')],
        default='published'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    album = models.ForeignKey('Album', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.artist.stage_name or self.artist.full_name}"
    

class FeaturedMusic(models.Model):
    song = models.ForeignKey('Song', on_delete=models.CASCADE)
    featured_on = models.DateTimeField(auto_now_add=True)
    display_order = models.PositiveIntegerField(default=0)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Featured: {self.song.title}"
    

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateTimeField()
    location = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    link = models.URLField(blank=True, help_text="External event link or ticket page")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    description = models.TextField()
    date_posted = models.DateField(auto_now_add=True)
    tags = models.CharField(max_length=200, blank=True, help_text="Comma-separated tags (e.g., reviews, afrobeats, trending)")
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    

class AdPromotion(models.Model):
    title = models.CharField(max_length=200)
    sponsor_name = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='ads/', blank=True, null=True)
    video = models.FileField(upload_to='ads/videos/', blank=True, null=True)
    link = models.URLField(blank=True, help_text="Where the ad redirects to")
    caption = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class SubmittedSong(models.Model):
    full_name = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    song_title = models.CharField(max_length=200)
    cover_art = models.ImageField(upload_to='submitted_covers/', blank=True, null=True)
    audio_file = models.FileField(upload_to='submitted_songs/')
    message = models.TextField(blank=True)  # ✅ Add this line
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_reviewed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.song_title} by {self.artist_name or self.full_name}"

class HeroBanner(models.Model):
    title = models.CharField(max_length=255, help_text="Main title in the hero section")
    subtitle = models.CharField(max_length=255, help_text="Subtitle or description")
    image = models.ImageField(upload_to='hero_banners/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class SiteSettings(models.Model):
    site_name = models.CharField(max_length=255, help_text="The name of the website")
    logo = models.ImageField(upload_to='site_logos/', help_text="Logo image")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = "Site Setting"
        verbose_name_plural = "Site Settings"

class Video(models.Model):
    title = models.CharField(max_length=255)
    artist_name = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='video_thumbnails/')
    video_url = models.URLField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    cover_art = models.ImageField(upload_to='album_covers/')
    genre = models.CharField(max_length=100)
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.artist.stage_name}"
