from django.urls import path, include

from petstagram.accounts import views

urlpatterns = (
    path('register/', views.register_page, name='register-user'),
    path('login/', views.login_page, name='login-user'),
    path('profile/<int:pk>/', include([
         path('', views.profile_details_page, name='profile-details'),
         path('edit/', views.profile_edit_page, name='edit-profile'),
         path('delete/', views.profile_delete_page, name='delete-profile')
         ])),
)
