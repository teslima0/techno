from django.apps import AppConfig

class FbDjangoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fb_django'

    def ready(self):
        import fb_django.signals