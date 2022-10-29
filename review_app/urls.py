from django.urls import path
from views.base import ListView


urlpatterns = [
    path("", ListView.as_view(), name='index')
]