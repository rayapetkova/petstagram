from django.contrib import admin

from petstagram.photos.models import Photo


@admin.register(Photo)
class PhotosAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'date_of_publication', 'location', 'all_tagged_pets')

    def all_tagged_pets(self, current_photo_object):
        all_tagged_pets = current_photo_object.tagged_pets.all()
        if not all_tagged_pets:
            return 'No pets'

        return ', '.join(p.name for p in all_tagged_pets)
