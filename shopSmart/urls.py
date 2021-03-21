"""shopSmart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf.urls import url,static
from django.urls import path,include
from . import views
from .views import crawl

admin.site.site_header = "ShopSmart - Administrator Dashboard"
admin.site.site_title = "ShopSmart"
admin.site.index_title = "Welcome, Admin!"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),

    path('reset_password/',auth_views.PasswordResetView.as_view(), name = 'reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(), name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name = "password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(), name = 'password_reset_complete'),
    url(r'^api/crawl/', views.crawl, name='crawl'),
]