from django.urls import path, include

from petstagram.pets import views

urlpatterns = (
    path('add/', views.add_pet, name='add-pet'),
    path('<str:username>/pet/<slug:pet_name>/', include(
        (path('', views.pet_details_page, name='pet-details-page'),
         path('edit/', views.edit_pet_page, name='pet-edit-page'),
         path('delete/', views.delete_pet_page, name='pet-delete-page')
         ))),
)
