#To make it clear which urls.py we’re working in, we add a docstring at the beginning of the file
"""Defines URL patterns for learning_logs."""

from django.urls import path
from . import views    #the dot tells Python to import views from the same directory as the current urls.py module

app_name = 'learning_logs'

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),

    # Show all topics.
    path('topics/', views.topics, name='topics'),

    # Detail page for a single topic
    path('topics/(?P<topic_id>\d+)/', views.topic, name='topic'),

]