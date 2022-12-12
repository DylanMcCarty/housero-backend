from django.apps import AppConfig


class HouseroConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Housero'

    def ready(self):
        import Housero.signals

        