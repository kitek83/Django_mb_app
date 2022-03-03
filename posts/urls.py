# posts/urls.py
from django.urls import path
from .views import HomePageView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns  # for adding the pictures from static file

urlpatterns = [
    path('',HomePageView.as_view(), name='home'),
]

urlpatterns += staticfiles_urlpatterns()     # for adding the pictures from static file