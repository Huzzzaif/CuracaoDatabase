from django.apps import AppConfig


class CuracaoDevicesDbConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'curacao_devices_db'

    def ready(self):
        import curacao_devices_db.signals

