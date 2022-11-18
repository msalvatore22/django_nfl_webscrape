from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .models import EspnPassingStats, EspnRushingStats, EspnReceivingStats, EspnDefenseStats


# Create your views here.
def index_view(request, *args, **kwargs):
   
    my_context = {
    }
    return render(request, "index.html", my_context)

def player_stats_index_view(request, *args, **kwargs):
    top_10_passing_yds = EspnPassingStats.objects.filter(pos='QB').order_by('-yds')[:10]
    top_10_passing_cmp = EspnPassingStats.objects.filter(pos='QB').order_by('-cmp')[:10]
    top_10_passing_td = EspnPassingStats.objects.filter(pos='QB').order_by('-td')[:10]
    top_10_receiving_yds = EspnReceivingStats.objects.all().order_by('-yds')[:10]
    top_10_receiving_rec = EspnReceivingStats.objects.all().order_by('-rec')[:10]
    top_10_receiving_td = EspnReceivingStats.objects.all().order_by('-td')[:10]
    top_10_rushing_yds = EspnRushingStats.objects.all().order_by('-yds')[:10]
    top_10_rushing_att = EspnRushingStats.objects.all().order_by('-att')[:10]
    top_10_rushing_td = EspnRushingStats.objects.all().order_by('-td')[:10]
    top_10_defense_tot = EspnDefenseStats.objects.all().order_by('-tot')[:10]
    top_10_defense_sack = EspnDefenseStats.objects.all().order_by('-sack')[:10]
    top_10_defense_int = EspnDefenseStats.objects.all().order_by('-int')[:10]
    
    my_context = {
    "top_10_passing_yds": top_10_passing_yds,
    "top_10_passing_cmp": top_10_passing_cmp,
    "top_10_passing_td": top_10_passing_td,
    "top_10_receiving_yds": top_10_receiving_yds,
    "top_10_receiving_rec": top_10_receiving_rec,
    "top_10_receiving_td":  top_10_receiving_td ,
    "top_10_rushing_yds": top_10_rushing_yds,
    "top_10_rushing_att": top_10_rushing_att,
    "top_10_rushing_td": top_10_rushing_td,
    "top_10_defense_tot": top_10_defense_tot,
    "top_10_defense_sack":  top_10_defense_sack ,
    "top_10_defense_int": top_10_defense_int,
    }

    return render(request, "player_stats/index.html", my_context)

def qb_list_view(request, *args, **kwargs):
    query = request.GET.get('sort')
    valid = ['cmp','att','cmp_percent','yds','yds_g','td','int','rtg']
    if query is None or query not in valid:
        query = 'yds'
    sorted_list = EspnPassingStats.objects.filter(pos='QB').order_by(f"-{query}")
    my_context ={
        "object_list": sorted_list
    }
    return render(request, 'player_stats/qb_list.html', my_context)

def rb_list_view(request, *args, **kwargs):
    query = request.GET.get('sort')
    valid = ['att','yds','yds_g','td','avg']
    if query is None or query not in valid:
        query = 'yds'
    sorted_list = EspnRushingStats.objects.filter(pos='RB').order_by(f"-{query}")
    my_context ={
        "object_list": sorted_list
    }
    return render(request, 'player_stats/rb_list.html', my_context)

def wr_list_view(request, *args, **kwargs):
    query = request.GET.get('sort')
    valid = ['tgts','rec','yds','yds_g','td']
    if query is None or query not in valid:
        query = 'yds'
    sorted_list = EspnReceivingStats.objects.filter(pos='WR').order_by(f"-{query}")
    my_context ={
        "object_list": sorted_list
    }
    return render(request, 'player_stats/rec_list.html', my_context)

def te_list_view(request, *args, **kwargs):
    query = request.GET.get('sort')
    valid = ['tgts','rec','yds','yds_g','td']
    if query is None or query not in valid:
        query = 'yds'
    sorted_list = EspnReceivingStats.objects.filter(pos='TE').order_by(f"-{query}")
    my_context ={
        "object_list": sorted_list
    }
    return render(request, 'player_stats/rec_list.html', my_context)

class PassingDetailView(DetailView):
    template_name = 'passing/passing_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(EspnPassingStats, id=id_)

class RushingDetailView(DetailView):
    template_name = 'rushing/rushing_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(EspnRushingStats, id=id_)

class ReceivingDetailView(DetailView):
    template_name = 'receiving/receiving_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(EspnReceivingStats, id=id_)

class DefenseDetailView(DetailView):
    template_name = 'defense/defense_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(EspnDefenseStats, id=id_)

def team_stats_index_view(request, team_abrv, *args, **kwargs):
    team_abrv = team_abrv.upper()
    passing_list = EspnPassingStats.objects.filter(team_abrv=team_abrv)
    rushing_list = EspnRushingStats.objects.filter(team_abrv=team_abrv)
    receiving_list = EspnReceivingStats.objects.filter(team_abrv=team_abrv)
    print(team_abrv)
    print(len(rushing_list))
    my_context = {
        "passing_list": passing_list,
        "rushing_list": rushing_list,
        "receiving_list": receiving_list
    }
    return render(request, "team_stats/index.html", my_context)