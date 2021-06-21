import os


import numpy as np
from sklearn.decomposition import NMF
import pickle


cwd =os.getcwd()



# NMF Model
R=df_ratings.drop('timestamp', axis=1)
R_wide = pd.pivot_table(R, values='rating', index=['userId'], columns= ['movieId'])

R_wide.to_csv("r_wide_matrix.csv")

nmf = NMF(n_components=300)






#save the model
with open('nmf_model.pkl','wb') as file:
    pickle.dump(nmf,file)
