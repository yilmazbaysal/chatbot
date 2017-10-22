from django.http import HttpResponse
from django.shortcuts import render
from .forms import QuestionForm
from django.views.generic.edit import FormView


class QuestionView(FormView):
    template_name = 'question_answer/index.html'
    form_class = QuestionForm

    def form_valid(self, form):
        # TODO: Get the question and return an answer
        question = form.cleaned_data['question']

        return super(QuestionView, self).form_valid(form)
