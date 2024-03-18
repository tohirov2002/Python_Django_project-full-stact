from django.urls import path

from .views import home,about,commander_create,edit_commander,delete_commanders

urlpatterns = [
    path('about/',about,name='about'),
    path('add/',commander_create,name='add_commander'),
    path('edit/<int:pk>',edit_commander,name='edit_commander'),
    path('delete/<int:pk>',delete_commanders,name='commander_delete'),
    path('', home, name='home'),
]