from django.db import models
from django.urls import reverse

class TimeStampedModel(models.Model):
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
      abstract = True

# Create your models here.
class EspnPassingStats(TimeStampedModel):
  class Meta:
    db_table = 'espn_passing_stats'
    constraints = [
      models.UniqueConstraint(fields=['player_full_name', 'pos', 'team_abrv'], name='espn_passing_stats unique player constraint')
    ]
  player_full_name = models.CharField(max_length=50)
  pos = models.CharField(max_length=4, null=True)
  team_full = models.CharField(max_length=30)
  team_abrv = models.CharField(max_length=3)
  season = models.CharField(max_length=25)
  gp = models.SmallIntegerField()
  cmp = models.SmallIntegerField()
  att = models.SmallIntegerField()
  cmp_percent = models.DecimalField(max_digits=5, decimal_places=2)
  yds = models.SmallIntegerField()
  avg = models.DecimalField(max_digits=5, decimal_places=2)
  yds_g = models.DecimalField(max_digits=5, decimal_places=2)
  lng = models.SmallIntegerField()
  td = models.SmallIntegerField()
  int = models.SmallIntegerField()
  sack = models.SmallIntegerField()
  syl = models.SmallIntegerField()
  rtg = models.DecimalField(max_digits=5, decimal_places=2)
  def get_absolute_url(self):
    return reverse("espn_webscrape:passing-detail", kwargs={"id": self.id})

class EspnReceivingStats(TimeStampedModel):
  class Meta:
    db_table = 'espn_receiving_stats'
    constraints = [
      models.UniqueConstraint(fields=['player_full_name', 'pos', 'team_abrv'], name='espn_receiving_stats unique player constraint')
    ]
  player_full_name = models.CharField(max_length=50)
  pos = models.CharField(max_length=4, null=True)
  team_full = models.CharField(max_length=30)
  team_abrv = models.CharField(max_length=3)
  season = models.CharField(max_length=25)
  gp = models.SmallIntegerField()
  rec = models.SmallIntegerField()
  tgts = models.SmallIntegerField()
  yds = models.SmallIntegerField()
  avg = models.DecimalField(max_digits=5, decimal_places=2)
  yds_g = models.DecimalField(max_digits=5, decimal_places=2)
  lng = models.SmallIntegerField()
  td = models.SmallIntegerField()
  big = models.SmallIntegerField()
  fum = models.SmallIntegerField()
  lst = models.SmallIntegerField()
  yac = models.SmallIntegerField()
  fd = models.SmallIntegerField()
  def get_absolute_url(self):
    return reverse("espn_webscrape:receiving-detail", kwargs={"id": self.id})

class EspnRushingStats(TimeStampedModel):
  class Meta:
    db_table = 'espn_rushing_stats'
    constraints = [
      models.UniqueConstraint(fields=['player_full_name', 'pos', 'team_abrv'], name='espn_rushing_stats unique player constraint')
    ]
  player_full_name = models.CharField(max_length=50)
  pos = models.CharField(max_length=4, null=True)
  team_full = models.CharField(max_length=30)
  team_abrv = models.CharField(max_length=3)
  season = models.CharField(max_length=25)
  gp = models.SmallIntegerField()
  car = models.SmallIntegerField()
  yds = models.SmallIntegerField()
  avg = models.DecimalField(max_digits=5, decimal_places=2)
  lng = models.SmallIntegerField()
  big = models.SmallIntegerField()
  td = models.SmallIntegerField()
  yds_g = models.DecimalField(max_digits=5, decimal_places=2)
  fum = models.SmallIntegerField()
  lst = models.SmallIntegerField()
  fd = models.SmallIntegerField()
  def get_absolute_url(self):
    return reverse("espn_webscrape:rushing-detail", kwargs={"id": self.id})
  
class EspnDefenseStats(TimeStampedModel):
  class Meta:
    db_table = 'espn_defense_stats'
    constraints = [
      models.UniqueConstraint(fields=['player_full_name', 'pos', 'team_abrv'], name='espn_defense_stats unique player constraint')
    ]
  player_full_name = models.CharField(max_length=50)
  pos = models.CharField(max_length=4, null=True)
  team_full = models.CharField(max_length=30)
  team_abrv = models.CharField(max_length=3)
  season = models.CharField(max_length=25)
  gp = models.SmallIntegerField()
  solo = models.SmallIntegerField()
  ast = models.SmallIntegerField()
  tot = models.SmallIntegerField()
  sack = models.DecimalField(max_digits=4, decimal_places=1)
  sack_yds = models.SmallIntegerField()
  pd = models.SmallIntegerField()
  int = models.SmallIntegerField()
  yds = models.SmallIntegerField()
  lng = models.SmallIntegerField()
  td = models.SmallIntegerField()
  ff = models.SmallIntegerField()
  fr = models.SmallIntegerField()
  ftd = models.SmallIntegerField()
  kb = models.SmallIntegerField()
  def get_absolute_url(self):
    return reverse("espn_webscrape:defense-detail", kwargs={"id": self.id})

