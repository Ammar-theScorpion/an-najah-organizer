from django.forms import ModelForm
from django import forms
from .models import RoomDetails
from .models import Room
from .models import Building
from .models import Floor
from .models import RoomItems
from django.forms import modelformset_factory

"""

class CampusForm(forms.Form):
    campus = forms.ModelChoiceField(
        queryset=Campus.objects.all(),
        empty_label=None,
        label="Where Are You At?",

    )
"""


class BuildingForm(forms.Form):
    building = forms.ModelChoiceField(
        queryset=Building.objects.all(),
        empty_label=None,
        label="",
        widget=forms.Select(
            attrs={
                "class": "border rounded px-4 py-2 w-full shadow-md",
                "placeholder": "floor number",
            }
        ),
    )


class FloorForm(ModelForm):
    class Meta:
        model = Floor
        fields = ["floor_number"]
        labels = {"floor_number": "Floor Number"}
        widgets = {
            "floor_number": forms.TextInput(
                attrs={
                    "class": "border rounded px-4 py-2 w-full shadow-md",
                    "placeholder": "floor number",
                }
            ),
        }


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = [
            "room_number",
            "width",
            "height",
            "length",
            "usage",
            "x",
            "y",
        ]
        labels = {"room_number": "Room Number", "usage": "Usage"}
        widgets = {
            "room_number": forms.TextInput(
                attrs={
                    "class": "border rounded px-4 py-2 w-full shadow-md",
                    "placeholder": "room number",
                }
            ),
            "width": forms.TextInput(
                attrs={
                    "class": "border rounded px-4 py-2 w-full shadow-md",
                    "placeholder": "Width",
                }
            ),
            "height": forms.TextInput(
                attrs={
                    "class": "border rounded px-4 py-2 w-full shadow-md ",
                    "placeholder": "Height",
                }
            ),
            "length": forms.TextInput(
                attrs={
                    "class": "border rounded px-4 py-2 w-full shadow-md",
                    "placeholder": "Length",
                }
            ),
            "usage": forms.TextInput(
                attrs={
                    "class": "border rounded px-4 py-2 w-full shadow-md",
                    "placeholder": "Usage",
                }
            ),
            "x": forms.NumberInput(
                attrs={
                    "class": "border rounded px-4 py-2 w-full shadow-md",
                    "placeholder": "X",
                }
            ),
            "y": forms.NumberInput(
                attrs={
                    "class": "border rounded px-4 py-2 w-full shadow-md",
                    "placeholder": "Y",
                }
            ),
        }


class RoomDetailsForm(ModelForm):
    class Meta:
        model = RoomDetails
        fields = ["item", "amount", "model", "attachments", "notes"]
        labels = {
            "item": "Item",
            "amount": "Amount",
            "model": "Model",
            "attachments": "Attachments",
            "notes": "Notes",
        }
        widgets = {
            "item": forms.Select(
                choices=RoomItems.objects.all(),
                attrs={
                    "class": "border rounded px-4 py-2 w-full shadow-md",
                    "placeholder": "Item",
                },
            ),
            "amount": forms.NumberInput(
                attrs={
                    "class": "border rounded px-4 py-2 w-full shadow-md",
                    "placeholder": "Amount",
                }
            ),
            "model": forms.TextInput(
                attrs={
                    "class": "border rounded px-4 py-2 w-full shadow-md",
                    "placeholder": "Model",
                }
            ),
            "attachments": forms.TextInput(
                attrs={
                    "class": "border rounded px-4 py-2 w-full shadow-md",
                    "placeholder": "Attachments",
                }
            ),
            "notes": forms.Textarea(
                attrs={
                    "class": "border rounded px-4 py-2 w-full shadow-md",
                    "placeholder": "Notes",
                }
            ),
        }


RoomDetailsFormSet = modelformset_factory(
    RoomDetails, form=RoomDetailsForm, extra=1
)  # extra defines new empty forms

RoomDetailsFormSetUpdate = modelformset_factory(
    RoomDetails, form=RoomDetailsForm, extra=0
)  # extra defines new empty forms
