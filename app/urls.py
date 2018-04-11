from django.urls import path
from django.conf.urls import url
from app import views

urlpatterns = [
    path('addBook/', views.book_add),
    path('listBook/', views.book_list),
    url(r'(\w+)/$', views.book_view),
    url(r'(\w+)/addSubject$', views.subject_add_text),
    url(r'(\w+)/addSubjectImg$', views.subject_add_image),
]