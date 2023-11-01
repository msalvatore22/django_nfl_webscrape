# Pro Football Metrics

## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)

## Overview

### The challenge

Scrape NFL data and display metrics and stats to end users. Utilize Celery as a worker process and Celery-Beat to schedule the worker process to scrape and persist NFL data in a PostgreSQL database. The webscraping is done with Beautifulsoup4 and the Requests module. Redis is used as a message queue to communicate to Celery that a scheduled task needs to be executed. Django is used to serve content to the users, and to complete the database modeling and interactions using the integrated ORM.

Chart.js and Bootstrap are used on the front end for charting and responsive design.

The low cost hosting solution for this project is Render.com. Django is deployed as a webservice, Celery and Celery beat are deployed as python workers, and Redis is deployed in message queue mode.

### Links

- Solution URL: [Add solution URL here](https://github.com/msalvatore22/django_nfl_webscrape)
- Live Site URL: [Add live site URL here](https://pro-football-metrics.onrender.com/)

## My process

### Built with

- Django
- PostgreSQL
- Celery
- Celery-Beat
- Redis
- Bootstrap
- Chart.js
- Render.com
- Beautifulsoup4

### What I learned
- Basic design pattern of Django and how to structure the app
- How to configure Django settings for developement and production
- Queries with Django ORM
- Webscraping html with Beautifulsoup4
