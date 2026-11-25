
from django.urls import path
from . import views

urlpatterns = [
    path('avtomobillar/', views.avtomobillar_royxati, name='avtomobillar_royxati'),

    path('avtomobillar-listview/', views.AvtomobilListView.as_view(), name='avtomobillar_listview'),

    path('avtomobil/<int:id>/', views.avtomobil_detail, name='avtomobil_detail'),
    path('avtomobil-qoshish/', views.avtomobil_qoshish, name='avtomobil_qoshish'),
]
