from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/', views.detail, name='detail'),
    path('add/', views.add, name='add'),
    path("view/", views.view, name="view"),
]