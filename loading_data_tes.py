import pandas as pd

DB_path_basic='Db/DataSet_basic.csv'
df1= pd.read_csv(DB_path_basic, sep='\t',header=[0,1], index_col=0)
df1.columns