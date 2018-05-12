from django.urls import path, include, re_path
from portals import views

urlpatterns = [
    re_path(r'^$', views.home, name='home_page'),
    re_path('create/', views.CreateItem.as_view(), name='create')
]
