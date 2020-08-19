from django.db import models
from django.contrib.auth.models import User
# Libreria de Pillow para trabajar con imagenes.
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # Metodo para ajustar imagenes automaticamente.
    def save(self, *args, **kwargs):
        super().save()

        # Declaramos la variable a trabajar.
        img = Image.open(self.image.path)

        # Se pone una condicional para poner el limite de altura y ancho de la imagen.
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

