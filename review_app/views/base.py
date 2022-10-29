from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from review_app.models import Product


class IndexView(ListView):
    template_name: str = 'index.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 5
    paginate_orphans: int = 1


class DisplayProductView(DetailView):
    template_name: str = 'display_product.html'
    model = Product


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
