import pickle
import os

Pkl_Filename = "Pickle_RL_Model.pkl"

with open(Pkl_Filename, 'rb') as file:  
    Pickled_LR_Model = pickle.load(file)

print(Pickled_LR_Model)
