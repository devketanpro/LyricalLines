from django.contrib import admin

from lyricist_app.models import Country, Song

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('artist', 'title', 'summary')
    search_fields = ('artist', 'title')
    filter_horizontal = ('countries',)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)