from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path

urlpatterns = [
    path('', views.MoviesView.as_view()),
    path("<slug:slug>", views.MovieDetailView.as_view(), name="movie_detail")
]
