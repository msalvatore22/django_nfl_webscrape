from django.urls import path
from .views import (
    PassingListView,
    PassingDetailView,
    RushingListView,
    RushingDetailView,
    index_view
)

# from .views import passing_list_view

app_name = 'espn_webscrape'
urlpatterns = [
    path('', index_view),
    path('passing/', PassingListView.as_view(), name='passing-list'),
    
    # path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('passing/<int:id>/', PassingDetailView.as_view(), name='passing-detail'),
    # path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
    # path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
    path('rushing/', RushingListView.as_view(), name='rushing-list'),
    path('rushing/<int:id>/', RushingDetailView.as_view(), name='rushing-detail'),
]