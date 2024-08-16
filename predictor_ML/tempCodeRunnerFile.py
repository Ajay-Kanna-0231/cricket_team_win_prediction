from espncricinfo.player import Player
from espncricinfo.match import Match
import pandas as pd

for i in range(62435, 67523):
    m = Match(f'{i}')
    with open(r"C:\Users\Ajay Kanna\Desktop\all projects web dev\cricket_team_win_prediction\predictor_ML\all_match_desc.txt",'a') as f:
        f.write(f"{m.description}, {i}" + "\n")
