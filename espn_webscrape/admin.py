from django.contrib import admin

# Register your models here.
from .models import EspnPassingStats, EspnRushingStats, EspnReceivingStats, EspnDefenseStats

admin.site.register(EspnPassingStats)
admin.site.register(EspnRushingStats)
admin.site.register(EspnReceivingStats)
admin.site.register(EspnDefenseStats)