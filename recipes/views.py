from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Recipe, Comment, Like

# 📋 Liste des recettes (ACCUEIL)
@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()  # kol les recettes ybanou
    return render(request, 'recipes/recipe_list.html', {
        'recipes': recipes
    })

# 📄 Détail d’une recette
def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    instructions_list = recipe.instructions.splitlines()

    return render(request, 'recipes/recipe_detail.html', {
        'recipe': recipe,
        'instructions_list': instructions_list
    })

# ➕ Ajouter une recette
@login_required
def add_recipe(request):
    if request.method == "POST":
        recipe = Recipe(
            title=request.POST.get('title'),
            ingredients=request.POST.get('ingredients'),
            instructions=request.POST.get('instructions', ''),
            author=request.user
        )

        if 'image' in request.FILES:
            recipe.image = request.FILES['image']

        recipe.save()
        messages.success(request, "Recette ajoutée avec succès")
        return redirect('recipe_detail', id=recipe.id)

    return render(request, 'recipes/recipe_form.html')

# ✏️ Modifier une recette
@login_required
def recipe_edit(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    if recipe.author != request.user:
        messages.error(request, "Vous n'êtes pas autorisé(e).")
        return redirect('recipe_list')

    if request.method == 'POST':
        recipe.title = request.POST.get('title')
        recipe.ingredients = request.POST.get('ingredients')
        recipe.instructions = request.POST.get('instructions', '')

        if 'image' in request.FILES:
            recipe.image = request.FILES['image']

        recipe.save()
        messages.success(request, "Recette modifiée avec succès")
        return redirect('recipe_detail', id=recipe.id)

    return render(request, 'recipes/recipe_edit.html', {
        'recipe': recipe
    })

# ❌ Supprimer une recette
@login_required
def recipe_delete(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    if recipe.author != request.user:
        return redirect('recipe_list')

    if request.method == 'POST':
        recipe.delete()
        messages.success(request, "Recette supprimée avec succès")
        return redirect('recipe_list')

    return render(request, 'recipes/recipe_confirm_delete.html', {
        'recipe': recipe
    })

# 🔍 Recherche — page vide par défaut, résultats seulement si luser recherche
@login_required
def search_recipes(request):
    query = request.GET.get('q')  # mot clé recherche
    recipes = []  # khawya par défaut

    if query:  # ghi ila drt chi recherche
        recipes = Recipe.objects.filter(
            Q(title__icontains=query) |
            Q(ingredients__icontains=query)
        )

    return render(request, 'recipes/search.html', {
        'recipes': recipes,
        'query': query
    })

# ❤️ LIKE / UNLIKE
@login_required
def like_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    like, created = Like.objects.get_or_create(
        recipe=recipe,
        user=request.user
    )

    if not created:
        like.delete()

    return HttpResponseRedirect(reverse('recipe_detail', args=[id]))

# 💬 Ajouter un commentaire
@login_required
def add_comment(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    if request.method == "POST":
        content = request.POST.get('content')
        if content:
            Comment.objects.create(
                recipe=recipe,
                user=request.user,
                content=content
            )

    return redirect('recipe_detail', id=id)
