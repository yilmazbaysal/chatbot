from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.QuestionView.as_view(), name='index'),
]