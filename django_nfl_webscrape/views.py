
from django.shortcuts import render
from django.views import generic

from espn_webscrape.models import EspnPassingStats # bring News into the views

# Create your views here.


# class HomePageView(generic.ListView):
#     template_name = 'home.html'
#     context_object_name = 'passing_stats'

#     def get_queryset(self):
#         return EspnPassingStats.objects.all()

