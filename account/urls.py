from django.urls import path
from account import views

urlpatterns = [
   path("", views.index, name = 'index'),
   path("all_products", views.all_products, name = 'all_products'),
   path("contact", views.contact, name = 'contact'),
   path("change_password", views.change_password, name = 'change_password'),
   path("favorites", views.favorites, name = 'favorites'),
   path("filtered_items", views.filtered_items, name = 'filtered_items'),
   path("fragrances", views.fragrances, name = 'fragrances'),
   path("login", views.loginUser, name = 'login'),
   path("logout", views.logoutUser, name = 'logout'),
   path("newarrivals",views.newarrival, name = 'newarrival'),
   path("preferences", views.preferences, name = 'preferences'),
   path("profile", views.profile, name = 'profile'),
   path("register", views.registerUser, name = 'register'),
   path("sales", views.sales, name = 'sales'),
   path("search", views.search, name = 'search'),
   path("settings", views.settings, name = 'settings'),
   
   
   
   
   
  
  
   
   
   
  
]
