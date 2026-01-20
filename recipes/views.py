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
