# Para automaticamente luego de crear un profile use el archivo dado.(ejm: foto)
from django.db.models.signals import post_save

# El modelo User sera el sender(el que envia el signal)
from django.contrib.auth.models import User

# La funcion(decorador) receiver. Es la que recibe el signal y hace la instruccion.
from django.dispatch import receiver

# Importar el modelo(base de datos) que se utilizara.
from .models import Profile




# El decorador recibe el signal(post_save) y el sender.
@receiver(post_save, sender=User)
# Funcion para la creacion del profile.
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
# Para salvar el profile.
def save_profile(sender, instance, **kwargs):
    instance.profile.save()





