import os
import celery

from celery.schedules import crontab # scheduler

# default django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_nfl_webscrape.settings')

app = celery.Celery('django_nfl_webscape')

app.conf.timezone = 'UTC'

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    # executes every 1 minute
    # 'scraping-task-one-min': {
    #     'task': 'espn_webscrape.tasks.espn_team_player_stats',
    #     'schedule': crontab(),
    # },
    # 'scraping-task-one-hour': {
    #     'task': 'espn_webscrape.tasks.espn_team_player_stats',
    #     'schedule': crontab('*/1'),
    # },
    'scraping-task-thirty-min': {
        'task': 'espn_webscrape.tasks.espn_team_player_stats',
        'schedule': crontab(minute='*/30'),
    },
}