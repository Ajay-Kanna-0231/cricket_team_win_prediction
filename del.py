import pandas as pd
data = pd.read_csv(r"C:\Users\Ajay Kanna\Desktop\all projects web dev\cricket_team_win_prediction\35320_2_allround_career_averages.csv")
data_cleaned = data.loc[:, ~data.columns.str.contains('^Unnamed')]

# Print the remaining columns to verify
print(data_cleaned.columns)
print(data_cleaned)