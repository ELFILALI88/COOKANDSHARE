from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # AUTH
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='users/login.html'),
        name='login'
    ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # PASSWORD CHANGE
    path(
        'users/password_change/',
        auth_views.PasswordChangeView.as_view(template_name='users/password_change.html'),
        name='password_change'
    ),
    path(
        'users/password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),
        name='password_change_done'
    ),

    # APPS
    path('', include('recipes.urls')),   # Accueil + recettes
    path('users/', include('users.urls')),
]

# MEDIA (images)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
