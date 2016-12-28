import pandas as pd
#Import the dataframe
data = pd.read_html('http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2')[0]
#Changing the names of columns

data.columns = ['RK', 'PLAYER', 'TEAM', 'GP', 'G', 'A', 'PTS', '+/-', 'PIM', 'PTS/G', 'SOG', 'PCT', 'GWG', 'PPG', 'PPA', 'SHG', 'SHA']

df = data

df = df.dropna(axis=0, thresh=(len(df.columns)-4))

df= df.drop(labels = 'RK',axis=1)


#df[['col2','col3']] = df[['col2','col3']].apply(pd.to_numeric)

df[['GP', 'G', 'A', 'PTS', '+/-', 
    'PIM', 'PTS/G', 'SOG','PCT', 'GWG', 'PPG', 'PPA', 'SHG', 'SHA']] = df[[
    'GP', 'G', 'A', 'PTS', '+/-', 'PIM', 'PTS/G', 'SOG','PCT', 'GWG', 'PPG', 'PPA', 'SHG', 'SHA']].apply(pd.to_numeric, errors='coerce')