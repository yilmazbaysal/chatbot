from django.apps import AppConfig


class DatasetConfig(AppConfig):
    name = 'dataset'

    # This will run when the project is reloaded
    def ready(self):
        # Register the signals
        import dataset.signals

        # Initial dataset load
        from question_answer.views import reload_dataset

        reload_dataset()
