#GFC = Goal fatti in casa/ Home goals scored 
#GSC = Goal subiti in casa / Home goals conceded 
#GFT = Goal fatti in trasferta / Away goals scored 
#GST = Goal subiti in trasferta / Away goals conceded 
#PC = Partite giocate in casa / Home mathces played 
#PT = Partite giocate in trasferta / Away matches played

import pandas as pd
from pathlib import Path
from scipy.stats import poisson
%matplotlib inline
import matplotlib.pyplot as plt

#User Interface
print("Welcome!")
print("----------------------------------------------")
a = input("Insert Home Team: ")
b = input("Insert Away Team: ")
print("----------------------------------------------")

#Csv path
csv_path = Path("/Users/albertomennuti/Jupyter/Betting/raw_data.csv")
df = pd.read_csv(csv_path)
df.set_index(['team', 'h_a'], inplace=True)

# ----------------- Home Team Stats --------------------------
if a=="milan":
    GFCa1 = df.loc["AC Milan", "h"]['xG']
    GSCa1 = df.loc["AC Milan", "h"]["xGA"]
    GFTa1 = df.loc["AC Milan", "a"]['xG']
    GSTa1 = df.loc["AC Milan", "a"]["xGA"]
    PCa1 = df.loc["AC Milan", "h"]["matches"]
    PTa1 = df.loc["AC Milan", "a"]["matches"]
if a=="alaves":
    GFCa1 = df.loc["Alaves", "h"]['xG']
    GSCa1 = df.loc["Alaves", "h"]["xGA"]
    GFTa1 = df.loc["Alaves", "a"]['xG']
    GSTa1 = df.loc["Alaves", "a"]["xGA"]
    PCa1 = df.loc["Alaves", "h"]["matches"]
    PTa1 = df.loc["Alaves", "a"]["matches"]
if a=="angers":
    GFCa1 = df.loc["Angers", "h"]['xG']
    GSCa1 = df.loc["Angers", "h"]["xGA"]
    GFTa1 = df.loc["Angers", "a"]['xG']
    GSTa1 = df.loc["Angers", "a"]["xGA"]
    PCa1 = df.loc["Angers", "h"]["matches"]
    PTa1 = df.loc["Angers", "a"]["matches"]
if a=="arsenal":
    GFCa1 = df.loc["Arsenal", "h"]['xG']
    GSCa1 = df.loc["Arsenal", "h"]["xGA"]
    GFTa1 = df.loc["Arsenal", "a"]['xG']
    GSTa1 = df.loc["Arsenal", "a"]["xGA"]
    PCa1 = df.loc["Arsenal", "h"]["matches"]
    PTa1 = df.loc["Arsenal", "a"]["matches"]
if a=="aston villa":
    GFCa1 = df.loc["Aston Villa", "h"]['xG']
    GSCa1 = df.loc["Aston Villa", "h"]["xGA"]
    GFTa1 = df.loc["Aston Villa", "a"]['xG']
    GSTa1 = df.loc["Aston Villa", "a"]["xGA"]
    PCa1 = df.loc["Aston Villa", "h"]["matches"]
    PTa1 = df.loc["Aston Villa", "a"]["matches"]
if a=="atalanta":
    GFCa1 = df.loc["Atalanta", "h"]['xG']
    GSCa1 = df.loc["Atalanta", "h"]["xGA"]
    GFTa1 = df.loc["Atalanta", "a"]['xG']
    GSTa1 = df.loc["Atalanta", "a"]["xGA"]
    PCa1 = df.loc["Atalanta", "h"]["matches"]
    PTa1 = df.loc["Atalanta", "a"]["matches"]
if a=="athletic":
    GFCa1 = df.loc["Athletic Club", "h"]['xG']
    GSCa1 = df.loc["Athletic Club", "h"]["xGA"]
    GFTa1 = df.loc["Athletic Club", "a"]['xG']
    GSTa1 = df.loc["Athletic Club", "a"]["xGA"]
    PCa1 = df.loc["Athletic Club", "h"]["matches"]
    PTa1 = df.loc["Athletic Club", "a"]["matches"]
if a=="atletico madrid":
    GFCa1 = df.loc["Atletico Madrid", "h"]['xG']
    GSCa1 = df.loc["Atletico Madrid", "h"]["xGA"]
    GFTa1 = df.loc["Atletico Madrid", "a"]['xG']
    GSTa1 = df.loc["Atletico Madrid", "a"]["xGA"]
    PCa1 = df.loc["Atletico Madrid", "h"]["matches"]
    PTa1 = df.loc["Atletico Madrid", "a"]["matches"]
if a=="augsburg":
    GFCa1 = df.loc["Augsburg", "h"]['xG']
    GSCa1 = df.loc["Augsburg", "h"]["xGA"]
    GFTa1 = df.loc["Augsburg", "a"]['xG']
    GSTa1 = df.loc["Augsburg", "a"]["xGA"]
    PCa1 = df.loc["Augsburg", "h"]["matches"]
    PTa1 = df.loc["Augsburg", "a"]["matches"]
if a=="barcelona":
    GFCa1 = df.loc["Barcelona", "h"]['xG']
    GSCa1 = df.loc["Barcelona", "h"]["xGA"]
    GFTa1 = df.loc["Barcelona", "a"]['xG']
    GSTa1 = df.loc["Barcelona", "a"]["xGA"]
    PCa1 = df.loc["Barcelona", "h"]["matches"]
    PTa1 = df.loc["Barcelona", "a"]["matches"]
if a=="bayer leverkusen":
    GFCa1 = df.loc["Bayer Leverkusen", "h"]['xG']
    GSCa1 = df.loc["Bayer Leverkusen", "h"]["xGA"]
    GFTa1 = df.loc["Bayer Leverkusen", "a"]['xG']
    GSTa1 = df.loc["Bayer Leverkusen", "a"]["xGA"]
    PCa1 = df.loc["Bayer Leverkusen", "h"]["matches"]
    PTa1 = df.loc["Bayer Leverkusen", "a"]["matches"]
if a=="bayern munich":
    GFCa1 = df.loc["Bayern Munich", "h"]['xG']
    GSCa1 = df.loc["Bayern Munich", "h"]["xGA"]
    GFTa1 = df.loc["Bayern Munich", "a"]['xG']
    GSTa1 = df.loc["Bayern Munich", "a"]["xGA"]
    PCa1 = df.loc["Bayern Munich", "h"]["matches"]
    PTa1 = df.loc["Bayern Munich", "a"]["matches"]
if a=="benevento":
    GFCa1 = df.loc["Benevento", "h"]['xG']
    GSCa1 = df.loc["Benevento", "h"]["xGA"]
    GFTa1 = df.loc["Benevento", "a"]['xG']
    GSTa1 = df.loc["Benevento", "a"]["xGA"]
    PCa1 = df.loc["Benevento", "h"]["matches"]
    PTa1 = df.loc["Benevento", "a"]["matches"]
if a=="bologna":
    GFCa1 = df.loc["Bologna", "h"]['xG']
    GSCa1 = df.loc["Bologna", "h"]["xGA"]
    GFTa1 = df.loc["Bologna", "a"]['xG']
    GSTa1 = df.loc["Bologna", "a"]["xGA"]
    PCa1 = df.loc["Bologna", "h"]["matches"]
    PTa1 = df.loc["Bologna", "a"]["matches"]
if a=="bordeaux":
    GFCa1 = df.loc["Bordeaux", "h"]['xG']
    GSCa1 = df.loc["Bordeaux", "h"]["xGA"]
    GFTa1 = df.loc["Bordeaux", "a"]['xG']
    GSTa1 = df.loc["Bordeaux", "a"]["xGA"]
    PCa1 = df.loc["Bordeaux", "h"]["matches"]
    PTa1 = df.loc["Bordeaux", "a"]["matches"]
if a=="borussia dortmund":
    GFCa1 = df.loc["Borussia Dortmund", "h"]['xG']
    GSCa1 = df.loc["Borussia Dortmund", "h"]["xGA"]
    GFTa1 = df.loc["Borussia Dortmund", "a"]['xG']
    GSTa1 = df.loc["Borussia Dortmund", "a"]["xGA"]
    PCa1 = df.loc["Borussia Dortmund", "h"]["matches"]
    PTa1 = df.loc["Borussia Dortmund", "a"]["matches"]
if a=="borussia mgladbach":
    GFCa1 = df.loc["Borussia M.Gladbach", "h"]['xG']
    GSCa1 = df.loc["Borussia M.Gladbach", "h"]["xGA"]
    GFTa1 = df.loc["Borussia M.Gladbach", "a"]['xG']
    GSTa1 = df.loc["Borussia M.Gladbach", "a"]["xGA"]
    PCa1 = df.loc["Borussia M.Gladbach", "h"]["matches"]
    PTa1 = df.loc["Borussia M.Gladbach", "a"]["matches"]
if a=="brest":
    GFCa1 = df.loc["Brest", "h"]['xG']
    GSCa1 = df.loc["Brest", "h"]["xGA"]
    GFTa1 = df.loc["Brest", "a"]['xG']
    GSTa1 = df.loc["Brest", "a"]["xGA"]
    PCa1 = df.loc["Brest", "h"]["matches"]
    PTa1 = df.loc["Brest", "a"]["matches"]
if a=="brighton":
    GFCa1 = df.loc["Brighton", "h"]['xG']
    GSCa1 = df.loc["Brighton", "h"]["xGA"]
    GFTa1 = df.loc["Brighton", "a"]['xG']
    GSTa1 = df.loc["Brighton", "a"]["xGA"]
    PCa1 = df.loc["Brighton", "h"]["matches"]
    PTa1 = df.loc["Brighton", "a"]["matches"]
if a=="burnley":
    GFCa1 = df.loc["Burnley", "h"]['xG']
    GSCa1 = df.loc["Burnley", "h"]["xGA"]
    GFTa1 = df.loc["Burnley", "a"]['xG']
    GSTa1 = df.loc["Burnley", "a"]["xGA"]
    PCa1 = df.loc["Burnley", "h"]["matches"]
    PTa1 = df.loc["Burnley", "a"]["matches"]
if a=="cadiz":
    GFCa1 = df.loc["Cadiz", "h"]['xG']
    GSCa1 = df.loc["Cadiz", "h"]["xGA"]
    GFTa1 = df.loc["Cadiz", "a"]['xG']
    GSTa1 = df.loc["Cadiz", "a"]["xGA"]
    PCa1 = df.loc["Cadiz", "h"]["matches"]
    PTa1 = df.loc["Cadiz", "a"]["matches"]
if a=="cagliari":
    GFCa1 = df.loc["Cagliari", "h"]['xG']
    GSCa1 = df.loc["Cagliari", "h"]["xGA"]
    GFTa1 = df.loc["Cagliari", "a"]['xG']
    GSTa1 = df.loc["Cagliari", "a"]["xGA"]
    PCa1 = df.loc["Cagliari", "h"]["matches"]
    PTa1 = df.loc["Cagliari", "a"]["matches"]
if a=="celta vigo":
    GFCa1 = df.loc["Celta Vigo", "h"]['xG']
    GSCa1 = df.loc["Celta Vigo", "h"]["xGA"]
    GFTa1 = df.loc["Celta Vigo", "a"]['xG']
    GSTa1 = df.loc["Celta Vigo", "a"]["xGA"]
    PCa1 = df.loc["Celta Vigo", "h"]["matches"]
    PTa1 = df.loc["Celta Vigo", "a"]["matches"]
if a=="chelsea":
    GFCa1 = df.loc["Chelsea", "h"]['xG']
    GSCa1 = df.loc["Chelsea", "h"]["xGA"]
    GFTa1 = df.loc["Chelsea", "a"]['xG']
    GSTa1 = df.loc["Chelsea", "a"]["xGA"]
    PCa1 = df.loc["Chelsea", "h"]["matches"]
    PTa1 = df.loc["Chelsea", "a"]["matches"]
if a=="crotone":
    GFCa1 = df.loc["Crotone", "h"]['xG']
    GSCa1 = df.loc["Crotone", "h"]["xGA"]
    GFTa1 = df.loc["Crotone", "a"]['xG']
    GSTa1 = df.loc["Crotone", "a"]["xGA"]
    PCa1 = df.loc["Crotone", "h"]["matches"]
    PTa1 = df.loc["Crotone", "a"]["matches"]
