from django.urls import path
from .views import (
    PassingDetailView,
    RushingDetailView,
    ReceivingDetailView,
    DefenseDetailView,
    index_view,
    player_stats_index_view,
    rb_list_view,
    qb_list_view,
    wr_list_view,
    te_list_view,
    team_stats_index_view,
    team_stats_api_view
)

app_name = 'espn_webscrape'
urlpatterns = [
    path('player_stats/', player_stats_index_view),
    path('player_stats/qb/', qb_list_view, name='qb-list'),
    path('player_stats/rb/', rb_list_view, name='rb-list'),
    path('player_stats/wr/', wr_list_view, name='wr-list'),
    path('player_stats/te/', te_list_view, name='te-list'),
    path('passing/<int:id>/', PassingDetailView.as_view(), name='passing-detail'),
    path('rushing/<int:id>/', RushingDetailView.as_view(), name='rushing-detail'),
    path('receiving/<int:id>/', ReceivingDetailView.as_view(), name='receiving-detail'),
    path('defense/<int:id>/', DefenseDetailView.as_view(), name='defense-detail'),
    path('team_stats/<str:team_abrv>', team_stats_index_view),
    path('team_stats/<str:team_abrv>/<str:category>/<str:stat>', team_stats_api_view, name='team_stats_api'),

]