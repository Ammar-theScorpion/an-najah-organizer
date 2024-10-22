from django.urls import path
from .views import create_room_view

app_name="rooms"
urlpatterns = [
    path("", create_room_view, name="fill")
]
