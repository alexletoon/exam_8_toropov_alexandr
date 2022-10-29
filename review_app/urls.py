from django.urls import path
from review_app.views.base import ListView


urlpatterns = [
    path("", ListView.as_view(), name='index')
]