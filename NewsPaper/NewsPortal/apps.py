from django.apps import AppConfig


class NewsportalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'NewsPortal'

    def ready(self):
        import NewsPortal.signals
