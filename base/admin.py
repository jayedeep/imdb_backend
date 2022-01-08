from django.contrib import admin
from .models import Movies
# Register your models here.
@admin.register(Movies)
class MoviesModelAdmin(admin.ModelAdmin):
    list_display = ['name','rating','realise_date','duration']