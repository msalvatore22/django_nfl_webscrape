from django.db import models

# Create your models here.
class EspnPassingStats(models.Model):
  class Meta:
    db_table = 'espn_passing_stats'
  player_full_name = models.CharField(max_length=50)
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

class EspnReceivingStats(models.Model):
  class Meta:
    db_table = 'espn_receiving_stats'
  player_full_name = models.CharField(max_length=50)
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

class EspnRushingStats(models.Model):
  class Meta:
    db_table = 'espn_rushing_stats'
  player_full_name = models.CharField(max_length=50)
  team_full = models.CharField(max_length=30)
  team_abrv = models.CharField(max_length=3)
  season = models.CharField(max_length=25)
  gp = models.SmallIntegerField()
  att = models.SmallIntegerField()
  yds = models.SmallIntegerField()
  avg = models.DecimalField(max_digits=5, decimal_places=2)
  lng = models.SmallIntegerField()
  big = models.SmallIntegerField()
  td = models.SmallIntegerField()
  yds_g = models.DecimalField(max_digits=5, decimal_places=2)
  fum = models.SmallIntegerField()
  lst = models.SmallIntegerField()
  fd = models.SmallIntegerField()
  
class EspnDefenseStats(models.Model):
  class Meta:
    db_table = 'espn_defense_stats'
  player_full_name = models.CharField(max_length=50)
  team_full = models.CharField(max_length=30)
  team_abrv = models.CharField(max_length=3)
  season = models.CharField(max_length=25)
  gp = models.SmallIntegerField()
  solo = models.SmallIntegerField()
  ast = models.SmallIntegerField()
  tot = models.SmallIntegerField()
  sack = models.DecimalField(max_digits=4, decimal_places=2)
  sack_yds = models.SmallIntegerField()
  pd = models.SmallIntegerField()
  int = models.DecimalField(max_digits=4, decimal_places=2)
  yds = models.SmallIntegerField()
  lng = models.SmallIntegerField()
  td = models.SmallIntegerField()
  ff = models.SmallIntegerField()
  fr = models.SmallIntegerField()
  ftd = models.SmallIntegerField()
  kb = models.SmallIntegerField()

