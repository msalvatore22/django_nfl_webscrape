# tasks
from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery import app, shared_task

# scraping
import requests
import pandas as pd
from bs4 import BeautifulSoup
from collections import defaultdict
from espn_webscrape.nfl_team_lists import nfl_teams

# model
from .models import EspnDefenseStats, EspnPassingStats, EspnReceivingStats, EspnRushingStats

# logging
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)

# persisting data
@shared_task
def save_espn_stats(espn_stat_dict):
    print(espn_stat_dict.keys())

    passing_list = espn_stat_dict['Passing']
    receiving_list = espn_stat_dict["Receiving"]
    rushing_list = espn_stat_dict["Rushing"]
    defense_list = espn_stat_dict["Defense"]

    for pass_stat in passing_list:
        try:
            udpated_values = {
                "player_full_name": pass_stat["Player Name"],
                "pos": pass_stat["POS"],
                "team_full": pass_stat["TEAM_FULL"],
                "team_abrv": pass_stat["TEAM"],
                "season": "2022 Regular Season",
                "gp": pass_stat["GP"],
                "cmp": pass_stat["CMP"],
                "att": pass_stat["ATT"],
                "cmp_percent": pass_stat["CMP%"],
                "yds": pass_stat["YDS"],
                "avg": pass_stat["AVG"],
                "yds_g": pass_stat["YDS/G"],
                "lng": pass_stat["LNG"],
                "td": pass_stat["TD"],
                "int": pass_stat["INT"],
                "sack": pass_stat["SACK"],
                "syl": pass_stat["SYL"],
                "rtg": pass_stat["RTG"]
            }
            obj, created = EspnPassingStats.objects.update_or_create(
                player_full_name = pass_stat["Player Name"],
                team_abrv = pass_stat["TEAM"],
                defaults=udpated_values
            )
        except Exception as e:
                print('failed to persist passing stat')
                print(e)
                break
    
    for rec_stat in receiving_list:
        try:
            udpated_values = {
                "player_full_name": rec_stat["Player Name"],
                "pos": rec_stat["POS"],
                "team_full": rec_stat["TEAM_FULL"],
                "team_abrv": rec_stat["TEAM"],
                "season": "2022 Regular Season",
                "gp": rec_stat["GP"],
                "rec": rec_stat["REC"],
                "tgts": rec_stat["TGTS"],
                "yds": rec_stat["YDS"],
                "avg": rec_stat["AVG"],
                "yds_g": rec_stat["YDS/G"],
                "lng": rec_stat["LNG"],
                "td": rec_stat["TD"],
                "big": rec_stat["BIG"],
                "fum": rec_stat["FUM"],
                "lst": rec_stat["LST"],
                "yac": rec_stat["YAC"],
                "fd": rec_stat["FD"]
            }
            obj, created = EspnReceivingStats.objects.update_or_create(
                player_full_name = rec_stat["Player Name"],
                team_abrv = rec_stat["TEAM"],
                defaults=udpated_values
            )
        except Exception as e:
                print('failed to persist passing stat')
                print(e)
                break
    
    for rush_stat in rushing_list:
        try:
            udpated_values = {
                "player_full_name": rush_stat["Player Name"],
                "pos": rush_stat["POS"],
                "team_full": rush_stat["TEAM_FULL"],
                "team_abrv": rush_stat["TEAM"],
                "season": "2022 Regular Season",
                "gp": rush_stat["GP"],
                "att": rush_stat["ATT"],
                "yds": rush_stat["YDS"],
                "avg": rush_stat["AVG"],
                "yds_g": rush_stat["YDS/G"],
                "lng": rush_stat["LNG"],
                "td": rush_stat["TD"],
                "big": rush_stat["BIG"],
                "fum": rush_stat["FUM"],
                "lst": rush_stat["LST"],
                "fd": rush_stat["FD"]
            }
            obj, created = EspnRushingStats.objects.update_or_create(
                player_full_name = rush_stat["Player Name"],
                team_abrv = rush_stat["TEAM"],
                defaults=udpated_values
            )
        except Exception as e:
                print('failed to persist passing stat')
                print(e)
                break
    
    for def_stat in defense_list:
        try:
            udpated_values = {
                "player_full_name": def_stat["Player Name"],
                "pos": def_stat["POS"],
                "team_full": def_stat["TEAM_FULL"],
                "team_abrv": def_stat["TEAM"],
                "season": "2022 Regular Season",
                "gp": def_stat["GP"],
                "solo": def_stat["SOLO"],
                "ast": def_stat["AST"],
                "tot": def_stat["TOT"],
                "sack": def_stat["SACK"],
                "sack_yds": def_stat["SACKYDS"],
                "pd": def_stat["PD"],
                "int": def_stat["INT"],
                "yds": def_stat["YDS"],
                "lng": def_stat["LNG"],
                "td": def_stat["TD"],
                "ff": def_stat["FF"],
                "fr": def_stat["FR"],
                "ftd": def_stat["FTD"],
                "kb": def_stat["KB"]
            }
            obj, created = EspnDefenseStats.objects.update_or_create(
                player_full_name = def_stat["Player Name"],
                team_abrv = def_stat["TEAM"],
                defaults=udpated_values
            )
        except Exception as e:
                print('failed to persist passing stat')
                print(e)
                break

# webscraping
@shared_task
def espn_team_player_stats():
    print(f"ESPN NFL Web Scrape Initiated")
    # print(nfl_teams)
    # store the dataframes in an object where the key is the title of the table
    espn_stat_dict = defaultdict(list)
    try:

        for team in nfl_teams:
            URL = f'https://www.espn.com/nfl/team/stats/_/name/{team[0]}/{team[1]}'
            page = requests.get(URL)
            # print(page)
            soup = BeautifulSoup(page.content, "html.parser")
            # print(soup)
            # find each table on the page
            responsive_tables = soup.find_all("div", class_="ResponsiveTable")
            # loop through each table to get the column headers

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
                    df["TEAM_FULL"] = team[1]

                    df_to_dict = df.to_dict('records')

                    espn_stat_dict[table_title].extend(df_to_dict)
        # print(espn_stat_dict["Passing"][0])
        return save_espn_stats(espn_stat_dict)
    except Exception as e:
        print('The nfl web scrape job failed. See exception:')
        print(e)
