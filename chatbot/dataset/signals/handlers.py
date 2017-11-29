from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver

from dataset.models import DataFile
from question_answer.views import reload_dataset


@receiver([post_save, post_delete], sender=DataFile)
def data_file_change_handler(sender, instance, **kwargs):
    reload_dataset()
