from django import forms


class QuestionForm(forms.Form):
    question = forms.CharField(
        label='',
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-lg',
                'placeholder': 'Enter your question here!',
            }
        )
    )