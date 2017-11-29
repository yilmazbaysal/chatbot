import os
from django.conf import settings
from django.http import JsonResponse

from dataset.models import DATA_SET_MEDIA_PATH
from .forms import QuestionForm
from django.views.generic.edit import FormView
from rivescript import RiveScript


BOT_INSTANCE = None


# Displays the main template of the project
class QuestionView(FormView):
    template_name = 'question_answer/index.html'
    form_class = QuestionForm

    success_url = '/'


# Gets answer from the ajax request and returns an answer to it
def get_answer(request):
    # Get the question
    question = request.POST.get('question')

    # Get answer from the bot
    reply = BOT_INSTANCE.reply("localuser", question)

    # Create context which will be sent to the front end
    data = {
        'answer': '{}'.format(reply)
    }

    return JsonResponse(data)


# This function creates new bot instance and loads the latest version of the dataset
def reload_dataset():
    global BOT_INSTANCE

    # Data set path
    data_set_directory = os.path.join(settings.MEDIA_ROOT, DATA_SET_MEDIA_PATH)

    # Train the bot
    BOT_INSTANCE = RiveScript()
    BOT_INSTANCE.load_directory(data_set_directory)
    BOT_INSTANCE.sort_replies()
