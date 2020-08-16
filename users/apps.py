from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    
    # Para importar el signal que se creo en signals.py
    def ready(self):
        import users.signals
