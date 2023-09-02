import pandas as pd
import pickle


#### lectura de archivo .csv ####

data_csv = pd.read_csv("data/ames.csv")

data_csv.info()

pd.set_option('display.max_columns', 6)
data_csv.head(5)

data_csv.describe()


#### lectura de archivo .txt ####

ames_txt = pd.read_csv("data/ames.txt", delimiter = ";")
ames_txt.head(3)


#### lectura de archivo .xlsx ####

ames_xlsx = pd.read_excel("data/ames.xlsx")
ames_xlsx.head(3)


#### lectura de archivo .pkl ####

## escritura
with open('data/ames.pkl', 'wb') as f:
    pickle.dump(ames_xlsx, f, pickle.HIGHEST_PROTOCOL)

## lectura
with open('data/ames.pkl', 'rb') as f:
    ames_pkl = pickle.load(f)

ames_pkl.head(3)