if a=="crystal palace":
    GFCa1 = df.loc["Crystal Palace", "h"]['xG']
    GSCa1 = df.loc["Crystal Palace", "h"]["xGA"]
    GFTa1 = df.loc["Crystal Palace", "a"]['xG']
    GSTa1 = df.loc["Crystal Palace", "a"]["xGA"]
    PCa1 = df.loc["Crystal Palace", "h"]["matches"]
    PTa1 = df.loc["Crystal Palace", "a"]["matches"]
if a=="dijon":
    GFCa1 = df.loc["Dijon", "h"]['xG']
    GSCa1 = df.loc["Dijon", "h"]["xGA"]
    GFTa1 = df.loc["Dijon", "a"]['xG']
    GSTa1 = df.loc["Dijon", "a"]["xGA"]
    PCa1 = df.loc["Dijon", "h"]["matches"]
    PTa1 = df.loc["Dijon", "a"]["matches"]
if a=="eibar":
    GFCa1 = df.loc["Eibar", "h"]['xG']
    GSCa1 = df.loc["Eibar", "h"]["xGA"]
    GFTa1 = df.loc["Eibar", "a"]['xG']
    GSTa1 = df.loc["Eibar", "a"]["xGA"]
    PCa1 = df.loc["Eibar", "h"]["matches"]
    PTa1 = df.loc["Eibar", "a"]["matches"]
if a=="eintracht frankfurt":
    GFCa1 = df.loc["Eintracht Frankfurt", "h"]['xG']
    GSCa1 = df.loc["Eintracht Frankfurt", "h"]["xGA"]
    GFTa1 = df.loc["Eintracht Frankfurt", "a"]['xG']
    GSTa1 = df.loc["Eintracht Frankfurt", "a"]["xGA"]
    PCa1 = df.loc["Eintracht Frankfurt", "h"]["matches"]
    PTa1 = df.loc["Eintracht Frankfurt", "a"]["matches"]
if a=="elche":
    GFCa1 = df.loc["Elche", "h"]['xG']
    GSCa1 = df.loc["Elche", "h"]["xGA"]
    GFTa1 = df.loc["Elche", "a"]['xG']
    GSTa1 = df.loc["Elche", "a"]["xGA"]
    PCa1 = df.loc["Elche", "h"]["matches"]
    PTa1 = df.loc["Elche", "a"]["matches"]
if a=="everton":
    GFCa1 = df.loc["Everton", "h"]['xG']
    GSCa1 = df.loc["Everton", "h"]["xGA"]
    GFTa1 = df.loc["Everton", "a"]['xG']
    GSTa1 = df.loc["Everton", "a"]["xGA"]
    PCa1 = df.loc["Everton", "h"]["matches"]
    PTa1 = df.loc["Everton", "a"]["matches"]
if a=="cologne":
    GFCa1 = df.loc["FC Cologne", "h"]['xG']
    GSCa1 = df.loc["FC Cologne", "h"]["xGA"]
    GFTa1 = df.loc["FC Cologne", "a"]['xG']
    GSTa1 = df.loc["FC Cologne", "a"]["xGA"]
    PCa1 = df.loc["FC Cologne", "h"]["matches"]
    PTa1 = df.loc["FC Cologne", "a"]["matches"]
if a=="fiorentina":
    GFCa1 = df.loc["Fiorentina", "h"]['xG']
    GSCa1 = df.loc["Fiorentina", "h"]["xGA"]
    GFTa1 = df.loc["Fiorentina", "a"]['xG']
    GSTa1 = df.loc["Fiorentina", "a"]["xGA"]
    PCa1 = df.loc["Fiorentina", "h"]["matches"]
    PTa1 = df.loc["Fiorentina", "a"]["matches"]
if a=="freiburg":
    GFCa1 = df.loc["Freiburg", "h"]['xG']
    GSCa1 = df.loc["Freiburg", "h"]["xGA"]
    GFTa1 = df.loc["Freiburg", "a"]['xG']
    GSTa1 = df.loc["Freiburg", "a"]["xGA"]
    PCa1 = df.loc["Freiburg", "h"]["matches"]
    PTa1 = df.loc["Freiburg", "a"]["matches"]
if a=="fulham":
    GFCa1 = df.loc["Fulham", "h"]['xG']
    GSCa1 = df.loc["Fulham", "h"]["xGA"]
    GFTa1 = df.loc["Fulham", "a"]['xG']
    GSTa1 = df.loc["Fulham", "a"]["xGA"]
    PCa1 = df.loc["Fulham", "h"]["matches"]
    PTa1 = df.loc["Fulham", "a"]["matches"]
if a=="genoa":
    GFCa1 = df.loc["Genoa", "h"]['xG']
    GSCa1 = df.loc["Genoa", "h"]["xGA"]
    GFTa1 = df.loc["Genoa", "a"]['xG']
    GSTa1 = df.loc["Genoa", "a"]["xGA"]
    PCa1 = df.loc["Genoa", "h"]["matches"]
    PTa1 = df.loc["Genoa", "a"]["matches"]
if a=="getafe":
    GFCa1 = df.loc["Getafe", "h"]['xG']
    GSCa1 = df.loc["Getafe", "h"]["xGA"]
    GFTa1 = df.loc["Getafe", "a"]['xG']
    GSTa1 = df.loc["Getafe", "a"]["xGA"]
    PCa1 = df.loc["Getafe", "h"]["matches"]
    PTa1 = df.loc["Getafe", "a"]["matches"]
if a=="granada":
    GFCa1 = df.loc["Granada", "h"]['xG']
    GSCa1 = df.loc["Granada", "h"]["xGA"]
    GFTa1 = df.loc["Granada", "a"]['xG']
    GSTa1 = df.loc["Granada", "a"]["xGA"]
    PCa1 = df.loc["Granada", "h"]["matches"]
    PTa1 = df.loc["Granada", "a"]["matches"]
if a=="hertha berlin;":
    GFCa1 = df.loc["Hertha Berlin", "h"]['xG']
    GSCa1 = df.loc["Hertha Berlin", "h"]["xGA"]
    GFTa1 = df.loc["Hertha Berlin", "a"]['xG']
    GSTa1 = df.loc["Hertha Berlin", "a"]["xGA"]
    PCa1 = df.loc["Hertha Berlin", "h"]["matches"]
    PTa1 = df.loc["Hertha Berlin", "a"]["matches"]
if a=="hoffenheim":
    GFCa1 = df.loc["Hoffenheim", "h"]['xG']
    GSCa1 = df.loc["Hoffenheim", "h"]["xGA"]
    GFTa1 = df.loc["Hoffenheim", "a"]['xG']
    GSTa1 = df.loc["Hoffenheim", "a"]["xGA"]
    PCa1 = df.loc["Hoffenheim", "h"]["matches"]
    PTa1 = df.loc["Hoffenheim", "a"]["matches"]
if a=="inter":
    GFCa1 = df.loc["Inter", "h"]['xG']
    GSCa1 = df.loc["Inter", "h"]["xGA"]
    GFTa1 = df.loc["Inter", "a"]['xG']
    GSTa1 = df.loc["Inter", "a"]["xGA"]
    PCa1 = df.loc["Inter", "h"]["matches"]
    PTa1 = df.loc["Inter", "a"]["matches"]
if a=="juventus":
    GFCa1 = df.loc["Juventus", "h"]['xG']
    GSCa1 = df.loc["Juventus", "h"]["xGA"]
    GFTa1 = df.loc["Juventus", "a"]['xG']
    GSTa1 = df.loc["Juventus", "a"]["xGA"]
    PCa1 = df.loc["Juventus", "h"]["matches"]
    PTa1 = df.loc["Juventus", "a"]["matches"]
if a=="lazio":
    GFCa1 = df.loc["Lazio", "h"]['xG']
    GSCa1 = df.loc["Lazio", "h"]["xGA"]
    GFTa1 = df.loc["Lazio", "a"]['xG']
    GSTa1 = df.loc["Lazio", "a"]["xGA"]
    PCa1 = df.loc["Lazio", "h"]["matches"]
    PTa1 = df.loc["Lazio", "a"]["matches"]
if a=="leeds":
    GFCa1 = df.loc["Leeds", "h"]['xG']
    GSCa1 = df.loc["Leeds", "h"]["xGA"]
    GFTa1 = df.loc["Leeds", "a"]['xG']
    GSTa1 = df.loc["Leeds", "a"]["xGA"]
    PCa1 = df.loc["Leeds", "h"]["matches"]
    PTa1 = df.loc["Leeds", "a"]["matches"]
if a=="leicester":
    GFCa1 = df.loc["Leicester", "h"]['xG']
    GSCa1 = df.loc["Leicester", "h"]["xGA"]
    GFTa1 = df.loc["Leicester", "a"]['xG']
    GSTa1 = df.loc["Leicester", "a"]["xGA"]
    PCa1 = df.loc["Leicester", "h"]["matches"]
    PTa1 = df.loc["Leicester", "a"]["matches"]
if a=="lens":
    GFCa1 = df.loc["Lens", "h"]['xG']
    GSCa1 = df.loc["Lens", "h"]["xGA"]
    GFTa1 = df.loc["Lens", "a"]['xG']
    GSTa1 = df.loc["Lens", "a"]["xGA"]
    PCa1 = df.loc["Lens", "h"]["matches"]
    PTa1 = df.loc["Lens", "a"]["matches"]
if a=="levante":
    GFCa1 = df.loc["Levante", "h"]['xG']
    GSCa1 = df.loc["Levante", "h"]["xGA"]
    GFTa1 = df.loc["Levante", "a"]['xG']
    GSTa1 = df.loc["Levante", "a"]["xGA"]
    PCa1 = df.loc["Levante", "h"]["matches"]
    PTa1 = df.loc["Levante", "a"]["matches"]
if a=="lille":
    GFCa1 = df.loc["Lille", "h"]['xG']
    GSCa1 = df.loc["Lille", "h"]["xGA"]
    GFTa1 = df.loc["Lille", "a"]['xG']
    GSTa1 = df.loc["Lille", "a"]["xGA"]
    PCa1 = df.loc["Lille", "h"]["matches"]
    PTa1 = df.loc["Lille", "a"]["matches"]
if a=="liverpool":
    GFCa1 = df.loc["Liverpool", "h"]['xG']
    GSCa1 = df.loc["Liverpool", "h"]["xGA"]
    GFTa1 = df.loc["Liverpool", "a"]['xG']
    GSTa1 = df.loc["Liverpool", "a"]["xGA"]
    PCa1 = df.loc["Liverpool", "h"]["matches"]
    PTa1 = df.loc["Liverpool", "a"]["matches"]
if a=="lorient":
    GFCa1 = df.loc["Lorient", "h"]['xG']
    GSCa1 = df.loc["Lorient", "h"]["xGA"]
    GFTa1 = df.loc["Lorient", "a"]['xG']
    GSTa1 = df.loc["Lorient", "a"]["xGA"]
    PCa1 = df.loc["Lorient", "h"]["matches"]
    PTa1 = df.loc["Lorient", "a"]["matches"]
if a=="lyon":
    GFCa1 = df.loc["Lyon", "h"]['xG']
    GSCa1 = df.loc["Lyon", "h"]["xGA"]
    GFTa1 = df.loc["Lyon", "a"]['xG']
    GSTa1 = df.loc["Lyon", "a"]["xGA"]
    PCa1 = df.loc["Lyon", "h"]["matches"]
    PTa1 = df.loc["Lyon", "a"]["matches"]
if a=="mainz":
    GFCa1 = df.loc["Mainz 05", "h"]['xG']
    GSCa1 = df.loc["Mainz 05", "h"]["xGA"]
    GFTa1 = df.loc["Mainz 05", "a"]['xG']
    GSTa1 = df.loc["Mainz 05", "a"]["xGA"]
    PCa1 = df.loc["Mainz 05", "h"]["matches"]
    PTa1 = df.loc["Mainz 05", "a"]["matches"]
