from django.http import request
from django.shortcuts import redirect, render
from shop.models.Category import Category
from shop.forms.users.signups import ImageUserForm, SignupForm
from django.views.decorators.csrf import csrf_exempt
from shop.models.ImageUser import ImageUser
from django.shortcuts import get_object_or_404

@csrf_exempt
def about(request):
    
    if request.user.is_authenticated:
        imageview = get_object_or_404(ImageUser,user=request.user)
        imageview =  ImageUser.objects.get(user=request.user)
    print(imageview.images)
    category = Category.objects.filter(is_activate=True)
    form_image = ImageUserForm()
    if request.method == 'POST':
        form_image = ImageUserForm(request.POST ,request.FILES)
        if form_image.is_valid():
           images = form_image.save(commit=False)
           if request.user.is_authenticated:
               images.user = request.user
           images.save()
           img_obj = form_image.instance
           return render(request, 'page/about.html', {'form_image': form_image, 'img_obj': img_obj})
        else:
            form_image = ImageUserForm()
    context = {
        'form_image':form_image,
        'category': category,
        'imageview':imageview,
    }
    return render(request, 'page/about.html', context)
