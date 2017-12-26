from django.apps import AppConfig
from django.db.models.signals import post_save, post_delete


class QuestionAnswerConfig(AppConfig):
    name = 'question_answer'

    # This will run when the project is reloaded
    def ready(self):
        from question_answer.views import reload_keywords
        from question_answer.models import StopWord, ProperNoun
        from question_answer.signals import keyword_change_handler

        # Reload the keyword on startup
        reload_keywords()

        # Connect the signals
        post_save.connect(keyword_change_handler, sender=StopWord)
        post_save.connect(keyword_change_handler, sender=ProperNoun)
        post_delete.connect(keyword_change_handler, sender=StopWord)
        post_delete.connect(keyword_change_handler, sender=ProperNoun)
