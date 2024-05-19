from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.get_users, name='user-list'),
    path('users/new/', views.create_user, name='user-create'),
    path('users/', views.get_notes),  # localhost:8000/api/notes/
    path('notes/new/', views.create_note),
]
