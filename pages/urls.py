from django.urls import path 
from . import views

urlpatterns = [
    path('createapi', views.createapi, name='createapi'),
    path('allapi', views.allapi, name='allapi'),
    path('deleteapi/<int:id>', views.deleteapi, name='deleteapi'),
    path('detailapi/<int:id>', views.detailapi, name='detailapi'),
    path('editapi/<int:id>', views.editapi, name='editapi'),
]