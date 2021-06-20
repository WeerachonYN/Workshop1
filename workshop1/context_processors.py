from django.conf import settings
from shop.models.ImageUser import ImageUser
from shop.models.Category import Category


def template_context(request):
    category = Category.objects.filter(is_activate=True)
    imageview = None
    if request.user.is_authenticated:
        try:
            imageview =  ImageUser.objects.get(user=request.user)
        except:
            pass

    return {

        'base': {
            'category':category,
            'imageview': imageview
        }
    }