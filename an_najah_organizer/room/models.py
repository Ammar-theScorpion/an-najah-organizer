from django.db import models
from utils.g_models import TimeStampModel
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField

User = get_user_model()


class Campus(models.Model):
    id = models.SmallIntegerField(unique=True, null=False, primary_key=True)
    name = models.CharField(null=False, unique=True, blank=False, max_length=100)

    def __str__(self) -> str:
        return f"{self.id}: {self.name}"


class Building(models.Model):
    id = models.IntegerField(unique=True, null=False, primary_key=True)
    name = models.CharField(null=False, unique=True, blank=False, max_length=100)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}"


class Floor(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    floor_number = models.CharField(max_length=10, null=False, blank=False)

    # class Meta:
    #   unique_together = ("building", "floor_number")

    def __str__(self):
        return f"Floor {self.floor_number} - {self.building.name}"


class Room(TimeStampModel):
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    width = models.FloatField(null=False, blank=False)
    length = models.FloatField(null=False, blank=False)
    height = models.FloatField(null=False, blank=False)
    usage = models.CharField(null=False, blank=False, max_length=200)

    x = models.FloatField(null=False, blank=False)
    y = models.FloatField(null=False, blank=False)

    class Meta:
        unique_together = ("campus", "building", "floor", "room_number")

    def __str__(self) -> str:
        return f"room number: {self.room_number} in floor: {self.floor}, in building: {self.building}, in campus: {self.campus}"


class RoomItems(models.Model):
    item = models.CharField(max_length=60, null=False)

    def __str__(self):
        return self.item


class RoomDetails(models.Model):

    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
    item = models.ForeignKey(RoomItems, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.PositiveSmallIntegerField(null=True, blank=True)
    model = models.CharField(max_length=50, null=True, blank=True)
    attachments = ArrayField(
        models.CharField(max_length=50), null=True, blank=True
    )  # stored as a list
    notes = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"item: {self.item.item} has {self.attachments} "


class Media(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="roomImages/", null=True, blank=True)
