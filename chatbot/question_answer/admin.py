from django.contrib import admin

from question_answer.models import StopWord, ProperNoun


def delete_selected(self, request, queryset):
    for instance in queryset.all():
        instance.delete()


class StopWordAdmin(admin.ModelAdmin):
    list_display = [
        'keyword',
    ]

    list_filter = [
        'keyword',
    ]

    exclude = [
        'keyword_type',
    ]

    actions = [
        delete_selected
    ]

    def get_queryset(self, request):
        queryset = super(StopWordAdmin, self).get_queryset(request).filter(
            keyword_type=StopWord.KEYWORD_TYPE_STOP_WORD
        )

        return queryset

    def save_model(self, request, obj, form, change):
        obj.keyword_type = StopWord.KEYWORD_TYPE_STOP_WORD
        obj.save()


class ProperNounAdmin(admin.ModelAdmin):
    list_display = [
        'keyword',
    ]

    list_filter = [
        'keyword',
    ]

    exclude = [
        'keyword_type',
    ]

    actions = [
        delete_selected
    ]

    def get_queryset(self, request):
        queryset = super(ProperNounAdmin, self).get_queryset(request).filter(
            keyword_type=ProperNoun.KEYWORD_TYPE_PROPER_NOUN
        )

        return queryset

    def save_model(self, request, obj, form, change):
        obj.keyword_type = ProperNoun.KEYWORD_TYPE_PROPER_NOUN
        obj.save()


admin.site.register(StopWord, StopWordAdmin)
admin.site.register(ProperNoun, ProperNounAdmin)
