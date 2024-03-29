import os
from celery import Celery

from celery.schedules import crontab # scheduler

# default django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_nfl_webscrape.settings')
ENVIRONMENT = os.environ.get("ENV")

app = Celery('django_nfl_webscape')

app.conf.timezone = 'UTC'

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


if ENVIRONMENT == 'dev':
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
        # executes every 5 minute
        'scraping-task-five-min': {
            'task': 'espn_webscrape.tasks.espn_team_player_stats',
            'schedule': crontab(minute='*/5'),
        },
        # 'scraping-task-thirty-min': {
        #     'task': 'espn_webscrape.tasks.espn_team_player_stats',
        #     'schedule': crontab(minute='*/30'),
        # },
    }
else:
    app.conf.beat_schedule = {
        'scraping-task-midnight': {
            'task': 'espn_webscrape.tasks.espn_team_player_stats',
            'schedule': crontab(minute=0, hour=4),
        },
    }
