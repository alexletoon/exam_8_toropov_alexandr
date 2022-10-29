from django.urls import path
from review_app.views.base import IndexView, DisplayProductView, AddProductView, DeleteProductView, EditProductView
from review_app.views.review import AddReviewView, UpdateReviewView, DeleteReviewView


urlpatterns = [
    path("", IndexView.as_view(), name='index_view'),
    path("product/<int:pk>", DisplayProductView.as_view(), name='display_product'),
    path('product/create', AddProductView.as_view(), name='add_product'),
    path('product/<int:pk>/delete', DeleteProductView.as_view(), name='delete_product'),
    path('product/edit/<int:pk>', EditProductView.as_view(), name='edit_product'),
    path('product/<int:pk>/add_review',AddReviewView.as_view(), name='add_review'),
    path('product/<int:pk>/update_review',UpdateReviewView.as_view(), name='update_review' ),
    path('product/<int:pk>/delete_review',DeleteReviewView.as_view(), name='delete_review' )
]