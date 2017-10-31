import json
import os
from django.conf import settings
from django.http import JsonResponse

from dataset.models import DATA_SET_MEDIA_PATH
from .forms import QuestionForm
from django.views.generic.edit import FormView
from rivescript import RiveScript


class QuestionView(FormView):
    template_name = 'question_answer/index.html'
    form_class = QuestionForm

    success_url = '/'


def get_answer(request):
    # Get the question
    question = request.POST.get('question')

    # Data set path
    data_set_directory = os.path.join(settings.MEDIA_ROOT, DATA_SET_MEDIA_PATH)

    # Train the bot
    bot = RiveScript()
    bot.load_directory(data_set_directory)
    bot.sort_replies()

    # Get answer from the bot
    reply = bot.reply("localuser", question)

    data = {
        'answer': '{}'.format(reply)
    }

    return JsonResponse(data)
