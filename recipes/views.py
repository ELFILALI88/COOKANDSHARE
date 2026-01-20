
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Recipe


# 📋 Liste des recettes
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})


# 📄 Détail d’une recette
def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})


# ➕ Ajouter une recette (TA TÂCHE – MEMBRE 2)
@login_required
def add_recipe(request):
    if request.method == "POST":
        Recipe.objects.create(
            title=request.POST['title'],
            ingredients=request.POST['ingredients'],
            instructions=request.POST.get('instructions', ''),
            author=request.user
        )
        return redirect('recipe_list')

    return render(request, 'recipes/recipe_form.html')


# ✏️ Modifier une recette
@login_required
def recipe_edit(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    if recipe.author != request.user:
        return redirect('recipe_list')

    if request.method == 'POST':
        recipe.title = request.POST['title']
        recipe.ingredients = request.POST['ingredients']
        recipe.instructions = request.POST.get('instructions', '')
        recipe.save()
        messages.success(request, "Recette modifiée avec succès")
        return redirect('recipe_detail', id=recipe.id)

    return render(request, 'recipes/recipe_edit.html', {'recipe': recipe})


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

    return render(request, 'recipes/recipe_confirm_delete.html', {'recipe': recipe})


# 🔍 Recherche (TÂCHE MEMBRE 4 — CONSERVÉE)
def search_recipes(request):
    query = request.GET.get('q')
    author_id = request.GET.get('author')

    recipes = Recipe.objects.all()
    authors = User.objects.all()

    if query:
        recipes = recipes.filter(
            Q(title__icontains=query) |
            Q(ingredients__icontains=query)
        )

    if author_id:
        recipes = recipes.filter(author__id=author_id)

    context = {
        'recipes': recipes,
        'authors': authors,
        'query': query,
        'author_id': author_id,
    }
    return render(request, 'recipes/search.html', context)
