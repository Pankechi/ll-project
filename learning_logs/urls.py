#Defines the URLs for learning_logs

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    path('', views.index, name='index'),  # homepage
    path('topics/', views.topics, name='topics'),  # topics list page
    path('topics/<int:topic_id>/', views.topic, name='topic'),  # single topic page
    path('new_topic/', views.new_topic, name='new_topic'),  # page for adding new topics
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'), # page for adding new entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'), # edditing entries
    path('delete_entry/<int:entry_id>/', views.delete_entry, name='delete_entry'), # delete enrtry
]