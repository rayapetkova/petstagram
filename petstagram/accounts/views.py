from django.shortcuts import render


def login_page(request):
    return render(request, f"accounts/login-page.html")


def register_page(request):
    return render(request, f"accounts/register-page.html")


def profile_delete_page(request, pk):
    return render(request, f"accounts/profile-delete-page.html")


def profile_details_page(request, pk):
    return render(request, f"accounts/profile-details-page.html")


def profile_edit_page(request, pk):
    return render(request, f"accounts/profile-edit-page.html")

