from django.db import models


class Carta(models.Model):
    # Definimos las opciones de rareza en una lista
    OPCIONES_RAREZA = [
        ('C', 'Common'),
        ('UC', 'Uncommon'),
        ('R', 'Rare'),
        ('SR', 'Superrare'),
        ('SEC', 'Secret'),
        ('AA', 'Alternative art'),
        ('SP', 'Special'),
        ('M', 'Manga'),
    ]

    # Campos de la base de datos
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Personaje")
    rareza = models.CharField(max_length=3, choices=OPCIONES_RAREZA, default='C')
    descripcion = models.TextField(verbose_name="Descripción o Efecto")

    # Usamos URLField para que solo acepte enlaces web válidos
    enlace_imagen_frontal = models.URLField(verbose_name="Enlace de la imagen (Delantera)")
    enlace_imagen_trasera = models.URLField(verbose_name="Enlace de la imagen (Trasera)")

    # Esta función hace que en el sistema la carta se llame por su nombre y rareza (Ej: "Luffy - Común")
    def __str__(self):
        return f"{self.nombre} - {self.get_rareza_display()}"

