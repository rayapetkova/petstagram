from django.shortcuts import render

from petstagram.photos.models import Photo


def home_page(request):
    all_photos = Photo.objects.all()

    context = {
        'photos': all_photos
    }

    return render(request, f"common/home-page.html", context=context)
