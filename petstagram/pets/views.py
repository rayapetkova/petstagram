from django.shortcuts import render

# Create your views here.
def pet_add_page(request):
    return render(request, f"pets/pet-add-page.html")


def pet_delete_page(request, username, pet_name):
    return render(request, f"pets/pet-delete-page.html")


def pet_details_page(request, username, pet_name):
    return render(request, f"pets/pet-details-page.html")


def pet_edit_page(request, username, pet_name):
    return render(request, f"pets/pet-edit-page.html")
