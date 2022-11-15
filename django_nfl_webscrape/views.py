
from django.shortcuts import render
from django.views import generic

from espn_webscrape.models import EspnPassingStats # bring News into the views

# Create your views here.


def home_view(request, *args, **kwargs):
  my_context = {
  }
  return render(request, "home.html", my_context)


