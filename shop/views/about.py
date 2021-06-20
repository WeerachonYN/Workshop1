from django.http import request
from django.shortcuts import redirect, render
from shop.forms.users.signups import ImageUserForm, SignupForm
from django.views.decorators.csrf import csrf_exempt
from shop.models.ImageUser import ImageUser
@csrf_exempt
def about(request):
  
    form_image = ImageUserForm()
    if request.method == 'POST':
        check_img = ImageUser.objects.filter(user=request.user)
        if len(check_img)>0:
            form_image = ImageUserForm(request.POST ,request.FILES,instance=check_img[0])
        else:
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
   
    }
    return render(request, 'page/about.html', context)
