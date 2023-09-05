from django.shortcuts import render

from petstagram.photos.models import Photo


def find_photo_likes_count(curr_photo):
    curr_photo.likes_count = curr_photo.like_set.count()
    return curr_photo


def home_page(request):
    all_photos = [find_photo_likes_count(photo) for photo in Photo.objects.all()]
    for c_photo in all_photos:
        c_photo.is_liked = True if c_photo.likes_count > 0 else False

    context = {
        'photos': all_photos
    }

    return render(request, f"common/home-page.html", context=context)
