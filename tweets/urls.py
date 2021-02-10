# tweets/urls.py
from django.urls import path
# from .views import TweetListView, TweetCreateView
from . import views

urlpatterns = [
    path('tweets/new/', views.tweet_new, name='tweet_new'),
    path('', views.tweet_list, name='home'),

    # path('tweets/new/', TweetCreateView.as_view(), name='tweet_new'),
    # path('', TweetListView.as_view(), name='home'),
]
