import pandas as pd
import numpy as np

df = pd.read_csv('2021_IN_Region_Mobility_Report.csv', parse_dates=['date'], infer_datetime_format=False)
df = df.iloc[:, np.r_[ 0:4, 8:15]]

cols = df.columns
colm = dict()

for i in range(len(cols)):
    if i > 4:
        name = cols[i].split(sep ='_')
        if i < 7:
            s = ''
            for j in range(3):
                s += name[j]+' '
            s = s.rstrip()
            colm[cols[i]] = s
        else:
            colm[cols[i]] = name[0]
    
    else:
        colm[cols[i]] = cols[i]


df = df.rename(columns=colm)
df = df[df["sub_region_2"].notna()]

cols = df.columns

def group_data(data):
    col = data.columns
    cols = {i:[] for i in col}
    loc = data.iloc[0, 3]
    loc_li = []
    ind = 0
    df_li = []

    while ind < len(data):
        df_loc = pd.DataFrame(data = cols)
        loc_li.append(loc)

        while (data.iloc[ind, 3] == loc):
            df_loc.loc[len(df_loc)] = data.iloc[ind, :]
            ind += 1
            if ind == len(data):
                break
        
        if ind != len(data):
            loc = data.iloc[ind, 3]
        df_li.append(df_loc)

    for i in range(len(df_li)):
        df_li[i] = df_li[i].groupby(pd.Grouper(key= "date", freq = "3M")).mean()
        df_li[i] = df_li[i].reset_index(drop=False)
        df_li[i]["sub region"] = [loc_li[i]]*5

    out_data = pd.concat(df_li, ignore_index=True)

    return out_data

data = group_data(df)
data.to_csv('2021_Mobility.csv', index = False)