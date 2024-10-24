from django.urls import path
from .views import create_room_view
from .views import update_room_view

app_name = "rooms"
urlpatterns = [
    path("", create_room_view, name="fill"),
    path("edit/<int:room_id>/", update_room_view, name="edit"),
]
