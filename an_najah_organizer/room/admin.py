from django.contrib import admin
from .models import Campus
from .models import Building
from .models import Floor
from .models import Room
from .models import RoomDetails
from .models import Media
from .models import RoomItems

# Register your models here.

admin.site.register(Campus)
admin.site.register(Building)
admin.site.register(Floor)
admin.site.register(Room)
admin.site.register(RoomDetails)
admin.site.register(RoomItems)
admin.site.register(Media)