if a=="manchester city":
    GFCa1 = df.loc["Manchester City", "h"]['xG']
    GSCa1 = df.loc["Manchester City", "h"]["xGA"]
    GFTa1 = df.loc["Manchester City", "a"]['xG']
    GSTa1 = df.loc["Manchester City", "a"]["xGA"]
    PCa1 = df.loc["Manchester City", "h"]["matches"]
    PTa1 = df.loc["Manchester City", "a"]["matches"]
if a=="manchester united":
    GFCa1 = df.loc["Manchester United", "h"]['xG']
    GSCa1 = df.loc["Manchester United", "h"]["xGA"]
    GFTa1 = df.loc["Manchester United", "a"]['xG']
    GSTa1 = df.loc["Manchester United", "a"]["xGA"]
    PCa1 = df.loc["Manchester United", "h"]["matches"]
    PTa1 = df.loc["Manchester United", "a"]["matches"]
if a=="marseille":
    GFCa1 = df.loc["Marseille", "h"]['xG']
    GSCa1 = df.loc["Marseille", "h"]["xGA"]
    GFTa1 = df.loc["Marseille", "a"]['xG']
    GSTa1 = df.loc["Marseille", "a"]["xGA"]
    PCa1 = df.loc["Marseille", "h"]["matches"]
    PTa1 = df.loc["Marseille", "a"]["matches"]
if a=="metz":
    GFCa1 = df.loc["Metz", "h"]['xG']
    GSCa1 = df.loc["Metz", "h"]["xGA"]
    GFTa1 = df.loc["Metz", "a"]['xG']
    GSTa1 = df.loc["Metz", "a"]["xGA"]
    PCa1 = df.loc["Metz", "h"]["matches"]
    PTa1 = df.loc["Metz", "a"]["matches"]
if a=="monaco":
    GFCa1 = df.loc["Monaco", "h"]['xG']
    GSCa1 = df.loc["Monaco", "h"]["xGA"]
    GFTa1 = df.loc["Monaco", "a"]['xG']
    GSTa1 = df.loc["Monaco", "a"]["xGA"]
    PCa1 = df.loc["Monaco", "h"]["matches"]
    PTa1 = df.loc["Monaco", "a"]["matches"]
if a=="montpellier":
    GFCa1 = df.loc["Montpellier", "h"]['xG']
    GSCa1 = df.loc["Montpellier", "h"]["xGA"]
    GFTa1 = df.loc["Montpellier", "a"]['xG']
    GSTa1 = df.loc["Montpellier", "a"]["xGA"]
    PCa1 = df.loc["Montpellier", "h"]["matches"]
    PTa1 = df.loc["Montpellier", "a"]["matches"]
if a=="nantes":
    GFCa1 = df.loc["Nantes", "h"]['xG']
    GSCa1 = df.loc["Nantes", "h"]["xGA"]
    GFTa1 = df.loc["Nantes", "a"]['xG']
    GSTa1 = df.loc["Nantes", "a"]["xGA"]
    PCa1 = df.loc["Nantes", "h"]["matches"]
    PTa1 = df.loc["Nantes", "a"]["matches"]
if a=="napoli":
    GFCa1 = df.loc["Napoli", "h"]['xG']
    GSCa1 = df.loc["Napoli", "h"]["xGA"]
    GFTa1 = df.loc["Napoli", "a"]['xG']
    GSTa1 = df.loc["Napoli", "a"]["xGA"]
    PCa1 = df.loc["Napoli", "h"]["matches"]
    PTa1 = df.loc["Napoli", "a"]["matches"]
if a=="newcastle":
    GFCa1 = df.loc["Newcastle United", "h"]['xG']
    GSCa1 = df.loc["Newcastle United", "h"]["xGA"]
    GFTa1 = df.loc["Newcastle United", "a"]['xG']
    GSTa1 = df.loc["Newcastle United", "a"]["xGA"]
    PCa1 = df.loc["Newcastle United", "h"]["matches"]
    PTa1 = df.loc["Newcastle United", "a"]["matches"]
if a=="nice":
    GFCa1 = df.loc["Nice", "h"]['xG']
    GSCa1 = df.loc["Nice", "h"]["xGA"]
    GFTa1 = df.loc["Nice", "a"]['xG']
    GSTa1 = df.loc["Nice", "a"]["xGA"]
    PCa1 = df.loc["Nice", "h"]["matches"]
    PTa1 = df.loc["Nice", "a"]["matches"]
if a=="nimes":
    GFCa1 = df.loc["Nimes", "h"]['xG']
    GSCa1 = df.loc["Nimes", "h"]["xGA"]
    GFTa1 = df.loc["Nimes", "a"]['xG']
    GSTa1 = df.loc["Nimes", "a"]["xGA"]
    PCa1 = df.loc["Nimes", "h"]["matches"]
    PTa1 = df.loc["Nimes", "a"]["matches"]
if a=="osasuna":
    GFCa1 = df.loc["Osasuna", "h"]['xG']
    GSCa1 = df.loc["Osasuna", "h"]["xGA"]
    GFTa1 = df.loc["Osasuna", "a"]['xG']
    GSTa1 = df.loc["Osasuna", "a"]["xGA"]
    PCa1 = df.loc["Osasuna", "h"]["matches"]
    PTa1 = df.loc["Osasuna", "a"]["matches"]
if a=="psg":
    GFCa1 = df.loc["Paris Saint Germain", "h"]['xG']
    GSCa1 = df.loc["Paris Saint Germain", "h"]["xGA"]
    GFTa1 = df.loc["Paris Saint Germain", "a"]['xG']
    GSTa1 = df.loc["Paris Saint Germain", "a"]["xGA"]
    PCa1 = df.loc["Paris Saint Germain", "h"]["matches"]
    PTa1 = df.loc["Paris Saint Germain", "a"]["matches"]
if a=="parma":
    GFCa1 = df.loc["Parma Calcio 1913", "h"]['xG']
    GSCa1 = df.loc["Parma Calcio 1913", "h"]["xGA"]
    GFTa1 = df.loc["Parma Calcio 1913", "a"]['xG']
    GSTa1 = df.loc["Parma Calcio 1913", "a"]["xGA"]
    PCa1 = df.loc["Parma Calcio 1913", "h"]["matches"]
    PTa1 = df.loc["Parma Calcio 1913", "a"]["matches"]
if a=="leipzig":
    GFCa1 = df.loc["RasenBallsport Leipzig", "h"]['xG']
    GSCa1 = df.loc["RasenBallsport Leipzig", "h"]["xGA"]
    GFTa1 = df.loc["RasenBallsport Leipzig", "a"]['xG']
    GSTa1 = df.loc["RasenBallsport Leipzig", "a"]["xGA"]
    PCa1 = df.loc["RasenBallsport Leipzig", "h"]["matches"]
    PTa1 = df.loc["RasenBallsport Leipzig", "a"]["matches"]
if a=="real betis":
    GFCa1 = df.loc["Real Betis", "h"]['xG']
    GSCa1 = df.loc["Real Betis", "h"]["xGA"]
    GFTa1 = df.loc["Real Betis", "a"]['xG']
    GSTa1 = df.loc["Real Betis", "a"]["xGA"]
    PCa1 = df.loc["Real Betis", "h"]["matches"]
    PTa1 = df.loc["Real Betis", "a"]["matches"]
if a=="real madrid":
    GFCa1 = df.loc["Real Madrid", "h"]['xG']
    GSCa1 = df.loc["Real Madrid", "h"]["xGA"]
    GFTa1 = df.loc["Real Madrid", "a"]['xG']
    GSTa1 = df.loc["Real Madrid", "a"]["xGA"]
    PCa1 = df.loc["Real Madrid", "h"]["matches"]
    PTa1 = df.loc["Real Madrid", "a"]["matches"]
if a=="real sociedad":
    GFCa1 = df.loc["Real Sociedad", "h"]['xG']
    GSCa1 = df.loc["Real Sociedad", "h"]["xGA"]
    GFTa1 = df.loc["Real Sociedad", "a"]['xG']
    GSTa1 = df.loc["Real Sociedad", "a"]["xGA"]
    PCa1 = df.loc["Real Sociedad", "h"]["matches"]
    PTa1 = df.loc["Real Sociedad", "a"]["matches"]
if a=="valladolid":
    GFCa1 = df.loc["Real Valladolid", "h"]['xG']
    GSCa1 = df.loc["Real Valladolid", "h"]["xGA"]
    GFTa1 = df.loc["Real Valladolid", "a"]['xG']
    GSTa1 = df.loc["Real Valladolid", "a"]["xGA"]
    PCa1 = df.loc["Real Valladolid", "h"]["matches"]
    PTa1 = df.loc["Real Valladolid", "a"]["matches"]
if a=="reims":
    GFCa1 = df.loc["Reims", "h"]['xG']
    GSCa1 = df.loc["Reims", "h"]["xGA"]
    GFTa1 = df.loc["Reims", "a"]['xG']
    GSTa1 = df.loc["Reims", "a"]["xGA"]
    PCa1 = df.loc["Reims", "h"]["matches"]
    PTa1 = df.loc["Reims", "a"]["matches"]
if a=="rennes":
    GFCa1 = df.loc["Rennes", "h"]['xG']
    GSCa1 = df.loc["Rennes", "h"]["xGA"]
    GFTa1 = df.loc["Rennes", "a"]['xG']
    GSTa1 = df.loc["Rennes", "a"]["xGA"]
    PCa1 = df.loc["Rennes", "h"]["matches"]
    PTa1 = df.loc["Rennes", "a"]["matches"]
if a=="roma":
    GFCa1 = df.loc["Roma", "h"]['xG']
    GSCa1 = df.loc["Roma", "h"]["xGA"]
    GFTa1 = df.loc["Roma", "a"]['xG']
    GSTa1 = df.loc["Roma", "a"]["xGA"]
    PCa1 = df.loc["Roma", "h"]["matches"]
    PTa1 = df.loc["Roma", "a"]["matches"]
if a=="huesca":
    GFCa1 = df.loc["SD Huesca", "h"]['xG']
    GSCa1 = df.loc["SD Huesca", "h"]["xGA"]
    GFTa1 = df.loc["SD Huesca", "a"]['xG']
    GSTa1 = df.loc["SD Huesca", "a"]["xGA"]
    PCa1 = df.loc["SD Huesca", "h"]["matches"]
    PTa1 = df.loc["SD Huesca", "a"]["matches"]
if a=="saint etienne":
    GFCa1 = df.loc["Saint-Etienne", "h"]['xG']
    GSCa1 = df.loc["Saint-Etienne", "h"]["xGA"]
    GFTa1 = df.loc["Saint-Etienne", "a"]['xG']
    GSTa1 = df.loc["Saint-Etienne", "a"]["xGA"]
    PCa1 = df.loc["Saint-Etienne", "h"]["matches"]
    PTa1 = df.loc["Saint-Etienne", "a"]["matches"]
if a=="sampdoria":
    GFCa1 = df.loc["Sampdoria", "h"]['xG']
    GSCa1 = df.loc["Sampdoria", "h"]["xGA"]
    GFTa1 = df.loc["Sampdoria", "a"]['xG']
    GSTa1 = df.loc["Sampdoria", "a"]["xGA"]
    PCa1 = df.loc["Sampdoria", "h"]["matches"]
    PTa1 = df.loc["Sampdoria", "a"]["matches"]
if a=="sassuolo":
    GFCa1 = df.loc["Sassuolo", "h"]['xG']
    GSCa1 = df.loc["Sassuolo", "h"]["xGA"]
    GFTa1 = df.loc["Sassuolo", "a"]['xG']
    GSTa1 = df.loc["Sassuolo", "a"]["xGA"]
    PCa1 = df.loc["Sassuolo", "h"]["matches"]
    PTa1 = df.loc["Sassuolo", "a"]["matches"]
if a=="schalke":
    GFCa1 = df.loc["Schalke 04", "h"]['xG']
    GSCa1 = df.loc["Schalke 04", "h"]["xGA"]
    GFTa1 = df.loc["Schalke 04", "a"]['xG']
    GSTa1 = df.loc["Schalke 04", "a"]["xGA"]
    PCa1 = df.loc["Schalke 04", "h"]["matches"]
    PTa1 = df.loc["Schalke 04", "a"]["matches"]
