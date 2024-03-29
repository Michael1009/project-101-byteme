"""skimatch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500


urlpatterns = [
    path('app/', include('app.urls', namespace='app')),
    path('admin/', admin.site.urls),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='main_page'),
    #path('sign_up/', views.sign_up, name = 'sign_up'),
    path('profile/', views.create_profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    #path('notifications/', views.notifications, name='notifications'),
    #path('settings/', views.settings, name='settings'),
    url(r'^auth/', include('social_django.urls', namespace='social')),  # <- Here
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('search/', views.search, name='search'),
    path('learn_more/', views.learn_more, name='learn_more')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = views.error404
handler500 = views.error500
