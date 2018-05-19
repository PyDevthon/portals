from django.urls import path, include, re_path
from portals import views

urlpatterns = [
    re_path(r'^$', views.home, name='home_page'),
    re_path('create/', views.CreateItem.as_view(), name='create'),
    path('view/<str:category>', views.DisplayItem.as_view(), name='display'),
    path('discuss/<int:key>', views.DiscussItem.as_view(), name='discuss'),
    path('addreply/<int:key>', views.AddReply.as_view(), name='addreply'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('logout', views.LogOut.as_view(), name='logout'),
    path('vote/<int:item_id>', views.Vote.as_view(), name='vote'),
]
