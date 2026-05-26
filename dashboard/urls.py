from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('edit/<int:id>/', views.edit_sale, name='edit_sale'),

    path('delete/<int:id>/', views.delete_sale, name='delete_sale'),

]