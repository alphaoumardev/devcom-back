from django.urls import path
from topics.views import get_topics

urlpatterns = [
    path('topic/', get_topics, name='topics')
]
