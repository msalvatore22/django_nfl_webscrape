from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .models import EspnPassingStats, EspnRushingStats

# Create your views here.
def index_view(request, *args, **kwargs):
  my_context = {
  }
  return render(request, "index.html", my_context)

class PassingListView(ListView):
    template_name = 'passing/passing_list.html'
    queryset = EspnPassingStats.objects.all() # <blog>/<modelname>_list.html

class PassingTableView(ListView):
    template_name = 'passing/passing_table.html'
    queryset = EspnPassingStats.objects.filter(pos='QB').order_by('-yds').values() # <blog>/<modelname>_list.html

class PassingDetailView(DetailView):
    template_name = 'passing/passing_detail.html'
    #queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(EspnPassingStats, id=id_)

class RushingListView(ListView):
    template_name = 'rushing/rushing_list.html'
    queryset = EspnRushingStats.objects.all() # <blog>/<modelname>_list.html

class RushingDetailView(DetailView):
    template_name = 'rushing/rushing_detail.html'
    #queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(EspnRushingStats, id=id_)