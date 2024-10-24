from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import CreateView
from .models import Campus
from .models import Media
from .forms import BuildingForm
from .forms import FloorForm
from .forms import RoomForm
from .forms import RoomDetailsForm
from .forms import RoomDetailsFormSetUpdate
from .forms import RoomDetailsFormSet
from .models import Room
from .models import RoomDetails
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


def room_table(request):
    if request.user.is_authenticated:
        rooms = (
            Room.objects.filter(user=request.user)
            .order_by("-created_at")[0:5]
            .prefetch_related()
        )
        return render(request, "pages/home.html", {"rooms": rooms})
    return render(request, "pages/home.html", {})


@login_required
def update_room_view(request, room_id):

    room_instance = get_object_or_404(Room, id=room_id)
    campuses = Campus.objects.all()

    building_form = BuildingForm()
    floor_form = FloorForm(instance=room_instance.floor)
    room_form = RoomForm(instance=room_instance)

    detail_form = RoomDetailsFormSetUpdate(
        queryset=RoomDetails.objects.filter(room=room_instance)
    )

    images = Media.objects.filter(room=room_instance)
    print(RoomDetails.objects.filter(room=room_instance))
    print(RoomDetails.objects.all())
    if request.method == "POST":
        # selected_campus_id = request.POST.get('selected_campus')
        building_form = BuildingForm(request.POST)
        floor_form = FloorForm(request.POST)
        room_form = RoomForm(request.POST)
        detail_form = RoomDetailsForm(request.POST)
        print(detail_form)
        if building_form.is_valid():
            building_data = building_form.cleaned_data

            selected_building = building_data.get("building")
            selected_campus_id = selected_building.campus
            if floor_form.is_valid():
                floor_instance = floor_form.save(commit=False)
                floor_instance.building = selected_building

                if room_form.is_valid():
                    room_instance = room_form.save(commit=False)
                    room_instance.campus = selected_campus_id
                    room_instance.building = selected_building
                    room_instance.floor = floor_instance
                    room_instance.user = request.user

                    floor_form.save()
                    room_instance.save()
                    images = request.FILES.getlist("cs")
                    for image in images:
                        Media.objects.create(room=room_instance, image=image)

                    if detail_form.is_valid():
                        detail_instance = detail_form.save(commit=False)
                        if detail_instance.amount and detail_instance.amount > 0:
                            detail_instance.room = room_instance
                            detail_instance.save()

                    return redirect(reverse("home"))

                else:
                    print("Room form errors:", room_form.errors)

            else:
                print("Floor form errors:", floor_form.errors)

        else:
            print("Building form errors:", building_form.errors)
    print("images", images)
    return render(
        request,
        "rooms/fill_room.html",
        {
            "campuses": campuses,
            "buildings": building_form,
            "floor_form": floor_form,
            "room_form": room_form,
            "detail_form": detail_form,
            "images": images,
        },
    )


@login_required
def create_room_view(request):
    # Initialize the forms
    campuses = Campus.objects.all()
    building_form = BuildingForm()
    floor_form = FloorForm()
    room_form = RoomForm()
    detail_form = RoomDetailsFormSet(queryset=RoomDetails.objects.none())
    print(detail_form)
    if request.method == "POST":
        # selected_campus_id = request.POST.get('selected_campus')
        building_form = BuildingForm(request.POST)
        floor_form = FloorForm(request.POST)
        room_form = RoomForm(request.POST)
        detail_form = RoomDetailsFormSet(
            request.POST
        )  # Populate formset with POST data

        if building_form.is_valid():
            building_data = building_form.cleaned_data

            selected_building = building_data.get("building")
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
                    room_instance.user = request.user

                    floor_form.save()
                    room_instance.save()
                    images = request.FILES.getlist("cs")[1:]
                    for image in images:
                        Media.objects.create(room=room_instance, image=image)

                    if detail_form.is_valid():
                        for form in detail_form:
                            print("formm", form)
                            if form.cleaned_data:
                                detail_instance = form.save(commit=False)
                                if (
                                    detail_instance.amount
                                    and detail_instance.amount > 0
                                ):
                                    detail_instance.room = room_instance
                                    detail_instance.save()

                        print("detail_form", detail_form)

                        return redirect(reverse("home"))

                    else:
                        print("detail_form ERROR", detail_form.errors)

                else:
                    print("Room form errors:", room_form.errors)

            else:
                print("Floor form errors:", floor_form.errors)

        else:
            print("Building form errors:", building_form.errors)

    return render(
        request,
        "rooms/fill_room.html",
        {
            "campuses": campuses,
            "buildings": building_form,
            "floor_form": floor_form,
            "room_form": room_form,
            "detail_form": detail_form,
        },
    )
