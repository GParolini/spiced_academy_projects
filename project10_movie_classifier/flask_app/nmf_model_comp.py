import os
from pathlib import Path
import pandas as pd
import numpy as np
from sklearn.decomposition import NMF
import pickle

#Reading users and movies data
cwd =os.getcwd()
pdir = os.path.dirname(cwd)
df_ratings = pd.read_csv(os.path.join(pdir, 'data','ratings.csv'))

# NMF Model
R=df_ratings.drop('timestamp', axis=1)
R_wide = pd.pivot_table(R, values='rating', index=['userId'], columns= ['movieId'])
R_wide = R_wide.fillna(0)
R_wide.to_csv("r_wide_matrix.csv")

nmf = NMF(n_components=300)
nmf.fit(R_wide)
Q = nmf.components_
P = nmf.transform(R_wide)
P = pd.DataFrame(nmf.transform(R_wide), index=R_wide.index)
R_wide_hat = pd.DataFrame(np.dot(P, Q), columns=R_wide.columns, index=R_wide.index)

#save the model
with open('nmf_model.pkl','wb') as file:
    pickle.dump(nmf,file)

