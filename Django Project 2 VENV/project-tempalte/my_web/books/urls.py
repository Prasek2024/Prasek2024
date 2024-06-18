from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.BookCreateView.as_view(), name='add_book'),
]