from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from posts.models import Product

# Create your views here.

def hello_view(request):
    if request.method=="GET":
        return HttpResponse("Hello! Its my first project)")

def now_date(request):
    current_datetime=datetime.now()
    if request.method=="GET":
        return HttpResponse(current_datetime)

def goodby(request):
    if request.method=="GET":
        return HttpResponse("Goodby user!")

def youtube_view(request):
    if request.method=="GET":
        return redirect("https://www.youtube.com/")

def main_page_view(request):
    if request.method == "GET":
        return render(request, 'layouts/index.html')

def products_view(request):
    if request.method == "GET":
        products = Product.objects.all()

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
            ]
        }
        return render(request, 'products/products.html', context=context)
def post_detail_view(request, id):
    if request.method == "GET":
        post = Product.objects.get(id=id)

        context = {
            'post': post,
            'comments': post.comments.all()
        }
        return render(request, 'products/detail.html', context=context)