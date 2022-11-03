import requests
import pandas as pd
from bs4 import BeautifulSoup
from collections import defaultdict
import nfl_team_lists
from celery import Celery
from celery.schedules import crontab
# from models import *

app = Celery('tasks') # defining the app name to be used in our flag

app.conf.timezone = 'UTC'

app.conf.beat_schedule = {
    # executes every 1 minute
    'scraping-task-one-min': {
        'task': 'tasks.espn_team_player_stats',
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

@app.task
def espn_team_player_stats():
    print(f"ESPN NFL Web Scrape Initiated")
    # print(nfl_teams)
    # store the dataframes in an object where the key is the title of the table
    espn_stat_dict = defaultdict(list)
    try:

        for team in nfl_team_lists.nfl_teams:
            URL = f'https://www.espn.com/nfl/team/stats/_/name/{team[0]}/{team[1]}'
            page = requests.get(URL)
            # print(page)
            soup = BeautifulSoup(page.content, "html.parser")
            # print(soup)
            # find each table on the page
            responsive_tables = soup.find_all("div", class_="ResponsiveTable")
            # loop through each table to get the column headers
            #   the player names for the index
            #   values in the table
            for idx, table_element in enumerate(responsive_tables):
                # create a an object for a data frame for each table
                d = {}
                player_list = []
                columns = []
                table_title = table_element.find("div", class_="Table__Title").text
                # print(table_title)
                tables = table_element.find_all("table", class_="Table")
                # goal is to make a dict with player name as key and row values in a list
                  # { 'Kyler Murray QB': [9,3,40...], "Backup QB": [4,5,6...]}
                # then with the column headers we can do pd.DataFrame.from_dict(d, orient='index',columns=column_headers)
                if table_title in ["Passing", "Rushing", "Receiving", "Defense"]:
                    player_table = tables[0].find_all("td", class_="Table__TD")
                    for player in player_table:
                        if 'Stats__TotalRow' not in player['class']:
                            player_text = player.text
                            player_name = player_text[:-3]
                            player_position = player_text[-2:]
                            player_list.append((player_name, player_position))  
                    # grab the stat headers that will be the columns of the data frame
                    stat_table = tables[1]
                    stat_headers = stat_table.find_all("th", class_="stats-cell")

                    # add POS as first column in table
                    columns.append('Player Name')
                    columns.append('POS')

                    for stat in stat_headers:
                        columns.append(stat.text) 
                    # grab the rows of the table and create the player stat dictionary used for the dataframe
                    stat_table_body = stat_table.find("tbody")
                    stat_rows = stat_table_body.find_all("tr", class_="Table__TR", limit=len(player_list))
                    for i,row in enumerate(stat_rows):
                        row_values = row.find_all('td', class_="Table__TD")
                        stat_list = []
                        # make first stat the player position
                        stat_list.append(player_list[i][0])
                        stat_list.append(player_list[i][1]) 
                        # get the stat values
                        for value in row_values:
                          remove_commas = float(value.text.replace(',', ''))
                          stat_list.append(float(remove_commas))

                        # add the stats for each player
                        d[player_list[i][0]] = stat_list

                    # create the data frame
                    df = pd.DataFrame.from_dict(d, orient="index", columns=columns)
                      
                    # add team column
                    df["TEAM"] = team[0].upper()    

                    df_to_dict = df.to_dict('records')

                    espn_stat_dict[table_title].extend(df_to_dict)
        print(espn_stat_dict["Passing"][0])
        return espn_stat_dict
    except Exception as e:
        print('The nfl web scrape job failed. See exception:')
        print(e)
    