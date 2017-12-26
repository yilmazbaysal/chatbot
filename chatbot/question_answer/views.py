import os
import uuid
from threading import Thread

from django.conf import settings
from django.http import JsonResponse

from question_answer.models import Keyword
from .forms import QuestionForm
from django.views.generic.edit import FormView
from rivescript import RiveScript


BOT_INSTANCE = None

KEYWORDS = None


# Displays the main template of the project
class QuestionView(FormView):
    template_name = 'question_answer/index.html'
    form_class = QuestionForm

    success_url = '/'


# Gets answer from the ajax request and returns an answer to it
def get_answer(request):
    # Get the question
    question = request.POST.get('question')

    # Create a unique identifier for the session, if does not have
    if request.session.get('unique_identifier', None) is None:
        request.session['unique_identifier'] = str(uuid.uuid4())

    # Get answer from the bot
    reply = BOT_INSTANCE.reply(request.session['unique_identifier'], question)

    # Create context which will be sent to the front end
    data = {
        'answer': '{}'.format(reply)
    }

    return JsonResponse(data)


# This function creates new bot instance and loads the latest version of the dataset
def reload_dataset(dataset_media_path):
    # Reinitialize the bot at the background
    background_thread = Thread(target=_reloaded_dataset_in_background, args=(dataset_media_path, ))
    background_thread.start()


def _reloaded_dataset_in_background(dataset_media_path):
    global BOT_INSTANCE

    # Data set path
    data_set_directory = os.path.join(settings.MEDIA_ROOT, dataset_media_path)

    # Train the bot
    BOT_INSTANCE = RiveScript(utf8=True)
    BOT_INSTANCE.load_directory(data_set_directory)
    BOT_INSTANCE.sort_replies()


def reload_keywords():
    """
    This function fetches keywords from database and assign them to the global variable
    :return: None
    """
    global KEYWORDS

    KEYWORDS = Keyword.objects.all().values_list('keyword', flat=True)

    print(KEYWORDS)
