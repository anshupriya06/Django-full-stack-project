from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('create/', views.item_create, name='item_create'),
    path('<int:item_id>/edit/', views.item_edit, name='item_edit'),
    path('<int:item_id>/delete/', views.item_delete, name='item_delete'),
]
