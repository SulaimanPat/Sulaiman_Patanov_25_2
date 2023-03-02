from django.contrib import admin
from posts.models import Product, Hashtag, Review
# Register your models here.

admin.site.register(Product)
admin.site.register(Hashtag)
admin.site.register(Review)