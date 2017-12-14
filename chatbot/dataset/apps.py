from django.apps import AppConfig


class DatasetConfig(AppConfig):
    name = 'dataset'

    # This will run when the project is reloaded
    def ready(self):
        # Initial dataset load
        from dataset.models import DATA_SET_MEDIA_PATH
        from question_answer.views import reload_dataset

        reload_dataset(DATA_SET_MEDIA_PATH)
