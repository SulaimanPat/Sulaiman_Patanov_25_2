from django.shortcuts import render, redirect
from posts.models import Product, Review
from posts.forms import ProductCreateForm, ReviewCreateForm
from posts.constants import PAGINATION_LIMIT
from django.views.generic import ListView, CreateView, DeleteView, DetailView
# Create your views here.


class MainPageSBV(ListView):
    model = Product
    template_name = "layouts/index.html"

class ProductsSBV(ListView):
    model = Product
    template_name = "products/products.html"

    def get(self, request, *args, **kwargs):
        products = self.get_queryset().order_by("-rate")
        search = request.GET.get("search")
        page = int(request.GET.get('page', 1))
        if search:
            products = products.filter(title__contains=search) or products.filter(description__contains=search)
        max_page = products.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        products = products[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]

        context = {
            'products': [
                {
                    'id': product.id,
                    'title': product.title,
                    'rate': product.rate,
                    'image': product.image,
                    'hashtags': product.hashtags.all()
                }
                for product in products
            ],
            'user': request.user,
            'pages': range(1, max_page + 1)
        }

        return render(request, self.template_name, context=context)

class ProductDetailSBV(ListView, DetailView):
    model = Product
    template_name = 'Products/detail.html'
    form_class = ReviewCreateForm
    def get(self, request, **kwargs):
        product = Product.objects.get_queryset()

        context = {
            'product': product,
            'reviews': product.reviews.all(),
            'form': ReviewCreateForm
        }

        return render(request, self.template_name, context=context)

    def post(self, request, **kwargs):
        data = request.POST
        form = ReviewCreateForm(data=data)
        product = Product.objects.get(id=id)

        if form.is_valid():
            Review.objects.create(
                text=form.cleaned_data.get("text"),
                product=product
            )

        context = {
            'product': product,
            'review': product.reviews.all(),
            'form': form
        }
        return render(request, self.template_name, context=context)
class CreateProductSBV(ListView, CreateView):
    model = Product
    template_name = 'products/create.html'
    form_class = ProductCreateForm

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'form': self.form_class if not kwargs.get('form') else kwargs['form']
        }

    def get(self, request, **kwargs):
        return render(request, self.template_name, context=self.get_context_data())

    def post(self, request, **kwargs):
        data, files = request.POST, request.FILES

        form = self.form_class(data, files)
        if form.is_valid():
            Product.objects.create(
                image=form.cleaned_data.get("image"),
                title=form.cleaned_data.get("title"),
                description=form.cleaned_data.get("description"),
                rate=form.cleaned_data.get("rate")
            )
            return redirect("/products")
        return render(request, self.template_name, context={
            'form': form
        })