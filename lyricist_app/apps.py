from django.apps import AppConfig


class LyricistAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "lyricist_app"

    def ready(self):
        import lyricist_app.signal