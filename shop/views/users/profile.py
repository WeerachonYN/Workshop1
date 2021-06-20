from django.http import request
from django.shortcuts import redirect, render
from shop.models.Category import Category
from shop.forms.users.signups import ImageUserForm
from django.views.decorators.csrf import csrf_exempt
from shop.models.ImageUser import ImageUser
from shop.forms.users.editprofile import UpdateProfileForm
from django.contrib.auth.models import User


def profileViews(request):
    form_image = ImageUserForm()
    edit_form = UpdateProfileForm()
    if request.method == 'POST':
        edit_form = UpdateProfileForm(request.POST, instance=request.user)

        check_img = ImageUser.objects.filter(user=request.user)
        if len(check_img) > 0:
            form_image = ImageUserForm(
                request.POST, request.FILES, instance=check_img[0])
        else:
            form_image = ImageUserForm(request.POST, request.FILES)

        if form_image.is_valid() and edit_form.is_valid():
            edit_form.save()
            images = form_image.save(commit=False)
            if request.user.is_authenticated:
                images.user = request.user

            images.save()

            img_obj = form_image.instance
            return render(request, 'page/auth/profile.html', {'edit_form': edit_form, 'form_image': form_image, 'img_obj': img_obj})
    instances = User.objects.get(username=request.user)
    edit_form = UpdateProfileForm(instance=instances)
    context = {
        'edit_form': edit_form,
        'form_image': form_image,

    }
    return render(request, 'page/auth/profile.html', context)
