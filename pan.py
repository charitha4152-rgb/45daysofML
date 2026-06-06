import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

df=pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

team=df.groupby('Team')
print(team.first())

aggregated_data = df.groupby(['Team', 'Position']).agg(
    total_salarys=('Salary', 'sum'),
    average_salarys=('Salary', 'mean'),
    player_count=('Name', 'count')
)

print(aggregated_data)