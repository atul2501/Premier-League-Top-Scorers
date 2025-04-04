#import 
from bs4 import BeautifulSoup
import pandas as pd

url='https://www.bbc.com/sport/football/premier-league/top-scorers'  #

player_names=[]
player_teams=[]
player_goals=[]
player_assists=[]
player_playeds=[]
Goals_per_90=[]
mins_per_Goals=[]
Goal_Conversions=[]
shot_Accuracys=[]
total_shots=[]

try:
    response=requests.get(url)
    response.raise_for_status()
except Exception in e:
    print(e)
else:
    soup=BeautifulSoup(response.content, 'html.parser')
    players=soup.find('tbody').find_all('tr', class_='ssrcss-dhlz6k-TableRowBody e1icz100')
    for player in players:
        player_name=player.find('div',class_='ssrcss-m6ah29-PlayerName e1n8xy5b1').get_text(strip=True)
        player_team=player.find('div',class_='ssrcss-qvpga1-TeamsSummary e1n8xy5b0').get_text(strip=True)
        player_goal=int(player.find('div',class_='ssrcss-8k20kk-CellWrapper ef9ipf0').get_text(strip=True))
        stats=player.find_all('div',class_='ssrcss-150z8d-CellWrapper ef9ipf0')
        player_assist=int(stats[0].get_text(strip=True))
        player_played=int(stats[2].get_text(strip=True))
        goal_90=stats[4].get_text(strip=True)
        mins_per_Goal=stats[6].get_text(strip=True)
        total_shot=int(stats[7].get_text(strip=True))
        Goal_Conversion=stats[8].get_text(strip=True)
        sort_Accuracy=stats[-1].get_text(strip=True)
                
        player_names.append(player_name)
        player_teams.append(player_team)
        player_playeds.append(player_played)
        player_goals.append(player_goal)
        player_assists.append(player_assist)
        Goals_per_90.append(goal_90)
        mins_per_Goals.append(mins_per_Goal)
        total_shots.append(total_shot)
        Goal_Conversions.append(Goal_Conversion)
        shot_Accuracys.append(sort_Accuracy)


data={
        'Name': player_names,
        'Goals': player_goals,
        'Assists': player_assists,
        'Played': player_playeds,
        'Goals per 90': Goals_per_90,
        'Mins per Goal': mins_per_Goals,
        'Total Shots': total_shots,
        'Goal Conversion': Goal_Conversions,
        'Shot Accuracy': shot_Accuracys
        
    }
df=pd.DataFrame(data)

df.head()
