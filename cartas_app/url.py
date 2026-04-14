from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cartas'),
    path('ver/', views.ver_cartas, name='ver_cartas'),
    path('crear/', views.crear_carta, name='crear_carta'),
    path('borrar/<int:pk>/', views.borrar_carta, name='borrar_carta'),
    path('modificar/<int:pk>/', views.modificar_carta, name='modificar_carta'),
]
