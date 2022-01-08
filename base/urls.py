from django.urls import path
from . views import MoviesApi,MoviesApiSearch

urlpatterns = [
    path('', MoviesApi.as_view()), # will be use for Simple CRUD
    path('filter/<str:sorted_by>', MoviesApi.as_view()),  # will Be used For Sorting by name..etc.
    path('search/',MoviesApiSearch.as_view(),name="MoviesApiSearch"), # To search by Name and Description.
    path('<int:pk>', MoviesApi.as_view()), #  will be use for Simple CRUD
]