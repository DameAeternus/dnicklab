from django.urls import path
from . import views
urlpatterns = [
    path('index/',views.index,name='index'),
    path('books/<int:id>/', views.viewbooks, name='viewbooks'),
    path('books/add', views.add, name='add')
]