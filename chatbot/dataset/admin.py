from django.contrib import admin
from .models import DataFile


class DataFileAdmin(admin.ModelAdmin):
    list_display = [
        'mnemonic',
        'file',
        'date_time'
    ]

    list_filter = [
        'mnemonic',
        'date_time'
    ]


admin.site.register(DataFile, DataFileAdmin)
