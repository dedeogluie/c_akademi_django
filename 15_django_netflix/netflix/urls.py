from django.urls import path, include
from .views import Home, ProfileList, ProfileCreate, MovieList
urlpatterns = [
    path("", Home.as_view(), name='Home'),
    path('accounts/', include('allauth.urls')),
    path('profiles/', ProfileList.as_view(), name='profile-list'),
    path('profile/create/', ProfileCreate.as_view(), name='profile-create'),
    path('watch/<int:profile_id>/', MovieList.as_view(), name="movie-list"),
]
