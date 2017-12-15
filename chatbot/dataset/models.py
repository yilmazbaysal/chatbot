import os
from django.db import models

from question_answer.views import reload_dataset

DATA_SET_MEDIA_PATH = 'data_set'


def data_file_upload_directory(instance, filename):
    return os.path.join(DATA_SET_MEDIA_PATH, os.path.basename(filename))


class DataFile(models.Model):
    mnemonic = models.CharField(max_length=100)
    file = models.FileField(upload_to=data_file_upload_directory)
    date_time = models.DateTimeField(auto_now=True)
    is_auto_generated = models.BooleanField(default=False)

    def __str__(self):
        return self.mnemonic

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super(DataFile, self).save()

        # Reinitialize the bot instance
        reload_dataset(DATA_SET_MEDIA_PATH)

    def delete(self, using=None, keep_parents=False):
        super(DataFile, self).delete()

        # Reinitialize the bot instance
        reload_dataset(DATA_SET_MEDIA_PATH)


class GeneratedDataFile(DataFile):
    class Meta:
        proxy = True

        verbose_name = 'Generated File'
        verbose_name_plural = 'Generated Files'
