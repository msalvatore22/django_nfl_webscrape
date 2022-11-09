import os
from celery import Celery

from celery.schedules import crontab # scheduler

# default django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_nfl_webscrape.settings')

app = Celery('django_nfl_webscape')

app.conf.timezone = 'UTC'

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    # executes every 1 minute
    'scraping-task-one-min': {
        'task': 'espn_webscrape.tasks.espn_team_player_stats',
        'schedule': crontab(),
    },
    # # executes every 15 minutes
    # 'scraping-task-fifteen-min': {
    #     'task': 'tasks.hackernews_rss',
    #     'schedule': crontab(minute='*/15')
    # },
    # # executes daily at midnight
    # 'scraping-task-midnight-daily': {
    #     'task': 'tasks.hackernews_rss',
    #     'schedule': crontab(minute=0, hour=0)
    # }
}
