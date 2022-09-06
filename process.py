import csv
import pandas as pd

df = pd.read_csv('dwarf_stars.csv')
df = df.dropna()

df['Mass'] = df['Mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
df['Mass'] = df['Mass']*0.102763
df['Radius'] = df['Radius']*0.000954588

df.to_csv("unit_converted_stars.csv")
