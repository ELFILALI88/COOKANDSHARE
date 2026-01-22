from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm
from recipes.models import Recipe
from .forms import UserRegisterForm

# --------------------
# INSCRIPTION
# --------------------


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Compte créé avec succès")
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

# --------------------
# PROFIL
# --------------------

@login_required
def profile(request):
    recipes = Recipe.objects.filter(author=request.user)

    return render(request, 'users/profile.html', {
        'recipes': recipes
    })



# --------------------
# MODIFIER PROFIL + PHOTO
# --------------------
@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(
            request.POST,
            instance=request.user
        )
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profil mis à jour avec succès")
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'users/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


# --------------------
# SUPPRIMER COMPTE
# --------------------
@login_required
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        messages.success(request, "Compte supprimé")
        return redirect('login')

    return render(request, 'users/delete_account.html')
