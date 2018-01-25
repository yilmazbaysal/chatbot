import os
import string
import uuid
import enchant
from threading import Thread

from django.conf import settings
from django.http import JsonResponse

from question_answer.models import Keyword
from .forms import QuestionForm
from django.views.generic.edit import FormView
from rivescript import RiveScript


BOT_INSTANCE = None

KEYWORDS = None

SPELL_CHECKER = enchant.Dict('en_US')


# Displays the main template of the project
class QuestionView(FormView):
    template_name = 'question_answer/index.html'
    form_class = QuestionForm

    success_url = '/'


def spell_checker(question):
    has_typo = False

    # Clean punctuations
    punctuation = set(string.punctuation)
    question = ''.join(ch for ch in question if ch not in punctuation)

    new_question = []
    for token in question.split(' '):
        turkish_chars = ['ğ', 'Ğ', 'ı', 'İ', 'ö', 'Ö', 'ü', 'Ü', 'ş', 'Ş', 'ç', 'Ç']
        if token.lower() not in KEYWORDS and not SPELL_CHECKER.check(token) and turkish_chars not in token:
            # There is a typo in the token and not a special keyword
            has_typo = True

            # Add first suggestion
            new_question.append(SPELL_CHECKER.suggest(token)[0])
        else:
            # Add original token
            new_question.append(token)

    return has_typo, ' '.join(new_question)


# Gets answer from the ajax request and returns an answer to it
def get_answer(request):
    # Get the question
    question = request.POST.get('question')

    # Create a unique identifier for the session, if does not have
    if request.session.get('unique_identifier', None) is None:
        request.session['unique_identifier'] = str(uuid.uuid4())

    # Check the question for typos
    try:
        has_typo, fixed_question = spell_checker(question)
    except:
        has_typo = False

    # Get answer from the bot
    reply = BOT_INSTANCE.reply(request.session['unique_identifier'], question)

    # Create context which will be sent to the front end
    if has_typo:
        # Get reply for the fixed question
        fixed_reply = BOT_INSTANCE.reply(request.session['unique_identifier'], fixed_question)

        data = {
            'answer': '{}'.format(reply),
            'spell_checked_question': 'Did you mean: <i>{}<i>'.format(fixed_question),
            'spell_checked_answer': '{}'.format(fixed_reply)
        }
    else:
        data = {
            'answer': '{}'.format(reply),
            'spell_checked_question': '',
            'spell_checked_answer': ''
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
