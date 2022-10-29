from django.urls import path
from review_app.views.base import IndexView, DisplayProductView, AddProductView
from review_app.views.review import AddReviewView


urlpatterns = [
    path("", IndexView.as_view(), name='index_view'),
    path("product/<int:pk>", DisplayProductView.as_view(), name='display_product'),
    path('product/create', AddProductView.as_view(), name='add_product'),
    path('product/<int:pk>/add_review',AddReviewView.as_view(), name='add_review' )
]