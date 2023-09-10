from django.shortcuts import render

from petstagram.pets.models import Pet
from petstagram.photos.models import Photo


def find_photo_likes_count(curr_photo):
    curr_photo.likes_count = curr_photo.like_set.count()
    return curr_photo


def pet_add_page(request):
    return render(request, f"pets/pet-add-page.html")


def pet_delete_page(request, username, pet_slug):
    return render(request, f"pets/pet-delete-page.html")


def pet_details_page(request, username, pet_slug):
    curr_pet = Pet.objects.get(slug=pet_slug)
    all_photos = [find_photo_likes_count(photo) for photo in curr_pet.photo_set.all()]
    for c_photo in all_photos:
        c_photo.is_liked = True if c_photo.likes_count > 0 else False

    context = {
        'curr_pet': curr_pet,
        'curr_pet_photos': all_photos,
        'pet_photos_count': len(all_photos)
    }

    return render(request, f"pets/pet-details-page.html", context=context)


def pet_edit_page(request, username, pet_slug):
    return render(request, f"pets/pet-edit-page.html")
