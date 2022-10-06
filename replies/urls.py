from django.urls import path
from replies.views import get_comments

urlpatterns = [
    path('replies/', get_comments, name='feeds'),

]
