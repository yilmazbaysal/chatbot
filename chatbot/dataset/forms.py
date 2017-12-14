from django import forms
from django.contrib.postgres.forms import SimpleArrayField, ValidationError

from dataset.models import DataFile


def lowercase_validator(keyword_list):
    """
    Checks the ArrayField whether it is all lowercase or not. Raise ValidationError if contains uppercase letter.
    :param keyword_list: List of keywords coming from an ArrayField.
    :return: No return value.
    """
    for keyword in keyword_list:
        if not keyword.islower():
            raise ValidationError('The keywords must be all lowercase!', code='invalid')


class GenerateDataFileForm(forms.ModelForm):

    keywords_1 = SimpleArrayField(
        forms.CharField(required=True),
        delimiter='|',
        required=True,
        validators=[lowercase_validator],
        label='#1 Keyword List (Use "|" as delimiter)'
    )
    keywords_2 = SimpleArrayField(
        forms.CharField(required=True),
        delimiter='|',
        required=True,
        validators=[lowercase_validator],
        label='#2 Keyword List (Use "|" as delimiter)'
    )
    keywords_3 = SimpleArrayField(
        forms.CharField(required=True),
        delimiter='|',
        required=False,
        validators=[lowercase_validator],
        label='#3 Keyword List (Use "|" as delimiter)'
    )
    keywords_4 = SimpleArrayField(
        forms.CharField(required=True),
        delimiter='|',
        required=False,
        validators=[lowercase_validator],
        label='#4 Keyword List (Use "|" as delimiter)'
    )

    answer = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = DataFile
        fields = [
            'mnemonic',
        ]
