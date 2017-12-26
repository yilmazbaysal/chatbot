from django.db.models.signals import post_save, post_delete

from question_answer.models import Keyword
from question_answer.views import reload_keywords


# Runs when a keyword edited on the admin panel
def keyword_change_handler(sender, instance, **kwargs):
    reload_keywords()
