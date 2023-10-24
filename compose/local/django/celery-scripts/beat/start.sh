#!/bin/bash

set -o errexit
set -o nounset

rm -f './celerybeat.pid'
celery -A django_nfl_webscrape beat -l INFO