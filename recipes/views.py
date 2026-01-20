<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Recipe


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})


def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})


@login_required
def add_recipe(request):
    if request.method == "POST":
        Recipe.objects.create(
            title=request.POST['title'],
            ingredients=request.POST['ingredients'],
            instructions=request.POST['instructions'],
            author=request.user  # 🔴 TRÈS IMPORTANT
        )
        return redirect('recipe_list')

    return render(request, 'recipes/recipe_form.html')


@login_required
def recipe_edit(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    if recipe.author != request.user:
        return redirect('recipe_list')

    if request.method == 'POST':
        recipe.title = request.POST['title']
        recipe.ingredients = request.POST['ingredients']
        recipe.instructions = request.POST['instructions']
        recipe.save()

        messages.success(request, "Recette modifiée avec succès")
        return redirect('recipe_detail', id=recipe.id)

    return render(request, 'recipes/recipe_edit.html', {'recipe': recipe})


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
=======
from django.shortcuts import render
from .models import Recipe
from django.contrib.auth.models import User
from django.db.models import Q

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
>>>>>>> 51441947e05d0a2ef62c62bfaef66c1a2a6ca0ae
