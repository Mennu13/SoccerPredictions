import numpy as np# linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import requests
from bs4 import BeautifulSoup
from pathlib import Path

base_url = 'https://understat.com/league'
leagues = ['La_liga', 'EPL', 'Bundesliga', 'Serie_A', 'Ligue_1', 'RFPL']
seasons = ['2020']


url = base_url+'/'+leagues[0]+'/'+seasons[0]
res = requests.get(url)
soup = BeautifulSoup(res.content, "lxml")

# Based on the structure of the webpage, I found that data is in the JSON variable, under <script> tags
scripts = soup.find_all('script')

import json

string_with_json_obj = ''

# Find data for teams
for el in scripts:
    if 'teamsData' in el.text:
      string_with_json_obj = el.text.strip()
      
# print(string_with_json_obj)

# strip unnecessary symbols and get only JSON data
ind_start = string_with_json_obj.index("('")+2
ind_end = string_with_json_obj.index("')")
json_data = string_with_json_obj[ind_start:ind_end]

json_data = json_data.encode('utf8').decode('unicode_escape')

# convert JSON data into Python dictionary
data = json.loads(json_data)

# Get teams and their relevant ids and put them into separate dictionary
teams = {}
for id in data.keys():
  teams[id] = data[id]['title']

# EDA to get a feeling of how the JSON is structured
# Column names are all the same, so we just use first element
columns = []
# Check the sample of values per each column
values = []
for id in data.keys():
  columns = list(data[id]['history'][0].keys())
  values = list(data[id]['history'][0].values())
  break

sevilla_data = []
for row in data['138']['history']:
  sevilla_data.append(list(row.values()))
  
df = pd.DataFrame(sevilla_data, columns=columns)

# Getting data for all teams
dataframes = {}
for id, team in teams.items():
  teams_data = []
  for row in data[id]['history']:
    teams_data.append(list(row.values()))
    
  df = pd.DataFrame(teams_data, columns=columns)
  dataframes[team] = df

for team, df in dataframes.items():
    dataframes[team]['ppda_coef'] = dataframes[team]['ppda'].apply(lambda x: x['att']/x['def'] if x['def'] != 0 else 0)
    dataframes[team]['ppda_att'] = dataframes[team]['ppda'].apply(lambda x: x['att'])
    dataframes[team]['ppda_def'] = dataframes[team]['ppda'].apply(lambda x: x['def'])
    dataframes[team]['oppda_coef'] = dataframes[team]['ppda_allowed'].apply(lambda x: x['att']/x['def'] if x['def'] != 0 else 0)
    dataframes[team]['oppda_att'] = dataframes[team]['ppda_allowed'].apply(lambda x: x['att'])
    dataframes[team]['oppda_def'] = dataframes[team]['ppda_allowed'].apply(lambda x: x['def'])
    
# And check how our new dataframes look based on Sevilla dataframe
dataframes['Sevilla'].head(2)

frames = []
for team, df in dataframes.items():
    df['team'] = team
    frames.append(df)
    
full_stat = pd.concat(frames)
full_stat = full_stat.drop(['ppda', 'ppda_allowed'], axis=1)

full_stat['xG_diff'] = full_stat['xG'] - full_stat['scored']
full_stat['xGA_diff'] = full_stat['xGA'] - full_stat['missed']
full_stat['xpts_diff'] = full_stat['xpts'] - full_stat['pts']

season_data = dict()
season_data[seasons[0]] = full_stat
full_data = dict()
full_data[leagues[0]] = season_data

full_data = dict()
for league in leagues:
  
  season_data = dict()
  for season in seasons:    
    url = base_url+'/'+league+'/'+season
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "lxml")

# Based on the structure of the webpage, I found that data is in the JSON variable, under <script> tags
    scripts = soup.find_all('script')
    
    string_with_json_obj = ''

    # Find data for teams
    for el in scripts:
        if 'teamsData' in el.text:
          string_with_json_obj = el.text.strip()

 # strip unnecessary symbols and get only JSON data
    ind_start = string_with_json_obj.index("('")+2
    ind_end = string_with_json_obj.index("')")
    json_data = string_with_json_obj[ind_start:ind_end]
    json_data = json_data.encode('utf8').decode('unicode_escape')
    
    
    # convert JSON data into Python dictionary
    data = json.loads(json_data)
    
    # Get teams and their relevant ids and put them into separate dictionary
    teams = {}
    for id in data.keys():
      teams[id] = data[id]['title']
      
    # EDA to get a feeling of how the JSON is structured
    # Column names are all the same, so we just use first element
    columns = []
    # Check the sample of values per each column
    values = []
    for id in data.keys():
      columns = list(data[id]['history'][0].keys())
      values = list(data[id]['history'][0].values())
      break
      
    # Getting data for all teams
    dataframes = {}
    for id, team in teams.items():
      teams_data = []
      for row in data[id]['history']:
        teams_data.append(list(row.values()))

      df = pd.DataFrame(teams_data, columns=columns)
      dataframes[team] = df
      # print('Added data for {}.'.format(team))
      
    
    for team, df in dataframes.items():
        dataframes[team]['ppda_coef'] = dataframes[team]['ppda'].apply(lambda x: x['att']/x['def'] if x['def'] != 0 else 0)
        dataframes[team]['ppda_att'] = dataframes[team]['ppda'].apply(lambda x: x['att'])
        dataframes[team]['ppda_def'] = dataframes[team]['ppda'].apply(lambda x: x['def'])
        dataframes[team]['oppda_coef'] = dataframes[team]['ppda_allowed'].apply(lambda x: x['att']/x['def'] if x['def'] != 0 else 0)
        dataframes[team]['oppda_att'] = dataframes[team]['ppda_allowed'].apply(lambda x: x['att'])
        dataframes[team]['oppda_def'] = dataframes[team]['ppda_allowed'].apply(lambda x: x['def'])
    
    frames = []
    for team, df in dataframes.items():
        df['team'] = team
        frames.append(df)
    
    full_stat = pd.concat(frames)
    full_stat = full_stat.drop(['ppda', 'ppda_allowed'], axis=1)
    
    full_stat['xG_diff'] = full_stat['xG'] - full_stat['scored']
    full_stat['xGA_diff'] = full_stat['xGA'] - full_stat['missed']
    full_stat['xpts_diff'] = full_stat['xpts'] - full_stat['pts']
    
    full_stat.reset_index(inplace=True, drop=True)
    season_data[season] = full_stat
  
  df_season = pd.concat(season_data)
  full_data[league] = df_season
  
data = pd.concat(full_data)

data.index = data.index.droplevel(2)
data.index = data.index.rename(names=['league','year'], level=[0,1])

matches = [ row.loses + row.wins + row.draws for index, row in data.iterrows() ]
data["matches"] = matches

filtered_data = data.groupby(by=["team", "h_a"]).sum()
filtered_data.to_csv("raw_data.csv")
