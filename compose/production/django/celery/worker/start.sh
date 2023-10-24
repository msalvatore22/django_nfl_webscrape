#!/bin/bash

set -o errexit
set -o nounset

celery -A django_nfl_webscrape worker -l INFO --concurrency 1 -E