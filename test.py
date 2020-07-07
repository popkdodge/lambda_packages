import k_pack as kp
import pandas as pd

df = pd.read_csv("test.csv") 
mycols = ["Matching time","Alignment time"]
print("\nBEFORE\n")
print(df[mycols[0]].head()) 
for colname in mycols:
    kp.convert_time(df[colname])
print("\nAFTER\n")    
print(df[mycols[0]].head())