import os


import json



cwd =os.getcwd()



# Creating a dictionary of the movie titles and id
df_movies.drop(['genres'], axis=1, inplace=True)


with open('movies_dict.json', 'w') as myfile:
    json.dump(movies_dict, myfile, indent=4)