if a=="sevilla":
    GFCa1 = df.loc["Sevilla", "h"]['xG']
    GSCa1 = df.loc["Sevilla", "h"]["xGA"]
    GFTa1 = df.loc["Sevilla", "a"]['xG']
    GSTa1 = df.loc["Sevilla", "a"]["xGA"]
    PCa1 = df.loc["Sevilla", "h"]["matches"]
    PTa1 = df.loc["Sevilla", "a"]["matches"]
if a=="sheffield":
    GFCa1 = df.loc["Sheffield United", "h"]['xG']
    GSCa1 = df.loc["Sheffield United", "h"]["xGA"]
    GFTa1 = df.loc["Sheffield United", "a"]['xG']
    GSTa1 = df.loc["Sheffield United", "a"]["xGA"]
    PCa1 = df.loc["Sheffield United", "h"]["matches"]
    PTa1 = df.loc["Sheffield United", "a"]["matches"]
if a=="southampton":
    GFCa1 = df.loc["Southampton", "h"]['xG']
    GSCa1 = df.loc["Southampton", "h"]["xGA"]
    GFTa1 = df.loc["Southampton", "a"]['xG']
    GSTa1 = df.loc["Southampton", "a"]["xGA"]
    PCa1 = df.loc["Southampton", "h"]["matches"]
    PTa1 = df.loc["Southampton", "a"]["matches"]
if a=="spezia":
    GFCa1 = df.loc["Spezia", "h"]['xG']
    GSCa1 = df.loc["Spezia", "h"]["xGA"]
    GFTa1 = df.loc["Spezia", "a"]['xG']
    GSTa1 = df.loc["Spezia", "a"]["xGA"]
    PCa1 = df.loc["Spezia", "h"]["matches"]
    PTa1 = df.loc["Spezia", "a"]["matches"]
if a=="strasbourg":
    GFCa1 = df.loc["Strasbourg", "h"]['xG']
    GSCa1 = df.loc["Strasbourg", "h"]["xGA"]
    GFTa1 = df.loc["Strasbourg", "a"]['xG']
    GSTa1 = df.loc["Strasbourg", "a"]["xGA"]
    PCa1 = df.loc["Strasbourg", "h"]["matches"]
    PTa1 = df.loc["Strasbourg", "a"]["matches"]
if a=="torino":
    GFCa1 = df.loc["Torino", "h"]['xG']
    GSCa1 = df.loc["Torino", "h"]["xGA"]
    GFTa1 = df.loc["Torino", "a"]['xG']
    GSTa1 = df.loc["Torino", "a"]["xGA"]
    PCa1 = df.loc["Torino", "h"]["matches"]
    PTa1 = df.loc["Torino", "a"]["matches"]
if a=="tottenham":
    GFCa1 = df.loc["Tottenham", "h"]['xG']
    GSCa1 = df.loc["Tottenham", "h"]["xGA"]
    GFTa1 = df.loc["Tottenham", "a"]['xG']
    GSTa1 = df.loc["Tottenham", "a"]["xGA"]
    PCa1 = df.loc["Tottenham", "h"]["matches"]
    PTa1 = df.loc["Tottenham", "a"]["matches"]
if a=="udinese":
    GFCa1 = df.loc["Udinese", "h"]['xG']
    GSCa1 = df.loc["Udinese", "h"]["xGA"]
    GFTa1 = df.loc["Udinese", "a"]['xG']
    GSTa1 = df.loc["Udinese", "a"]["xGA"]
    PCa1 = df.loc["Udinese", "h"]["matches"]
    PTa1 = df.loc["Udinese", "a"]["matches"]
if a=="union berlin":
    GFCa1 = df.loc["Union Berlin", "h"]['xG']
    GSCa1 = df.loc["Union Berlin", "h"]["xGA"]
    GFTa1 = df.loc["Union Berlin", "a"]['xG']
    GSTa1 = df.loc["Union Berlin", "a"]["xGA"]
    PCa1 = df.loc["Union Berlin", "h"]["matches"]
    PTa1 = df.loc["Union Berlin", "a"]["matches"]
if a=="valencia":
    GFCa1 = df.loc["Valencia", "h"]['xG']
    GSCa1 = df.loc["Valencia", "h"]["xGA"]
    GFTa1 = df.loc["Valencia", "a"]['xG']
    GSTa1 = df.loc["Valencia", "a"]["xGA"]
    PCa1 = df.loc["Valencia", "h"]["matches"]
    PTa1 = df.loc["Valencia", "a"]["matches"]
if a=="verona":
    GFCa1 = df.loc["Verona", "h"]['xG']
    GSCa1 = df.loc["Verona", "h"]["xGA"]
    GFTa1 = df.loc["Verona", "a"]['xG']
    GSTa1 = df.loc["Verona", "a"]["xGA"]
    PCa1 = df.loc["Verona", "h"]["matches"]
    PTa1 = df.loc["Verona", "a"]["matches"]
if a=="stuttgart":
    GFCa1 = df.loc["VfB Stuttgart", "h"]['xG']
    GSCa1 = df.loc["VfB Stuttgart", "h"]["xGA"]
    GFTa1 = df.loc["VfB Stuttgart", "a"]['xG']
    GSTa1 = df.loc["VfB Stuttgart", "a"]["xGA"]
    PCa1 = df.loc["VfB Stuttgart", "h"]["matches"]
    PTa1 = df.loc["VfB Stuttgart", "a"]["matches"]
if a=="villareal":
    GFCa1 = df.loc["Villarreal", "h"]['xG']
    GSCa1 = df.loc["Villarreal", "h"]["xGA"]
    GFTa1 = df.loc["Villarreal", "a"]['xG']
    GSTa1 = df.loc["Villarreal", "a"]["xGA"]
    PCa1 = df.loc["Villarreal", "h"]["matches"]
    PTa1 = df.loc["Villarreal", "a"]["matches"]
if a=="werder brema":
    GFCa1 = df.loc["Werder Bremen", "h"]['xG']
    GSCa1 = df.loc["Werder Bremen", "h"]["xGA"]
    GFTa1 = df.loc["Werder Bremen", "a"]['xG']
    GSTa1 = df.loc["Werder Bremen", "a"]["xGA"]
    PCa1 = df.loc["Werder Bremen", "h"]["matches"]
    PTa1 = df.loc["Werder Bremen", "a"]["matches"]
if a=="west bromwich":
    GFCa1 = df.loc["West Bromwich Albion", "h"]['xG']
    GSCa1 = df.loc["West Bromwich Albion", "h"]["xGA"]
    GFTa1 = df.loc["West Bromwich Albion", "a"]['xG']
    GSTa1 = df.loc["West Bromwich Albion", "a"]["xGA"]
    PCa1 = df.loc["West Bromwich Albion", "h"]["matches"]
    PTa1 = df.loc["West Bromwich Albion", "a"]["matches"]
if a=="west ham":
    GFCa1 = df.loc["West Ham", "h"]['xG']
    GSCa1 = df.loc["West Ham", "h"]["xGA"]
    GFTa1 = df.loc["West Ham", "a"]['xG']
    GSTa1 = df.loc["West Ham", "a"]["xGA"]
    PCa1 = df.loc["West Ham", "h"]["matches"]
    PTa1 = df.loc["West Ham", "a"]["matches"]
if a=="wolfsburg":
    GFCa1 = df.loc["Wolfsburg", "h"]['xG']
    GSCa1 = df.loc["Wolfsburg", "h"]["xGA"]
    GFTa1 = df.loc["Wolfsburg", "a"]['xG']
    GSTa1 = df.loc["Wolfsburg", "a"]["xGA"]
    PCa1 = df.loc["Wolfsburg", "h"]["matches"]
    PTa1 = df.loc["Wolfsburg", "a"]["matches"]
if a=="wolverhampton":
    GFCa1 = df.loc["Wolverhampton Wanderers", "h"]['xG']
    GSCa1 = df.loc["Wolverhampton Wanderers", "h"]["xGA"]
    GFTa1 = df.loc["Wolverhampton Wanderers", "a"]['xG']
    GSTa1 = df.loc["Wolverhampton Wanderers", "a"]["xGA"]
    PCa1 = df.loc["Wolverhampton Wanderers", "h"]["matches"]
    PTa1 = df.loc["Wolverhampton Wanderers", "a"]["matches"]
    

#----------------------------- Away Team Stats ---------------------------------------------------
if b=="milan":
    GFCa2 = df.loc["AC Milan", "h"]['xG']
    GSCa2 = df.loc["AC Milan", "h"]["xGA"]
    GFTa2 = df.loc["AC Milan", "a"]['xG']
    GSTa2 = df.loc["AC Milan", "a"]["xGA"]
    PCa2 = df.loc["AC Milan", "h"]["matches"]
    PTa2 = df.loc["AC Milan", "a"]["matches"]
if b=="alaves":
    GFCa2 = df.loc["Alaves", "h"]['xG']
    GSCa2 = df.loc["Alaves", "h"]["xGA"]
    GFTa2 = df.loc["Alaves", "a"]['xG']
    GSTa2 = df.loc["Alaves", "a"]["xGA"]
    PCa2 = df.loc["Alaves", "h"]["matches"]
    PTa2 = df.loc["Alaves", "a"]["matches"]
if b=="angers":
    GFCa2 = df.loc["Angers", "h"]['xG']
    GSCa2 = df.loc["Angers", "h"]["xGA"]
    GFTa2 = df.loc["Angers", "a"]['xG']
    GSTa2 = df.loc["Angers", "a"]["xGA"]
    PCa2 = df.loc["Angers", "h"]["matches"]
    PTa2 = df.loc["Angers", "a"]["matches"]
if b=="arsenal":
    GFCa2 = df.loc["Arsenal", "h"]['xG']
    GSCa2 = df.loc["Arsenal", "h"]["xGA"]
    GFTa2 = df.loc["Arsenal", "a"]['xG']
    GSTa2 = df.loc["Arsenal", "a"]["xGA"]
    PCa2 = df.loc["Arsenal", "h"]["matches"]
    PTa2 = df.loc["Arsenal", "a"]["matches"]
if b=="aston villa":
    GFCa2 = df.loc["Aston Villa", "h"]['xG']
    GSCa2 = df.loc["Aston Villa", "h"]["xGA"]
    GFTa2 = df.loc["Aston Villa", "a"]['xG']
    GSTa2 = df.loc["Aston Villa", "a"]["xGA"]
    PCa2 = df.loc["Aston Villa", "h"]["matches"]
    PTa2 = df.loc["Aston Villa", "a"]["matches"]
if b=="atalanta":
    GFCa2 = df.loc["Atalanta", "h"]['xG']
    GSCa2 = df.loc["Atalanta", "h"]["xGA"]
    GFTa2 = df.loc["Atalanta", "a"]['xG']
    GSTa2 = df.loc["Atalanta", "a"]["xGA"]
    PCa2 = df.loc["Atalanta", "h"]["matches"]
    PTa2 = df.loc["Atalanta", "a"]["matches"]
if b=="athletic":
    GFCa2 = df.loc["Athletic Club", "h"]['xG']
    GSCa2 = df.loc["Athletic Club", "h"]["xGA"]
    GFTa2 = df.loc["Athletic Club", "a"]['xG']
    GSTa2 = df.loc["Athletic Club", "a"]["xGA"]
    PCa2 = df.loc["Athletic Club", "h"]["matches"]
    PTa2 = df.loc["Athletic Club", "a"]["matches"]
if b=="atletico madrid":
    GFCa2 = df.loc["Atletico Madrid", "h"]['xG']
    GSCa2 = df.loc["Atletico Madrid", "h"]["xGA"]
    GFTa2 = df.loc["Atletico Madrid", "a"]['xG']
    GSTa2 = df.loc["Atletico Madrid", "a"]["xGA"]
    PCa2 = df.loc["Atletico Madrid", "h"]["matches"]
    PTa2 = df.loc["Atletico Madrid", "a"]["matches"]
