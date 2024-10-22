from django.forms import ModelForm
from django import forms
from .models import RoomDetails
from .models import Room
from .models import Floor
from .models import Building


'''

class CampusForm(forms.Form):
    campus = forms.ModelChoiceField(
        queryset=Campus.objects.all(),
        empty_label=None,
        label="Where Are You At?",

    )
'''
class BuildingForm(forms.Form):
    building = forms.ModelChoiceField(
        queryset=Building.objects.all(),
        empty_label=None,
        label="Where Are You At?",

    )


class FloorForm(ModelForm):
    class Meta:
        model = Floor
        fields = ['floor_number']


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = [
            'room_number',
        ]

class RoomDetailsForm(ModelForm):
    class Meta:
        model = RoomDetails
        fields = [
            'width', 'height', 'length', 'windows', 'doors', 'lcd', 'condition'
        ]