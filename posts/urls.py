from django.urls import path
from posts.views import *

urlpatterns = [
    path('', index),
    path('auth/', authorization)
]