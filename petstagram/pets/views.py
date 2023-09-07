from django.shortcuts import render

from petstagram.pets.models import Pet
from petstagram.photos.models import Photo


# Create your views here.
def pet_add_page(request):
    return render(request, f"pets/pet-add-page.html")


def pet_delete_page(request, username, pet_slug):
    return render(request, f"pets/pet-delete-page.html")


def pet_details_page(request, username, pet_slug):
    curr_pet = Pet.objects.get(slug=pet_slug)
    all_photos = curr_pet.photo_set.all()

    context = {
        'curr_pet': curr_pet,
        'curr_pet_photos': all_photos
    }

    return render(request, f"pets/pet-details-page.html", context=context)


def pet_edit_page(request, username, pet_slug):
    return render(request, f"pets/pet-edit-page.html")
