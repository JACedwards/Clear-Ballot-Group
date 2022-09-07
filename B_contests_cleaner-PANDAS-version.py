import pandas as pd

cts = pd.read_csv('contests.csv')

cts = cts.drop_duplicates(subset="ContestName",keep='first')

cts.to_csv('contests_cleaned.csv',index=False)

