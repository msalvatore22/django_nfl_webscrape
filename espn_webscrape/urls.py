from django.urls import path
from .views import (
    PassingListView,
    PassingDetailView,
    index_view
)

# from .views import passing_list_view

app_name = 'espn_webscrape'
urlpatterns = [
    path('', index_view),
    path('passing/', PassingListView.as_view(), name='passing-list'),
    # path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<int:id>/', PassingDetailView.as_view(), name='passing-detail'),
    # path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
    # path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
]