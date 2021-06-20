from django.http import request
from django.shortcuts import redirect, render
from shop.models.Product import Product
from shop.models.Category import Category
from shop.models.ImageProduct import ImageProduct
from shop.forms.comment import CommentForm



def product(request, pk, cat_id):
    products = Product.objects.get(pk=pk, is_activate=True)
    images = ImageProduct.objects.filter(product=pk,)
    category = Category.objects.filter(is_activate=True)
    title = category.get(name=products.category)
    recomment = Product.objects.filter(is_activate=True).filter(
        is_recomment=True).order_by('price')
    # comment
    form_comment = CommentForm()
    # Submit Comment
    if request.method == "POST":
        form_comment = CommentForm(request.POST)

        # Check validation
        if form_comment.is_valid():
            comment = form_comment.save(commit=False)

            # Save comment
            if request.user.is_authenticated:
                print(request.user.username)
                comment.user = request.user

            comment.product = products
            comment.save()

        # Reset CommentForm
            form_comment = CommentForm()
    context = {

        'products': products,
        'category': category,
        'images': images,
        'title': title,
        'list_product': recomment,
        'form_comment': form_comment,
    }

    return render(request, 'page/product.html', context)
