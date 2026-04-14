from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cartas_app.urls')), # Conectamos las urls de la app
]
