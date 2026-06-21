from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('welcome/', views.welcome, name='welcome'),
    path('memories/', views.memories, name='memories'),
    path('celebration/', views.celebration, name='celebration'),
    path('gallery/', views.gallery, name='gallery'),
    path('final_message/', views.final_message, name='final_message'),
    path('byee/', views.byee, name='byee'),
]