if b=="augsburg":
    GFCa2 = df.loc["Augsburg", "h"]['xG']
    GSCa2 = df.loc["Augsburg", "h"]["xGA"]
    GFTa2 = df.loc["Augsburg", "a"]['xG']
    GSTa2 = df.loc["Augsburg", "a"]["xGA"]
    PCa2 = df.loc["Augsburg", "h"]["matches"]
    PTa2 = df.loc["Augsburg", "a"]["matches"]
if b=="barcelona":
    GFCa2 = df.loc["Barcelona", "h"]['xG']
    GSCa2 = df.loc["Barcelona", "h"]["xGA"]
    GFTa2 = df.loc["Barcelona", "a"]['xG']
    GSTa2 = df.loc["Barcelona", "a"]["xGA"]
    PCa2 = df.loc["Barcelona", "h"]["matches"]
    PTa2 = df.loc["Barcelona", "a"]["matches"]
if b=="bayer leverkusen":
    GFCa2 = df.loc["Bayer Leverkusen", "h"]['xG']
    GSCa2 = df.loc["Bayer Leverkusen", "h"]["xGA"]
    GFTa2 = df.loc["Bayer Leverkusen", "a"]['xG']
    GSTa2 = df.loc["Bayer Leverkusen", "a"]["xGA"]
    PCa2 = df.loc["Bayer Leverkusen", "h"]["matches"]
    PTa2 = df.loc["Bayer Leverkusen", "a"]["matches"]
if b=="bayern munich":
    GFCa2 = df.loc["Bayern Munich", "h"]['xG']
    GSCa2 = df.loc["Bayern Munich", "h"]["xGA"]
    GFTa2 = df.loc["Bayern Munich", "a"]['xG']
    GSTa2 = df.loc["Bayern Munich", "a"]["xGA"]
    PCa2 = df.loc["Bayern Munich", "h"]["matches"]
    PTa2 = df.loc["Bayern Munich", "a"]["matches"]
if b=="benevento":
    GFCa2 = df.loc["Benevento", "h"]['xG']
    GSCa2 = df.loc["Benevento", "h"]["xGA"]
    GFTa2 = df.loc["Benevento", "a"]['xG']
    GSTa2 = df.loc["Benevento", "a"]["xGA"]
    PCa2 = df.loc["Benevento", "h"]["matches"]
    PTa2 = df.loc["Benevento", "a"]["matches"]
if b=="bologna":
    GFCa2 = df.loc["Bologna", "h"]['xG']
    GSCa2 = df.loc["Bologna", "h"]["xGA"]
    GFTa2 = df.loc["Bologna", "a"]['xG']
    GSTa2 = df.loc["Bologna", "a"]["xGA"]
    PCa2 = df.loc["Bologna", "h"]["matches"]
    PTa2 = df.loc["Bologna", "a"]["matches"]
if b=="bordeaux":
    GFCa2 = df.loc["Bordeaux", "h"]['xG']
    GSCa2 = df.loc["Bordeaux", "h"]["xGA"]
    GFTa2 = df.loc["Bordeaux", "a"]['xG']
    GSTa2 = df.loc["Bordeaux", "a"]["xGA"]
    PCa2 = df.loc["Bordeaux", "h"]["matches"]
    PTa2 = df.loc["Bordeaux", "a"]["matches"]
if b=="borussia dortmund":
    GFCa2 = df.loc["Borussia Dortmund", "h"]['xG']
    GSCa2 = df.loc["Borussia Dortmund", "h"]["xGA"]
    GFTa2 = df.loc["Borussia Dortmund", "a"]['xG']
    GSTa2 = df.loc["Borussia Dortmund", "a"]["xGA"]
    PCa2 = df.loc["Borussia Dortmund", "h"]["matches"]
    PTa2 = df.loc["Borussia Dortmund", "a"]["matches"]
if b=="borussia mgladbach":
    GFCa2 = df.loc["Borussia M.Gladbach", "h"]['xG']
    GSCa2 = df.loc["Borussia M.Gladbach", "h"]["xGA"]
    GFTa2 = df.loc["Borussia M.Gladbach", "a"]['xG']
    GSTa2 = df.loc["Borussia M.Gladbach", "a"]["xGA"]
    PCa2 = df.loc["Borussia M.Gladbach", "h"]["matches"]
    PTa2 = df.loc["Borussia M.Gladbach", "a"]["matches"]
if b=="brest":
    GFCa2 = df.loc["Brest", "h"]['xG']
    GSCa2 = df.loc["Brest", "h"]["xGA"]
    GFTa2 = df.loc["Brest", "a"]['xG']
    GSTa2 = df.loc["Brest", "a"]["xGA"]
    PCa2 = df.loc["Brest", "h"]["matches"]
    PTa2 = df.loc["Brest", "a"]["matches"]
if b=="brighton":
    GFCa2 = df.loc["Brighton", "h"]['xG']
    GSCa2 = df.loc["Brighton", "h"]["xGA"]
    GFTa2 = df.loc["Brighton", "a"]['xG']
    GSTa2 = df.loc["Brighton", "a"]["xGA"]
    PCa2 = df.loc["Brighton", "h"]["matches"]
    PTa2 = df.loc["Brighton", "a"]["matches"]
if b=="burnley":
    GFCa2 = df.loc["Burnley", "h"]['xG']
    GSCa2 = df.loc["Burnley", "h"]["xGA"]
    GFTa2 = df.loc["Burnley", "a"]['xG']
    GSTa2 = df.loc["Burnley", "a"]["xGA"]
    PCa2 = df.loc["Burnley", "h"]["matches"]
    PTa2 = df.loc["Burnley", "a"]["matches"]
if b=="cadiz":
    GFCa2 = df.loc["Cadiz", "h"]['xG']
    GSCa2 = df.loc["Cadiz", "h"]["xGA"]
    GFTa2 = df.loc["Cadiz", "a"]['xG']
    GSTa2 = df.loc["Cadiz", "a"]["xGA"]
    PCa2 = df.loc["Cadiz", "h"]["matches"]
    PTa2 = df.loc["Cadiz", "a"]["matches"]
if b=="cagliari":
    GFCa2 = df.loc["Cagliari", "h"]['xG']
    GSCa2 = df.loc["Cagliari", "h"]["xGA"]
    GFTa2 = df.loc["Cagliari", "a"]['xG']
    GSTa2 = df.loc["Cagliari", "a"]["xGA"]
    PCa2 = df.loc["Cagliari", "h"]["matches"]
    PTa2 = df.loc["Cagliari", "a"]["matches"]
if b=="celta vigo":
    GFCa2 = df.loc["Celta Vigo", "h"]['xG']
    GSCa2 = df.loc["Celta Vigo", "h"]["xGA"]
    GFTa2 = df.loc["Celta Vigo", "a"]['xG']
    GSTa2 = df.loc["Celta Vigo", "a"]["xGA"]
    PCa2 = df.loc["Celta Vigo", "h"]["matches"]
    PTa2 = df.loc["Celta Vigo", "a"]["matches"]
if b=="chelsea":
    GFCa2 = df.loc["Chelsea", "h"]['xG']
    GSCa2 = df.loc["Chelsea", "h"]["xGA"]
    GFTa2 = df.loc["Chelsea", "a"]['xG']
    GSTa2 = df.loc["Chelsea", "a"]["xGA"]
    PCa2 = df.loc["Chelsea", "h"]["matches"]
    PTa2 = df.loc["Chelsea", "a"]["matches"]
if b=="crotone":
    GFCa2 = df.loc["Crotone", "h"]['xG']
    GSCa2 = df.loc["Crotone", "h"]["xGA"]
    GFTa2 = df.loc["Crotone", "a"]['xG']
    GSTa2 = df.loc["Crotone", "a"]["xGA"]
    PCa2 = df.loc["Crotone", "h"]["matches"]
    PTa2 = df.loc["Crotone", "a"]["matches"]
if b=="crystal palace":
    GFCa2 = df.loc["Crystal Palace", "h"]['xG']
    GSCa2 = df.loc["Crystal Palace", "h"]["xGA"]
    GFTa2 = df.loc["Crystal Palace", "a"]['xG']
    GSTa2 = df.loc["Crystal Palace", "a"]["xGA"]
    PCa2 = df.loc["Crystal Palace", "h"]["matches"]
    PTa2 = df.loc["Crystal Palace", "a"]["matches"]
if b=="dijon":
    GFCa2 = df.loc["Dijon", "h"]['xG']
    GSCa2 = df.loc["Dijon", "h"]["xGA"]
    GFTa2 = df.loc["Dijon", "a"]['xG']
    GSTa2 = df.loc["Dijon", "a"]["xGA"]
    PCa2 = df.loc["Dijon", "h"]["matches"]
    PTa2 = df.loc["Dijon", "a"]["matches"]
if b=="eibar":
    GFCa2 = df.loc["Eibar", "h"]['xG']
    GSCa2 = df.loc["Eibar", "h"]["xGA"]
    GFTa2 = df.loc["Eibar", "a"]['xG']
    GSTa2 = df.loc["Eibar", "a"]["xGA"]
    PCa2 = df.loc["Eibar", "h"]["matches"]
    PTa2 = df.loc["Eibar", "a"]["matches"]
if b=="eintracht frankfurt":
    GFCa2 = df.loc["Eintracht Frankfurt", "h"]['xG']
    GSCa2 = df.loc["Eintracht Frankfurt", "h"]["xGA"]
    GFTa2 = df.loc["Eintracht Frankfurt", "a"]['xG']
    GSTa2 = df.loc["Eintracht Frankfurt", "a"]["xGA"]
    PCa2 = df.loc["Eintracht Frankfurt", "h"]["matches"]
    PTa2 = df.loc["Eintracht Frankfurt", "a"]["matches"]
if b=="elche":
    GFCa2 = df.loc["Elche", "h"]['xG']
    GSCa2 = df.loc["Elche", "h"]["xGA"]
    GFTa2 = df.loc["Elche", "a"]['xG']
    GSTa2 = df.loc["Elche", "a"]["xGA"]
    PCa2 = df.loc["Elche", "h"]["matches"]
    PTa2 = df.loc["Elche", "a"]["matches"]
if b=="everton":
    GFCa2 = df.loc["Everton", "h"]['xG']
    GSCa2 = df.loc["Everton", "h"]["xGA"]
    GFTa2 = df.loc["Everton", "a"]['xG']
    GSTa2 = df.loc["Everton", "a"]["xGA"]
    PCa2 = df.loc["Everton", "h"]["matches"]
    PTa2 = df.loc["Everton", "a"]["matches"]
if b=="cologne":
    GFCa2 = df.loc["FC Cologne", "h"]['xG']
    GSCa2 = df.loc["FC Cologne", "h"]["xGA"]
    GFTa2 = df.loc["FC Cologne", "a"]['xG']
    GSTa2 = df.loc["FC Cologne", "a"]["xGA"]
    PCa2 = df.loc["FC Cologne", "h"]["matches"]
    PTa2 = df.loc["FC Cologne", "a"]["matches"]
if b=="fiorentina":
    GFCa2 = df.loc["Fiorentina", "h"]['xG']
    GSCa2 = df.loc["Fiorentina", "h"]["xGA"]
    GFTa2 = df.loc["Fiorentina", "a"]['xG']
    GSTa2 = df.loc["Fiorentina", "a"]["xGA"]
    PCa2 = df.loc["Fiorentina", "h"]["matches"]
    PTa2 = df.loc["Fiorentina", "a"]["matches"]
if b=="freiburg":
    GFCa2 = df.loc["Freiburg", "h"]['xG']
    GSCa2 = df.loc["Freiburg", "h"]["xGA"]
    GFTa2 = df.loc["Freiburg", "a"]['xG']
    GSTa2 = df.loc["Freiburg", "a"]["xGA"]
    PCa2 = df.loc["Freiburg", "h"]["matches"]
    PTa2 = df.loc["Freiburg", "a"]["matches"]
if b=="fulham":
    GFCa2 = df.loc["Fulham", "h"]['xG']
    GSCa2 = df.loc["Fulham", "h"]["xGA"]
    GFTa2 = df.loc["Fulham", "a"]['xG']
    GSTa2 = df.loc["Fulham", "a"]["xGA"]
    PCa2 = df.loc["Fulham", "h"]["matches"]
    PTa2 = df.loc["Fulham", "a"]["matches"]
