from django.urls import path
from review_app.views.base import IndexView, DisplayProductView


urlpatterns = [
    path("", IndexView.as_view(), name='index_view'),
    path("product/<int:pk>", DisplayProductView.as_view(), name='display_product')
]