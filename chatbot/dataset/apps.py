from django.apps import AppConfig


class DatasetConfig(AppConfig):
    name = 'dataset'

    # This will run when the project is reloaded
    def ready(self):
        from question_answer.views import reload_dataset

        reload_dataset()