if b=="genoa":
    GFCa2 = df.loc["Genoa", "h"]['xG']
    GSCa2 = df.loc["Genoa", "h"]["xGA"]
    GFTa2 = df.loc["Genoa", "a"]['xG']
    GSTa2 = df.loc["Genoa", "a"]["xGA"]
    PCa2 = df.loc["Genoa", "h"]["matches"]
    PTa2 = df.loc["Genoa", "a"]["matches"]
if b=="getafe":
    GFCa2 = df.loc["Getafe", "h"]['xG']
    GSCa2 = df.loc["Getafe", "h"]["xGA"]
    GFTa2 = df.loc["Getafe", "a"]['xG']
    GSTa2 = df.loc["Getafe", "a"]["xGA"]
    PCa2 = df.loc["Getafe", "h"]["matches"]
    PTa2 = df.loc["Getafe", "a"]["matches"]
if b=="granada":
    GFCa2 = df.loc["Granada", "h"]['xG']
    GSCa2 = df.loc["Granada", "h"]["xGA"]
    GFTa2 = df.loc["Granada", "a"]['xG']
    GSTa2 = df.loc["Granada", "a"]["xGA"]
    PCa2 = df.loc["Granada", "h"]["matches"]
    PTa2 = df.loc["Granada", "a"]["matches"]
if b=="hertha berlin;":
    GFCa2 = df.loc["Hertha Berlin", "h"]['xG']
    GSCa2 = df.loc["Hertha Berlin", "h"]["xGA"]
    GFTa2 = df.loc["Hertha Berlin", "a"]['xG']
    GSTa1 = df.loc["Hertha Berlin", "a"]["xGA"]
    PCa2 = df.loc["Hertha Berlin", "h"]["matches"]
    PTa2 = df.loc["Hertha Berlin", "a"]["matches"]
if b=="hoffenheim":
    GFCa2 = df.loc["Hoffenheim", "h"]['xG']
    GSCa2 = df.loc["Hoffenheim", "h"]["xGA"]
    GFTa2 = df.loc["Hoffenheim", "a"]['xG']
    GSTa2 = df.loc["Hoffenheim", "a"]["xGA"]
    PCa2 = df.loc["Hoffenheim", "h"]["matches"]
    PTa2 = df.loc["Hoffenheim", "a"]["matches"]
if b=="inter":
    GFCa2 = df.loc["Inter", "h"]['xG']
    GSCa2= df.loc["Inter", "h"]["xGA"]
    GFTa2 = df.loc["Inter", "a"]['xG']
    GSTa2 = df.loc["Inter", "a"]["xGA"]
    PCa2 = df.loc["Inter", "h"]["matches"]
    PTa2 = df.loc["Inter", "a"]["matches"]
if b=="juventus":
    GFCa2 = df.loc["Juventus", "h"]['xG']
    GSCa2 = df.loc["Juventus", "h"]["xGA"]
    GFTa2 = df.loc["Juventus", "a"]['xG']
    GSTa2 = df.loc["Juventus", "a"]["xGA"]
    PCa2 = df.loc["Juventus", "h"]["matches"]
    PTa2 = df.loc["Juventus", "a"]["matches"]
if b=="lazio":
    GFCa2 = df.loc["Lazio", "h"]['xG']
    GSCa2 = df.loc["Lazio", "h"]["xGA"]
    GFTa2 = df.loc["Lazio", "a"]['xG']
    GSTa2 = df.loc["Lazio", "a"]["xGA"]
    PCa2 = df.loc["Lazio", "h"]["matches"]
    PTa2 = df.loc["Lazio", "a"]["matches"]
if b=="leeds":
    GFCa2 = df.loc["Leeds", "h"]['xG']
    GSCa2 = df.loc["Leeds", "h"]["xGA"]
    GFTa2 = df.loc["Leeds", "a"]['xG']
    GSTa2 = df.loc["Leeds", "a"]["xGA"]
    PCa2 = df.loc["Leeds", "h"]["matches"]
    PTa2 = df.loc["Leeds", "a"]["matches"]
if b=="leicester":
    GFCa2 = df.loc["Leicester", "h"]['xG']
    GSCa2 = df.loc["Leicester", "h"]["xGA"]
    GFTa2 = df.loc["Leicester", "a"]['xG']
    GSTa2 = df.loc["Leicester", "a"]["xGA"]
    PCa2 = df.loc["Leicester", "h"]["matches"]
    PTa2 = df.loc["Leicester", "a"]["matches"]
if b=="lens":
    GFCa2 = df.loc["Lens", "h"]['xG']
    GSCa2 = df.loc["Lens", "h"]["xGA"]
    GFTa2 = df.loc["Lens", "a"]['xG']
    GSTa2 = df.loc["Lens", "a"]["xGA"]
    PCa2 = df.loc["Lens", "h"]["matches"]
    PTa2 = df.loc["Lens", "a"]["matches"]
if b=="levante":
    GFCa2 = df.loc["Levante", "h"]['xG']
    GSCa2 = df.loc["Levante", "h"]["xGA"]
    GFTa2 = df.loc["Levante", "a"]['xG']
    GSTa2 = df.loc["Levante", "a"]["xGA"]
    PCa2 = df.loc["Levante", "h"]["matches"]
    PTa2 = df.loc["Levante", "a"]["matches"]
if b=="lille":
    GFCa2 = df.loc["Lille", "h"]['xG']
    GSCa2 = df.loc["Lille", "h"]["xGA"]
    GFTa2 = df.loc["Lille", "a"]['xG']
    GSTa2 = df.loc["Lille", "a"]["xGA"]
    PCa2 = df.loc["Lille", "h"]["matches"]
    PTa2 = df.loc["Lille", "a"]["matches"]
if b=="liverpool":
    GFCa2 = df.loc["Liverpool", "h"]['xG']
    GSCa2 = df.loc["Liverpool", "h"]["xGA"]
    GFTa2 = df.loc["Liverpool", "a"]['xG']
    GSTa2 = df.loc["Liverpool", "a"]["xGA"]
    PCa2 = df.loc["Liverpool", "h"]["matches"]
    PTa2 = df.loc["Liverpool", "a"]["matches"]
if b=="lorient":
    GFCa2 = df.loc["Lorient", "h"]['xG']
    GSCa2 = df.loc["Lorient", "h"]["xGA"]
    GFTa2 = df.loc["Lorient", "a"]['xG']
    GSTa2 = df.loc["Lorient", "a"]["xGA"]
    PCa2 = df.loc["Lorient", "h"]["matches"]
    PTa2 = df.loc["Lorient", "a"]["matches"]
if b=="lyon":
    GFCa2 = df.loc["Lyon", "h"]['xG']
    GSCa2 = df.loc["Lyon", "h"]["xGA"]
    GFTa2 = df.loc["Lyon", "a"]['xG']
    GSTa2 = df.loc["Lyon", "a"]["xGA"]
    PCa2 = df.loc["Lyon", "h"]["matches"]
    PTa2 = df.loc["Lyon", "a"]["matches"]
if b=="mainz":
    GFCa2 = df.loc["Mainz 05", "h"]['xG']
    GSCa2 = df.loc["Mainz 05", "h"]["xGA"]
    GFTa2 = df.loc["Mainz 05", "a"]['xG']
    GSTa2 = df.loc["Mainz 05", "a"]["xGA"]
    PCa2 = df.loc["Mainz 05", "h"]["matches"]
    PTa2 = df.loc["Mainz 05", "a"]["matches"]
if b=="manchester city":
    GFCa2 = df.loc["Manchester City", "h"]['xG']
    GSCa2 = df.loc["Manchester City", "h"]["xGA"]
    GFTa2 = df.loc["Manchester City", "a"]['xG']
    GSTa2 = df.loc["Manchester City", "a"]["xGA"]
    PCa2 = df.loc["Manchester City", "h"]["matches"]
    PTa2 = df.loc["Manchester City", "a"]["matches"]
if b=="manchester united":
    GFCa2 = df.loc["Manchester United", "h"]['xG']
    GSCa2 = df.loc["Manchester United", "h"]["xGA"]
    GFTa2 = df.loc["Manchester United", "a"]['xG']
    GSTa2 = df.loc["Manchester United", "a"]["xGA"]
    PCa2 = df.loc["Manchester United", "h"]["matches"]
    PTa2 = df.loc["Manchester United", "a"]["matches"]
if b=="marseille":
    GFCa2 = df.loc["Marseille", "h"]['xG']
    GSCa2 = df.loc["Marseille", "h"]["xGA"]
    GFTa2 = df.loc["Marseille", "a"]['xG']
    GSTa2 = df.loc["Marseille", "a"]["xGA"]
    PCa2 = df.loc["Marseille", "h"]["matches"]
    PTa2 = df.loc["Marseille", "a"]["matches"]
if b=="metz":
    GFCa2 = df.loc["Metz", "h"]['xG']
    GSCa2 = df.loc["Metz", "h"]["xGA"]
    GFTa2 = df.loc["Metz", "a"]['xG']
    GSTa2 = df.loc["Metz", "a"]["xGA"]
    PCa2 = df.loc["Metz", "h"]["matches"]
    PTa2 = df.loc["Metz", "a"]["matches"]
if b=="monaco":
    GFCa2 = df.loc["Monaco", "h"]['xG']
    GSCa2 = df.loc["Monaco", "h"]["xGA"]
    GFTa2 = df.loc["Monaco", "a"]['xG']
    GSTa2 = df.loc["Monaco", "a"]["xGA"]
    PCa2 = df.loc["Monaco", "h"]["matches"]
    PTa2 = df.loc["Monaco", "a"]["matches"]
if b=="montpellier":
    GFCa2 = df.loc["Montpellier", "h"]['xG']
    GSCa2 = df.loc["Montpellier", "h"]["xGA"]
    GFTa2 = df.loc["Montpellier", "a"]['xG']
    GSTa2 = df.loc["Montpellier", "a"]["xGA"]
    PCa2 = df.loc["Montpellier", "h"]["matches"]
    PTa2 = df.loc["Montpellier", "a"]["matches"]
if b=="nantes":
    GFCa2 = df.loc["Nantes", "h"]['xG']
    GSCa2 = df.loc["Nantes", "h"]["xGA"]
    GFTa2 = df.loc["Nantes", "a"]['xG']
    GSTa2 = df.loc["Nantes", "a"]["xGA"]
    PCa2 = df.loc["Nantes", "h"]["matches"]
    PTa2 = df.loc["Nantes", "a"]["matches"]
if b=="napoli":
    GFCa1 = df.loc["Napoli", "h"]['xG']
    GSCa1 = df.loc["Napoli", "h"]["xGA"]
    GFTa1 = df.loc["Napoli", "a"]['xG']
    GSTa1 = df.loc["Napoli", "a"]["xGA"]
    PCa1 = df.loc["Napoli", "h"]["matches"]
    PTa1 = df.loc["Napoli", "a"]["matches"]
if b=="newcastle":
    GFCa2 = df.loc["Newcastle United", "h"]['xG']
    GSCa2 = df.loc["Newcastle United", "h"]["xGA"]
    GFTa2 = df.loc["Newcastle United", "a"]['xG']
    GSTa2 = df.loc["Newcastle United", "a"]["xGA"]
    PCa2 = df.loc["Newcastle United", "h"]["matches"]
    PTa2 = df.loc["Newcastle United", "a"]["matches"]
if b=="nice":
    GFCa2 = df.loc["Nice", "h"]['xG']
    GSCa2 = df.loc["Nice", "h"]["xGA"]
    GFTa2 = df.loc["Nice", "a"]['xG']
    GSTa2 = df.loc["Nice", "a"]["xGA"]
    PCa2 = df.loc["Nice", "h"]["matches"]
    PTa2 = df.loc["Nice", "a"]["matches"]
if b=="nimes":
    GFCa2 = df.loc["Nimes", "h"]['xG']
    GSCa2 = df.loc["Nimes", "h"]["xGA"]
    GFTa2 = df.loc["Nimes", "a"]['xG']
    GSTa2 = df.loc["Nimes", "a"]["xGA"]
    PCa2 = df.loc["Nimes", "h"]["matches"]
    PTa2 = df.loc["Nimes", "a"]["matches"]
