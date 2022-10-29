from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from review_app.models import Product, Review
from review_app.forms import ProductForm, ReviewForm
from django.shortcuts import get_object_or_404, redirect


class AddReviewView(CreateView):
    template_name: str = 'add_review.html'
    model = Review
    form_class = ReviewForm
    paginate_by = 5
    paginate_orphans: int = 1
    success_url ='/'


    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        form.instance.product = product
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateReviewView(UpdateView):
    template_name: str = 'update_review.html'
    model = Review
    form_class = ReviewForm
    paginate_by = 5
    paginate_orphans: int = 1
    success_url ='/'

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        form.instance.product = product
        form.instance.author = self.request.user
        return super().form_valid(form)

