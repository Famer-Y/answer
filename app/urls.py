from django.urls import path
from django.conf.urls import url
from app import views

urlpatterns = [
    path('createbook/', views.book_create),
    path('booklist/', views.book_list),
    url(r'(\w+)/$', views.book_view)
]