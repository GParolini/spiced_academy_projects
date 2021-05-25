import os
from pathlib import Path
import pandas as pd
import json


#Reading users and movies data
cwd =os.getcwd()
pdir = os.path.dirname(cwd)
df_movies = pd.read_csv(os.path.join(pdir, 'data','movies.csv'))

# Creating a dictionary of the movie titles and id
df_movies.drop(['genres'], axis=1, inplace=True)
movies_dict= dict(df_movies.values)

with open('movies_dict.json', 'w') as myfile:
    json.dump(movies_dict, myfile, indent=4)
