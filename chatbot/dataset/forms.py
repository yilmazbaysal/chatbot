import string

from django import forms
from django.contrib.postgres.forms import SimpleArrayField, ValidationError

from dataset.models import DataFile


def keyword_validator(keyword_list):
    """
    Checks the ArrayField whether it is all lowercase or not. Raise ValidationError if contains uppercase letter.
    :param keyword_list: List of keywords coming from an ArrayField.
    :return: No return value.
    """
    for i in range(len(keyword_list)):
        # Keyword length check
        if len(keyword_list[i]) < 3:
            raise ValidationError(
                'Ensure the keyword {} has at least 3 characters (it has {}).'.format(i, len(keyword_list[i])),
                code='invalid'
            )

        # Keyword character check
        for letter in keyword_list[i]:
            if not letter.islower():
                raise ValidationError('The keywords must be all lowercase!', code='invalid')
            elif letter.isdigit():
                raise ValidationError('The all characters of keywords can not be numeric!', code='invalid')
            else:
                for c in letter:
                    if c != '-' and c in string.punctuation:
                        raise ValidationError('The keywords can not include any punctuation! Except "-".', code='invalid')


class GenerateDataFileForm(forms.ModelForm):
    mnemonic = forms.CharField(min_length=3, required=True)

    keywords_1 = SimpleArrayField(
        forms.CharField(required=True),
        delimiter='|',
        required=True,
        validators=[keyword_validator],
        label='#1 Keyword List (Use "|" as delimiter)'
    )
    keywords_2 = SimpleArrayField(
        forms.CharField(required=True),
        delimiter='|',
        required=True,
        validators=[keyword_validator],
        label='#2 Keyword List (Use "|" as delimiter)'
    )
    keywords_3 = SimpleArrayField(
        forms.CharField(required=True),
        delimiter='|',
        required=False,
        validators=[keyword_validator],
        label='#3 Keyword List (Use "|" as delimiter)'
    )
    keywords_4 = SimpleArrayField(
        forms.CharField(required=True),
        delimiter='|',
        required=False,
        validators=[keyword_validator],
        label='#4 Keyword List (Use "|" as delimiter)'
    )

    answer = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = DataFile
        fields = [
            'mnemonic',
        ]
