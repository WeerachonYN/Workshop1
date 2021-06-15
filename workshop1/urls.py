"""workshop1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from shop.views.homepage import homepage
from shop.views.category import category
from shop.views.category import categoryFilter
from shop.views.product import product
from shop.views.contact import contact
from shop.views.about import about

urlpatterns = [

    path('admin/', admin.site.urls),
    # page
    path('',homepage,name = 'home'),
    path('category',category,name='category-list'),
    path('category/<int:pk>',categoryFilter,name='category-filter'),
    # path('category',search_category,name='category_search'),
    path('product/<int:cat_id>/<int:pk>',product,name='product'),
    path('contact',contact,name='contact'),
    path('about',about,name='about'),
]   
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
