"""
ASGI config for ProyectoTCG project.
"""
import os
from django.core.asgi import get_asgi_application

# Asegúrate de que esto coincide con el nombre de tu proyecto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProyectoTCG.settings')

application = get_asgi_application()