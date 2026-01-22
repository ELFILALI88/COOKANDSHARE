from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),  # tes URLs de l'app recipes
    # Users
    path('users/', include('users.urls')),

    # Auth
    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html'
    ), name='login'),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    path(
    'password/change/',
    auth_views.PasswordChangeView.as_view(
        template_name='users/password_change.html',
        success_url='/users/profile/'
    ),
    name='password_change'
),

]

# 🔹 Permet à Django de servir les fichiers médias en mode DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



from django.urls import include

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
