from django.db import models


class Keyword(models.Model):
    KEYWORD_TYPE_STOP_WORD = 'S'
    KEYWORD_TYPE_PROPER_NOUN = 'P'

    KEYWORD_TYPE_CHOICES = (
        (KEYWORD_TYPE_STOP_WORD, 'Stop Word'),
        (KEYWORD_TYPE_PROPER_NOUN, 'Proper Noun'),
    )

    keyword = models.CharField(max_length=50, unique=True, null=False, blank=False)
    keyword_type = models.CharField(max_length=1, choices=KEYWORD_TYPE_CHOICES, null=False, blank=False)


class StopWord(Keyword):
    class Meta:
        proxy = True

        verbose_name = 'Stop Word'
        verbose_name_plural = 'Stop Words'


class ProperNoun(Keyword):
    class Meta:
        proxy = True

        verbose_name = 'Proper Noun'
        verbose_name_plural = 'Proper Nouns'
