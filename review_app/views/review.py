from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from review_app.models import Product, Review
from review_app.forms import ProductForm, ReviewForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


class AddReviewView(LoginRequiredMixin, CreateView):
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
    


class UpdateReviewView(UserPassesTestMixin, UpdateView):
    template_name: str = 'update_review.html'
    model = Review
    form_class = ReviewForm
    success_url ='/'


    def test_func(self):
        return self.request.user.is_superuser or self.get_object().author == self.request.user or self.request.user.has_perm('review_app.change_product')

class DeleteReviewView(UserPassesTestMixin, DeleteView):
    template_name: str = 'confirm_review_delete.html'
    model = Review
    success_url ='/'


    def test_func(self):
        return self.request.user.is_superuser or self.get_object().author == self.request.user or self.request.user.has_perm('review_app.delete_product')
