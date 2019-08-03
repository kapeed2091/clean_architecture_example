from django.apps import AppConfig


class FbPostV2AppConfig(AppConfig):
    name = "clean_arch_app"

    def ready(self):
        from clean_arch_app import signals # pylint: disable=unused-variable
