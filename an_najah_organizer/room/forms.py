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
        label="",
        widget=forms.Select(attrs={
                    'class': 'border rounded px-4 py-2 w-full shadow-md',
                    'placeholder': 'floor number'
                })
    )


class FloorForm(ModelForm):
    class Meta:
        model = Floor
        fields = ['floor_number']
        labels = {"floor_number": "Floor Number"}
        widgets = {
            'floor_number': forms.TextInput(attrs={'class': 'border rounded px-4 py-2 w-full shadow-md', 'placeholder': 'floor number'}),
        }

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = [
            'room_number',
        ]
        labels = {"room_number": "Room Number"}
        widgets = {
            'room_number': forms.TextInput(attrs={'class': 'border rounded px-4 py-2 w-full shadow-md', 'placeholder': 'room number'}),
        }

class RoomDetailsForm(ModelForm):
    class Meta:
        model = RoomDetails
        fields = [
            'width', 'height', 'length', 'windows', 'doors', 'lcd', 'condition'
        ]
        labels = {"condition": "Number Of Conditions", "lcd": "Number Of LCDs", "windows": "Number Of Windows", "doors": "Number Of Doors"}
        widgets = {
            'width': forms.TextInput(attrs={'class': 'border rounded px-4 py-2 w-full shadow-md', 'placeholder': 'Width'}),
            'height': forms.TextInput(attrs={'class': 'border rounded px-4 py-2 w-full shadow-md ', 'placeholder': 'Height'}),
            'length': forms.TextInput(attrs={'class': 'border rounded px-4 py-2 w-full shadow-md', 'placeholder': 'Length'}),
            'windows': forms.NumberInput(attrs={'class': 'border rounded px-4 py-2 w-full shadow-md', 'placeholder': 'Windows'}),
            'doors': forms.NumberInput(attrs={'class': 'border rounded px-4 py-2 w-full shadow-md', 'placeholder': 'Doors'}),
            'lcd': forms.NumberInput(attrs={'class': 'border rounded px-4 py-2 w-full shadow-md'}),
            'condition': forms.NumberInput(attrs={'class': 'border rounded px-4 py-2 w-full shadow-md'}),
        }