import os
from django.db import models
from django.utils import timezone


def data_file_upload_directory(instance, filename):
    return 'data_set/{0}/{1}'.format(timezone.now().strftime('%Y'), os.path.basename(filename))


class DataFile(models.Model):
    mnemonic = models.CharField(max_length=100)
    file = models.FileField(upload_to=data_file_upload_directory)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return self.mnemonic