if b=="osasuna":
    GFCa2 = df.loc["Osasuna", "h"]['xG']
    GSCa2 = df.loc["Osasuna", "h"]["xGA"]
    GFTa2 = df.loc["Osasuna", "a"]['xG']
    GSTa2 = df.loc["Osasuna", "a"]["xGA"]
    PCa2 = df.loc["Osasuna", "h"]["matches"]
    PTa2 = df.loc["Osasuna", "a"]["matches"]
if b=="psg":
    GFCa2 = df.loc["Paris Saint Germain", "h"]['xG']
    GSCa2 = df.loc["Paris Saint Germain", "h"]["xGA"]
    GFTa2 = df.loc["Paris Saint Germain", "a"]['xG']
    GSTa2 = df.loc["Paris Saint Germain", "a"]["xGA"]
    PCa2 = df.loc["Paris Saint Germain", "h"]["matches"]
    PTa2 = df.loc["Paris Saint Germain", "a"]["matches"]
if b=="parma":
    GFCa2 = df.loc["Parma Calcio 1913", "h"]['xG']
    GSCa2 = df.loc["Parma Calcio 1913", "h"]["xGA"]
    GFTa2 = df.loc["Parma Calcio 1913", "a"]['xG']
    GSTa2 = df.loc["Parma Calcio 1913", "a"]["xGA"]
    PCa2 = df.loc["Parma Calcio 1913", "h"]["matches"]
    PTa2 = df.loc["Parma Calcio 1913", "a"]["matches"]
if b=="leipzig":
    GFCa2 = df.loc["RasenBallsport Leipzig", "h"]['xG']
    GSCa2 = df.loc["RasenBallsport Leipzig", "h"]["xGA"]
    GFTa2 = df.loc["RasenBallsport Leipzig", "a"]['xG']
    GSTa2 = df.loc["RasenBallsport Leipzig", "a"]["xGA"]
    PCa2 = df.loc["RasenBallsport Leipzig", "h"]["matches"]
    PTa2 = df.loc["RasenBallsport Leipzig", "a"]["matches"]
if b=="real betis":
    GFCa2 = df.loc["Real Betis", "h"]['xG']
    GSCa2 = df.loc["Real Betis", "h"]["xGA"]
    GFTa2 = df.loc["Real Betis", "a"]['xG']
    GSTa2 = df.loc["Real Betis", "a"]["xGA"]
    PCa2 = df.loc["Real Betis", "h"]["matches"]
    PTa2 = df.loc["Real Betis", "a"]["matches"]
if b=="real madrid":
    GFCa2 = df.loc["Real Madrid", "h"]['xG']
    GSCa2 = df.loc["Real Madrid", "h"]["xGA"]
    GFTa2 = df.loc["Real Madrid", "a"]['xG']
    GSTa2 = df.loc["Real Madrid", "a"]["xGA"]
    PCa2 = df.loc["Real Madrid", "h"]["matches"]
    PTa2 = df.loc["Real Madrid", "a"]["matches"]
if b=="real sociedad":
    GFCa2 = df.loc["Real Sociedad", "h"]['xG']
    GSCa2 = df.loc["Real Sociedad", "h"]["xGA"]
    GFTa2 = df.loc["Real Sociedad", "a"]['xG']
    GSTa2 = df.loc["Real Sociedad", "a"]["xGA"]
    PCa2 = df.loc["Real Sociedad", "h"]["matches"]
    PTa2 = df.loc["Real Sociedad", "a"]["matches"]
if b=="valladolid":
    GFCa2 = df.loc["Real Valladolid", "h"]['xG']
    GSCa2 = df.loc["Real Valladolid", "h"]["xGA"]
    GFTa2 = df.loc["Real Valladolid", "a"]['xG']
    GSTa2 = df.loc["Real Valladolid", "a"]["xGA"]
    PCa2 = df.loc["Real Valladolid", "h"]["matches"]
    PTa2 = df.loc["Real Valladolid", "a"]["matches"]
if b=="reims":
    GFCa2 = df.loc["Reims", "h"]['xG']
    GSCa2 = df.loc["Reims", "h"]["xGA"]
    GFTa2 = df.loc["Reims", "a"]['xG']
    GSTa2 = df.loc["Reims", "a"]["xGA"]
    PCa2 = df.loc["Reims", "h"]["matches"]
    PTa2 = df.loc["Reims", "a"]["matches"]
if b=="rennes":
    GFCa2 = df.loc["Rennes", "h"]['xG']
    GSCa2 = df.loc["Rennes", "h"]["xGA"]
    GFTa2 = df.loc["Rennes", "a"]['xG']
    GSTa2 = df.loc["Rennes", "a"]["xGA"]
    PCa2 = df.loc["Rennes", "h"]["matches"]
    PTa2 = df.loc["Rennes", "a"]["matches"]
if b=="roma":
    GFCa2 = df.loc["Roma", "h"]['xG']
    GSCa2 = df.loc["Roma", "h"]["xGA"]
    GFTa2 = df.loc["Roma", "a"]['xG']
    GSTa2 = df.loc["Roma", "a"]["xGA"]
    PCa2 = df.loc["Roma", "h"]["matches"]
    PTa2 = df.loc["Roma", "a"]["matches"]
if b=="huesca":
    GFCa2 = df.loc["SD Huesca", "h"]['xG']
    GSCa2 = df.loc["SD Huesca", "h"]["xGA"]
    GFTa2 = df.loc["SD Huesca", "a"]['xG']
    GSTa2 = df.loc["SD Huesca", "a"]["xGA"]
    PCa2 = df.loc["SD Huesca", "h"]["matches"]
    PTa2 = df.loc["SD Huesca", "a"]["matches"]
if b=="saint etienne":
    GFCa2 = df.loc["Saint-Etienne", "h"]['xG']
    GSCa2 = df.loc["Saint-Etienne", "h"]["xGA"]
    GFTa2 = df.loc["Saint-Etienne", "a"]['xG']
    GSTa2 = df.loc["Saint-Etienne", "a"]["xGA"]
    PCa2 = df.loc["Saint-Etienne", "h"]["matches"]
    PTa2 = df.loc["Saint-Etienne", "a"]["matches"]
if b=="sampdoria":
    GFCa2 = df.loc["Sampdoria", "h"]['xG']
    GSCa2 = df.loc["Sampdoria", "h"]["xGA"]
    GFTa2 = df.loc["Sampdoria", "a"]['xG']
    GSTa2 = df.loc["Sampdoria", "a"]["xGA"]
    PCa2 = df.loc["Sampdoria", "h"]["matches"]
    PTa2 = df.loc["Sampdoria", "a"]["matches"]
if b=="sassuolo":
    GFCa2 = df.loc["Sassuolo", "h"]['xG']
    GSCa2 = df.loc["Sassuolo", "h"]["xGA"]
    GFTa2 = df.loc["Sassuolo", "a"]['xG']
    GSTa2 = df.loc["Sassuolo", "a"]["xGA"]
    PCa2 = df.loc["Sassuolo", "h"]["matches"]
    PTa2 = df.loc["Sassuolo", "a"]["matches"]
if b=="schalke":
    GFCa2 = df.loc["Schalke 04", "h"]['xG']
    GSCa2 = df.loc["Schalke 04", "h"]["xGA"]
    GFTa2 = df.loc["Schalke 04", "a"]['xG']
    GSTa2 = df.loc["Schalke 04", "a"]["xGA"]
    PCa2 = df.loc["Schalke 04", "h"]["matches"]
    PTa2 = df.loc["Schalke 04", "a"]["matches"]
if b=="sevilla":
    GFCa2 = df.loc["Sevilla", "h"]['xG']
    GSCa2 = df.loc["Sevilla", "h"]["xGA"]
    GFTa2 = df.loc["Sevilla", "a"]['xG']
    GSTa2 = df.loc["Sevilla", "a"]["xGA"]
    PCa2 = df.loc["Sevilla", "h"]["matches"]
    PTa2 = df.loc["Sevilla", "a"]["matches"]
if b=="sheffield":
    GFCa2 = df.loc["Sheffield United", "h"]['xG']
    GSCa2 = df.loc["Sheffield United", "h"]["xGA"]
    GFTa2 = df.loc["Sheffield United", "a"]['xG']
    GSTa2 = df.loc["Sheffield United", "a"]["xGA"]
    PCa2 = df.loc["Sheffield United", "h"]["matches"]
    PTa2 = df.loc["Sheffield United", "a"]["matches"]
if b=="southampton":
    GFCa2 = df.loc["Southampton", "h"]['xG']
    GSCa2 = df.loc["Southampton", "h"]["xGA"]
    GFTa2 = df.loc["Southampton", "a"]['xG']
    GSTa2 = df.loc["Southampton", "a"]["xGA"]
    PCa2 = df.loc["Southampton", "h"]["matches"]
    PTa2 = df.loc["Southampton", "a"]["matches"]
if b=="spezia":
    GFCa2 = df.loc["Spezia", "h"]['xG']
    GSCa2 = df.loc["Spezia", "h"]["xGA"]
    GFTa2 = df.loc["Spezia", "a"]['xG']
    GSTa2 = df.loc["Spezia", "a"]["xGA"]
    PCa2 = df.loc["Spezia", "h"]["matches"]
    PTa2 = df.loc["Spezia", "a"]["matches"]
if b=="strasbourg":
    GFCa2 = df.loc["Strasbourg", "h"]['xG']
    GSCa2 = df.loc["Strasbourg", "h"]["xGA"]
    GFTa2 = df.loc["Strasbourg", "a"]['xG']
    GSTa2 = df.loc["Strasbourg", "a"]["xGA"]
    PCa2 = df.loc["Strasbourg", "h"]["matches"]
    PTa2 = df.loc["Strasbourg", "a"]["matches"]
if b=="torino":
    GFCa2 = df.loc["Torino", "h"]['xG']
    GSCa2 = df.loc["Torino", "h"]["xGA"]
    GFTa2 = df.loc["Torino", "a"]['xG']
    GSTa2 = df.loc["Torino", "a"]["xGA"]
    PCa2 = df.loc["Torino", "h"]["matches"]
    PTa2 = df.loc["Torino", "a"]["matches"]
if b=="tottenham":
    GFCa2 = df.loc["Tottenham", "h"]['xG']
    GSCa2 = df.loc["Tottenham", "h"]["xGA"]
    GFTa2 = df.loc["Tottenham", "a"]['xG']
    GSTa2 = df.loc["Tottenham", "a"]["xGA"]
    PCa2 = df.loc["Tottenham", "h"]["matches"]
    PTa2 = df.loc["Tottenham", "a"]["matches"]
if b=="udinese":
    GFCa2 = df.loc["Udinese", "h"]['xG']
    GSCa2 = df.loc["Udinese", "h"]["xGA"]
    GFTa2 = df.loc["Udinese", "a"]['xG']
    GSTa2 = df.loc["Udinese", "a"]["xGA"]
    PCa2 = df.loc["Udinese", "h"]["matches"]
    PTa2 = df.loc["Udinese", "a"]["matches"]
if b=="union berlin":
    GFCa2 = df.loc["Union Berlin", "h"]['xG']
    GSCa2 = df.loc["Union Berlin", "h"]["xGA"]
    GFTa2 = df.loc["Union Berlin", "a"]['xG']
    GSTa2 = df.loc["Union Berlin", "a"]["xGA"]
    PCa2 = df.loc["Union Berlin", "h"]["matches"]
    PTa2 = df.loc["Union Berlin", "a"]["matches"]
if b=="valencia":
    GFCa2 = df.loc["Valencia", "h"]['xG']
    GSCa2 = df.loc["Valencia", "h"]["xGA"]
    GFTa2 = df.loc["Valencia", "a"]['xG']
    GSTa2 = df.loc["Valencia", "a"]["xGA"]
    PCa2 = df.loc["Valencia", "h"]["matches"]
    PTa2 = df.loc["Valencia", "a"]["matches"]
if b=="verona":
    GFCa2 = df.loc["Verona", "h"]['xG']
    GSCa2 = df.loc["Verona", "h"]["xGA"]
    GFTa2 = df.loc["Verona", "a"]['xG']
    GSTa2 = df.loc["Verona", "a"]["xGA"]
    PCa2 = df.loc["Verona", "h"]["matches"]
    PTa2 = df.loc["Verona", "a"]["matches"]
