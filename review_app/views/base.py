from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from review_app.models import Product, Review
from review_app.forms import ProductForm
from django.db.models import Avg, IntegerField

class IndexView(ListView):
    template_name: str = 'index.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 5
    paginate_orphans: int = 1


class DisplayProductView(DetailView):
    template_name: str = 'display_product.html'
    model = Product


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_review = self.object.product_reviews.all()
        total = product_review.aggregate(Avg('rating', output_field=IntegerField()))
        total = total.get('rating__avg')
        context['total'] = total
        context['reviews'] = product_review
        return context



class AddProductView(CreateView):
    template_name: str = 'add_product.html'
    model = Product
    form_class = ProductForm
    success_url = '/'

class EditProductView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name: str = 'edit_product.html'
    success_url = '/'


class DeleteProductView(DeleteView):
    model = Product
    template_name: str = 'confirm_delete.html'
    success_url = '/'
