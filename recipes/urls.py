from django.urls import path
from . import views

urlpatterns = [

    # 📋 Accueil – liste des recettes
    path('', views.recipe_list, name='recipe_list'),

    # 📄 Détail recette
    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),

    # ➕ Ajouter recette
    path('add/', views.add_recipe, name='add_recipe'),

    # ✏️ Modifier recette
    path('edit/<int:id>/', views.recipe_edit, name='recipe_edit'),

    # ❌ Supprimer recette
    path('delete/<int:id>/', views.recipe_delete, name='recipe_delete'),

    # 🔍 Recherche
    path('search/', views.search_recipes, name='search_recipes'),

    # ❤️ Like / Unlike
    path('like/<int:id>/', views.like_recipe, name='like_recipe'),

    # 💬 Ajouter commentaire
    path('comment/<int:id>/', views.add_comment, name='add_comment'),
]
