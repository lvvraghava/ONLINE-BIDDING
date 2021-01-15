from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from user_app import views as user_app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_app_views.register, name='register'),
    path('login/', user_app_views.loginPage, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user_app/logout.html'), name='logout'),
    path('', include('Nouserapp.urls')),
    path('prodapp/', include('Producerapp.urls')),
    path('consapp/', include('Consumerapp.urls'))
]