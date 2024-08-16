from espncricinfo.player import Player
from espncricinfo.match import Match
import pandas as pd
data = pd.read_csv(r"C:\Users\Ajay Kanna\Desktop\all projects web dev\cricket_team_win_prediction\data_base.csv")

def help(tmp, arr, j):
    for i in range(len(arr)):
        #print(m.team_1_players[i]['object_id'])
        if arr[i]['object_id'] not in data['ID'].values:
            #print(arr[i]['object_id'])
            return False
        else:
            #print(arr[i]['object_id'])
            tmp[f"team_{j}_{i}"] = arr[i]['object_id']
    return True

results = []
# over: 62387: 64221
# 65000
for i in range(66510, 67523):
    try:
        m = Match(f'{i}')
        tmp = {}
        tmp["Match_ID"] = i
        tmp["Team_won"] = m.match_winner
        print(m.description, i)
        if 'ODI' in m.description and int(m.description.strip()[-4:]) > 1978:
            if not help(tmp, m.team_1_players, 1): continue
            if not help(tmp, m.team_2_players, 2): continue 
        else: continue
        results.append(tmp)
        print(i, m.description)
    except Exception as e:
        print(f"NO, {i}")

results_df = pd.DataFrame(results)
results_df.to_csv(r"C:\Users\Ajay Kanna\Desktop\all projects web dev\cricket_team_win_prediction\matches_player_info.csv", index=False)

'''m = Match('65000')
if 'ODI' in m.description and int(m.description.strip()[-4:]) > 1978:
    print(m.description)
    print(len(m.team_1_players))'''