if b=="stuttgart":
    GFCa2 = df.loc["VfB Stuttgart", "h"]['xG']
    GSCa2 = df.loc["VfB Stuttgart", "h"]["xGA"]
    GFTa2 = df.loc["VfB Stuttgart", "a"]['xG']
    GSTa2 = df.loc["VfB Stuttgart", "a"]["xGA"]
    PCa2 = df.loc["VfB Stuttgart", "h"]["matches"]
    PTa2 = df.loc["VfB Stuttgart", "a"]["matches"]
if b=="villareal":
    GFCa2 = df.loc["Villarreal", "h"]['xG']
    GSCa2 = df.loc["Villarreal", "h"]["xGA"]
    GFTa2 = df.loc["Villarreal", "a"]['xG']
    GSTa2 = df.loc["Villarreal", "a"]["xGA"]
    PCa2 = df.loc["Villarreal", "h"]["matches"]
    PTa2 = df.loc["Villarreal", "a"]["matches"]
if b=="werder brema":
    GFCa2 = df.loc["Werder Bremen", "h"]['xG']
    GSCa2 = df.loc["Werder Bremen", "h"]["xGA"]
    GFTa2 = df.loc["Werder Bremen", "a"]['xG']
    GSTa2 = df.loc["Werder Bremen", "a"]["xGA"]
    PCa2 = df.loc["Werder Bremen", "h"]["matches"]
    PTa2 = df.loc["Werder Bremen", "a"]["matches"]
if b=="west bromwich":
    GFCa2 = df.loc["West Bromwich Albion", "h"]['xG']
    GSCa2 = df.loc["West Bromwich Albion", "h"]["xGA"]
    GFTa2 = df.loc["West Bromwich Albion", "a"]['xG']
    GSTa2 = df.loc["West Bromwich Albion", "a"]["xGA"]
    PCa2 = df.loc["West Bromwich Albion", "h"]["matches"]
    PTa2 = df.loc["West Bromwich Albion", "a"]["matches"]
if b=="west ham":
    GFCa2 = df.loc["West Ham", "h"]['xG']
    GSCa2 = df.loc["West Ham", "h"]["xGA"]
    GFTa2 = df.loc["West Ham", "a"]['xG']
    GSTa2 = df.loc["West Ham", "a"]["xGA"]
    PCa2 = df.loc["West Ham", "h"]["matches"]
    PTa2 = df.loc["West Ham", "a"]["matches"]
if b=="wolfsburg":
    GFCa2 = df.loc["Wolfsburg", "h"]['xG']
    GSCa2 = df.loc["Wolfsburg", "h"]["xGA"]
    GFTa2 = df.loc["Wolfsburg", "a"]['xG']
    GSTa2 = df.loc["Wolfsburg", "a"]["xGA"]
    PCa2 = df.loc["Wolfsburg", "h"]["matches"]
    PTa2 = df.loc["Wolfsburg", "a"]["matches"]
if b=="wolverhampton":
    GFCa2 = df.loc["Wolverhampton Wanderers", "h"]['xG']
    GSCa2 = df.loc["Wolverhampton Wanderers", "h"]["xGA"]
    GFTa2 = df.loc["Wolverhampton Wanderers", "a"]['xG']
    GSTa2 = df.loc["Wolverhampton Wanderers", "a"]["xGA"]
    PCa2 = df.loc["Wolverhampton Wanderers", "h"]["matches"]
    PTa2 = df.loc["Wolverhampton Wanderers", "a"]["matches"]

# ---------------------------------- GOAL MEAN ------------------------------------------
x = ((GFCa1/PCa1) + (GSTa2/PTa2))/2 

y = ((GSCa1/PCa1) + (GFTa2/PTa2))/2

#------------------------ POISSON home goals --------------------------------------

# 0 
probx1 = poisson.pmf(0,x)

# 1 
probx2 = poisson.pmf(1,x)

# 2 
probx3 = poisson.pmf(2,x)

# 3 
probx4 = poisson.pmf(3,x)

# 4 
probx5 = poisson.pmf(4,x)

# 5 
probx6 = poisson.pmf(5,x)

# 6 
probx7 = poisson.pmf(6,x)

#------------------------POISSON away goals-------------------------------
# 0 
proby1 = poisson.pmf(0,y)

# 1 
proby2 = poisson.pmf(1,y)

# 2 
proby3 = poisson.pmf(2,y)

# 3 
proby4 = poisson.pmf(3,y)

# 4 
proby5 = poisson.pmf(4,y)

# 5 
proby6 = poisson.pmf(5,y)

# 6 
proby7 = poisson.pmf(6,y)

#-----------------------------POISSON combinations---------------------------

# 0 - 0
probx1y1 = probx1*proby1


# 1 - 0
probx2y1 = probx2*proby1


# 2 - 0
probx3y1 = probx3*proby1


# 3 - 0
probx4y1 = probx4*proby1


# 4 - 0
probx5y1 = probx5*proby1

# 5 - 0
probx6y1 = probx6*proby1

# 6 - 0
probx7y1 = probx7*proby1

# 1 - 1
probx2y2 = probx2*proby2

# 2 - 1
probx3y2 = probx3*proby2

# 3 - 1
probx4y2 = probx4*proby2

# 4 - 1
probx5y2 = probx5*proby2

# 5 - 1
probx6y2 = probx6*proby2

# 6 - 1
probx7y2 = probx7*proby2

# 1 - 2
probx2y3 = probx2*proby3

# 2 - 2
probx3y3 = probx3*proby3

# 3 - 2
probx4y3 = probx4*proby3

# 4 - 2
probx5y3 = probx5*proby3

# 5 - 2
probx6y3 = probx6*proby3

# 6 - 2
probx7y3 = probx7*proby3

# 1 - 3
probx2y4 = probx2*proby4

# 2 - 3
probx3y4 = probx3*proby4

# 3 - 3
probx4y4 = probx4*proby4

# 4 - 3
probx5y4 = probx5*proby4

# 5 - 3
probx6y4 = probx6*proby4

# 6 - 3
probx7y4 = probx7*proby4

# 1 - 4
probx2y5 = probx2*proby5

# 2 - 4
probx3y5 = probx3*proby5

# 3 - 4
probx4y5 = probx4*proby5

# 4 - 4
probx5y5 = probx5*proby5

# 5 - 4
probx6y5 = probx6*proby5

# 6 - 4
probx7y5 = probx7*proby5


# 1 - 5
probx2y6 = probx2*proby6

# 2 - 5
probx3y6 = probx3*proby6

# 3 - 5
probx4y6 = probx4*proby6

# 4 - 5
probx5y6 = probx5*proby6

# 5 - 5
probx6y6 = probx6*proby6

# 6 - 5
probx7y6 = probx7*proby6

# 1 - 6
probx2y7 = probx2*proby7

# 2 - 6
probx3y7 = probx3*proby7

# 3 - 6
probx4y7 = probx4*proby7

# 4 - 6
probx5y7 = probx5*proby7

# 5 - 6
probx6y7 = probx6*proby7

# 6 - 6
probx7y7 = probx7*proby7

# 0 - 1
probx1y2 = probx1*proby2

# 0 - 2
probx1y3 = probx1*proby3

# 0 - 3
probx1y4 = probx1*proby4

# 0 - 4
probx1y5 = probx1*proby5

# 0 - 5
probx1y6 = probx1*proby6

# 0 - 6
probx1y7 = probx1*proby7

#1
prob1 = probx2y1+probx3y1+probx4y1+probx5y1+probx6y1+probx7y1+probx3y2+probx4y2+probx5y2+probx6y2+probx7y2+probx4y3+probx5y3+probx6y3+probx7y3+probx5y4+probx6y4+probx7y4+probx6y5+probx7y5+probx7y6
print("Home team win probability:",(round(prob1*100)))
if prob1 >= 0.60:
    print('Home team have a great probability to win when >60%')
print("------------------------------")

#X
probx = probx1y1+probx2y2+probx3y3+probx4y4+probx5y5+probx6y6+probx7y7
print("Draw probability:",(round(probx*100)))
print("------------------------------")

#2
prob2 = probx1y2+probx1y3+probx1y4+probx1y5+probx1y6+probx1y7+probx2y3+probx2y4+probx2y5+probx2y6+probx2y7+probx3y4+probx3y5+probx3y6+probx3y7+probx4y5+probx4y6+probx4y7+probx5y6+probx5y7+probx6y7
print("Away team win probability:",(round(prob2*100)))
if prob2 >= 0.55:
    print('Away team have a great probability to win when >55%')
print("------------------------------")

#--------------------------------Over 1,5
probover1 = probx3y1+probx4y1+probx5y1+probx6y1+probx7y1+probx2y2+probx3y2+probx4y2+probx5y2+probx6y2+probx7y2+probx2y3+probx3y3+probx4y3+probx5y3+probx6y3+probx7y3+probx2y4+probx3y4+probx4y4+probx5y4+probx6y4+probx7y4+probx2y5+probx3y5+probx4y5+probx5y5+probx6y5+probx7y5+probx1y6+probx2y6+probx3y6+probx4y6+probx5y6+probx6y6+probx7y6+probx1y7+probx2y7+probx3y7+probx4y7+probx5y7+probx6y7+probx7y7+probx1y3+probx1y4+probx1y5+probx1y6+probx1y7
print('Over 1,5:',round(probover1*100))
if probover1 >= 0.75:
    print('Great probability of 1,5 when >75%')
print("------------------------------")

#------------------------------Over 2,5
probover2 = probx4y1+probx5y1+probx6y1+probx7y1+probx3y2+probx4y2+probx5y2+probx6y2+probx7y2+probx2y3+probx3y3+probx4y3+probx5y3+probx6y3+probx7y3+probx2y4+probx3y4+probx4y4+probx5y4+probx6y4+probx7y4+probx2y5+probx3y5+probx4y5+probx5y5+probx6y5+probx7y5+probx2y6+probx3y6+probx4y6+probx5y6+probx6y6+probx7y6+probx2y7+probx3y7+probx4y7+probx5y7+probx6y7+probx7y7+probx1y4+probx1y5+probx1y6+probx1y7
print('Over 2,5:',round(probover2*100))
if probover2 >= 0.65:
    print('Great probability of 2,5 when >65%')
print("------------------------------")

#----------------------------------Over 3,5
probover3 = probx5y1+probx6y1+probx7y1+probx4y2+probx5y2+probx6y2+probx7y2+probx3y3+probx4y3+probx5y3+probx6y3+probx7y3+probx2y4+probx3y4+probx4y4+probx5y4+probx6y4+probx7y4+probx2y5+probx3y5+probx4y5+probx5y5+probx6y5+probx7y5+probx2y6+probx3y6+probx4y6+probx5y6+probx6y6+probx7y6+probx2y7+probx3y7+probx4y7+probx5y7+probx6y7+probx7y7
print('Over 3,5:',round(probover3*100))
print("------------------------------")

#-----------------------------------Under 1,5
probunder1 = probx1y1+probx2y1+probx1y2
print('Under 1,5:',round(probunder1*100))
print("------------------------------")

#---------------------------------Under 2,5
probunder2 = probx1y1+probx2y1+probx3y1+probx2y2+probx1y2+probx1y3
print('Under 2,5:',round(probunder2*100))
if probunder2 >= 0.65:
    print('Great probability of 2,5 when >65%')
print("------------------------------")

#--------------------------------------Under 3,5
probunder3 = probx1y1+probx2y1+probx3y1+probx4y1+probx2y2+probx3y2+probx2y3+probx1y2+probx1y3+probx1y4
print('Under 3,5:',round(probunder3*100))
if probunder3 >= 0.75:
    print('Great probability of 3,5 when >75%')
    
#--------------------------------------Graph
names =["1","x","2"]
values=[prob1, probx, prob2]
plt.bar(names, values)
plt.xlabel("Results")
plt.ylabel("Probability")

names =["U 3,5","U 2,5","O 2,5","O 1,5"]
values=[probunder3, probunder2, probover2, probover1]
plt.bar(names, values)
plt.ylabel("Probability")
