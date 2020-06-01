from django.contrib import admin

# Register your models here.
from .models import Category, Genre, Movie, MovieShorts, Actor, Raiting, RaitingStar, Reviews

admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(MovieShorts)
admin.site.register(Actor)
admin.site.register(Raiting)
admin.site.register(RaitingStar)
admin.site.register(Reviews)
