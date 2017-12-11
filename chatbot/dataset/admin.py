from django.contrib import admin
from .models import DataFile


def delete_selected(self, request, queryset):
    for instance in queryset.all():
        instance.delete()


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

    actions = [
        delete_selected
    ]


admin.site.register(DataFile, DataFileAdmin)
