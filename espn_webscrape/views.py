from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .models import EspnPassingStats, EspnRushingStats, EspnReceivingStats


# Create your views here.
def index_view(request, *args, **kwargs):
   
    my_context = {
    }
    return render(request, "index.html", my_context)

def player_stats_index_view(request, *args, **kwargs):
    qb_yds = EspnPassingStats.objects.filter(pos='QB').order_by('-yds')
    my_context = {
        "obj_list": qb_yds
    }
    return render(request, "player_stats/index.html", my_context)

class QBListView(ListView):
    template_name = 'player_stats/qb_list.html'
    queryset = EspnPassingStats.objects.filter(pos='QB').order_by('-yds')

class RBListView(ListView):
    template_name = 'player_stats/rb_list.html'
    queryset = EspnRushingStats.objects.filter(pos='RB').order_by('-yds')

class WRListView(ListView):
    template_name = 'player_stats/rec_list.html'
    queryset = EspnReceivingStats.objects.filter(pos='WR').order_by('-yds')

class TEListView(ListView):
    template_name = 'player_stats/rec_list.html'
    queryset = EspnReceivingStats.objects.filter(pos='TE').order_by('-yds')

class PassingListView(ListView):
    template_name = 'passing/passing_list.html'
    queryset = EspnRushingStats.objects.all().order_by('-yds') # <blog>/<modelname>_list.html

class PassingDetailView(DetailView):
    template_name = 'passing/passing_detail.html'
    #queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(EspnPassingStats, id=id_)

class RushingListView(ListView):
    template_name = 'rushing/rushing_list.html'
    queryset = EspnRushingStats.objects.all().order_by('-yds') # <blog>/<modelname>_list.html

class RushingDetailView(DetailView):
    template_name = 'rushing/rushing_detail.html'
    #queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(EspnRushingStats, id=id_)