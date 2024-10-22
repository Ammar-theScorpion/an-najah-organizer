from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import CreateView
from .models import Campus
from .models import Building
from .forms import BuildingForm
from .forms import FloorForm
from .forms import RoomForm
from .forms import RoomDetailsForm
# Create your views here.


def create_room_view(request):
    # Initialize the forms
    campuses = Campus.objects.all()
    building_form = BuildingForm()
    floor_form = FloorForm()
    room_form = RoomForm()
    detail_form = RoomDetailsForm()

    if request.method == 'POST':
        #selected_campus_id = request.POST.get('selected_campus')
        building_form = BuildingForm(request.POST)
        floor_form = FloorForm(request.POST)
        room_form = RoomForm(request.POST)
                
        if building_form.is_valid():
                building_data = building_form.cleaned_data

                selected_building = building_data.get('building')
                selected_campus_id = selected_building.campus
                print("selected_campus_id", selected_campus_id)
                if floor_form.is_valid():
                    floor_instance = floor_form.save(commit=False)
                    floor_instance.building = selected_building

                    if room_form.is_valid():
                        room_instance = room_form.save(commit=False)
                        room_instance.campus = selected_campus_id
                        room_instance.building = selected_building
                        room_instance.floor = floor_instance

                        floor_form.save()
                        room_instance.save()

                        return redirect(reverse('home'))

                    else:
                        print("Room form errors:", room_form.errors)

                else:
                    print("Floor form errors:", floor_form.errors)

        else:
            print("Building form errors:", building_form.errors)


    return render(request, 'rooms/fill_room.html', {
        'campuses': campuses,
        'buildings': building_form,
        'floor_form': floor_form,
        'room_form': room_form,
        'detail_form': detail_form
    })
