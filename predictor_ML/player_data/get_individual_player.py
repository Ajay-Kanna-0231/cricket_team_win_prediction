from espncricinfo.player import Player
import pandas as pd

# Load the data from the CSV file
data = pd.read_csv(r"C:\Users\Ajay Kanna\Desktop\all projects web dev\cricket_team_win_prediction\cricket_data.csv")

# Open a file to log errors in append mode
with open("error_log.txt", "a") as error_file:
    for i in range(33, len(data["ID"])):
        try:
            # Create Player object
            p = Player(f'{data["ID"][i]}')
            print(p.name, data["ID"][i], i)
            
            # Get career averages and save to file
            file_name = rf'C:\Users\Ajay Kanna\Desktop\all projects web dev\cricket_team_win_prediction\predictor_ML\player_data\all_players_data\{data["ID"][i]}.csv'
            career_averages = p.get_career_averages(file_name=file_name, match_format=2)
        
        except Exception as e:
            # Log errors to the file
            error_message = f"Player ID {data['ID'][i]} at index {i}: {e}\n"
            error_file.write(error_message)
