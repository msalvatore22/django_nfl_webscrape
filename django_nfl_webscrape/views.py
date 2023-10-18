
from django.shortcuts import render
from django.views import generic

from espn_webscrape.models import ( 
  EspnPassingStats, 
  EspnReceivingStats, 
  EspnRushingStats, 
  EspnDefenseStats
)

# Create your views here.


def home_view(request, *args, **kwargs):
  top_10_passing_yds = EspnPassingStats.objects.filter(pos='QB').order_by('-yds')[:10]
  top_10_passing_cmp = EspnPassingStats.objects.filter(pos='QB').order_by('-cmp')[:10]
  top_10_passing_td = EspnPassingStats.objects.filter(pos='QB').order_by('-td')[:10]

  top_10_receiving_yds = EspnReceivingStats.objects.all().order_by('-yds')[:10]
  top_10_receiving_rec = EspnReceivingStats.objects.all().order_by('-rec')[:10]
  top_10_receiving_td = EspnReceivingStats.objects.all().order_by('-td')[:10]

  top_10_rushing_yds = EspnRushingStats.objects.all().order_by('-yds')[:10]
  top_10_rushing_car = EspnRushingStats.objects.all().order_by('-car')[:10]
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
    "top_10_rushing_car": top_10_rushing_car,
    "top_10_rushing_td": top_10_rushing_td,
    "top_10_defense_tot": top_10_defense_tot,
    "top_10_defense_sack":  top_10_defense_sack ,
    "top_10_defense_int": top_10_defense_int,
  }
  return render(request, "home.html", my_context)


