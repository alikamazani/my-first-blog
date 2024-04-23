from django.urls import path
from . import views
urlpatterns = [
    path('blogs', views.blogs_page, name='blogs-page')
]