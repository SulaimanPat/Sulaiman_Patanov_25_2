"""OnlineStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from posts.views import hello_view, now_date, goodby, youtube_view, main_page_view, products_view, post_detail_view
from django.conf.urls.static import static
from OnlineStore import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page_view),
    path('hello/', hello_view),
    path('now_date/', now_date),
    path('goodby/', goodby),
    path('youtube/', youtube_view),
    path('products/', products_view),
    path('products/<int:id>/', post_detail_view)

]
urlpatterns+=static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)