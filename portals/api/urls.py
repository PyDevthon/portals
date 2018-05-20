from django.urls import path, re_path
from portals.api import views


urlpatterns = [
    path('Discussions', views.DiscussionsListView.as_view(), name='Discussions_List'),
    path('Discussions/<str:category>', views.DiscussionsListView.as_view(), name='Particular_Cat'),
    path('Discussions/<int:pk>/', views.DiscussionsItemsView.as_view(), name='Particular_item'),
    path('Replies', views.RepliesListView.as_view(), name='Replies_List'),
    path('Replies/<int:replied_to_id>', views.RepliesToView.as_view(), name='Replied_to'),
]
