
from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('<int:id>/', views.recipe_detail, name='recipe_detail'),
    path('<int:id>/edit/', views.recipe_edit, name='recipe_edit'),
    path('<int:id>/delete/', views.recipe_delete, name='recipe_delete'),
    path('search/', views.search_recipes, name='search_recipes'),
]

