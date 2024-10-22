from django.db import models
from utils.g_models import TimeStampModel

class Campus(models.Model):
    id = models.SmallIntegerField(unique=True, null=False, primary_key=True)
    name = models.CharField(null=False, unique=True, blank=False, max_length=100)

    def __str__(self) -> str:
        return f"campus: {self.name}, number {self.id}"

class Building(models.Model):
    id = models.IntegerField(unique=True, null=False, primary_key=True)
    name = models.CharField(null=False, unique=True, blank=False, max_length=100)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}"

class Floor(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    floor_number = models.IntegerField(blank=False)

    class Meta:
        unique_together = ('building', 'floor_number')

    def __str__(self):
        return f"Floor {self.floor_number} - {self.building.name}"


class Room(models.Model):
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=30)

    class Meta:
        unique_together = ('campus', 'building', 'floor', 'room_number')

    def __str__(self) -> str:
        return f"room number: {self.room_number} in floor: {self.floor}, in building: {self.building}, in campus: {self.campus}"

class RoomDetails(TimeStampModel):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    width = models.FloatField(null=False, blank=False)
    length = models.FloatField(null=False, blank=False)
    height = models.FloatField(null=False, blank=False)
    usage = models.CharField(null=False, blank=False, max_length=200)
    
    windows = models.SmallIntegerField(null=False, blank=False, default=1)
    doors = models.SmallIntegerField(null=False, blank=False, default=1)
    lcd = models.SmallIntegerField(null=False, blank=False, default=1)
    condition = models.SmallIntegerField(null=False, blank=False, default=1)


    def __str__(self) -> str:
        return f"room: {self.room.room_number} is {self.width} wide and {self.height} heigh"
