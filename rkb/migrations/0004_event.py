# Generated by Django 5.2.4 on 2025-07-12 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rkb', '0003_featuredmusic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('event_date', models.DateTimeField()),
                ('location', models.CharField(blank=True, max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='event_images/')),
                ('link', models.URLField(blank=True, help_text='External event link or ticket page')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
