import functions
import pandas as pd

#df_num[df_num['AFREGNING']=='dør']

#type(df_num.loc[2,'AFREGNING'])
#print(pd.isna(x))
#print(re.search("[^0-9]",x))
#print(type('123')==str)

# %%
#df_2 = df[[' ', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 5',
    #   'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9']]
#df_2.columns=df_2.iloc[0]

df=pd.read_csv(r"C:\Users\mikke\Documents\Job\Drop_Inn_tal\Kopi af Copy of MASTER DOKUMENT 2025 - Sheet1.csv", header=0,dtype=str)
df=df.drop(columns=['@dropdown','Unnamed: 21','Unnamed: 22','#NAME?'])

df=functions.make_num(df,'AFREGNING','ANDET')
df[df['ANDET']=='dør']
#print(df_int.columns)

#df_int['AFREGNING'].div(df_int['PUBLIKUM'])

# %%
df=functions.make_num(df,'PUBLIKUM','ANDET')
df

# %%
df=functions.make_num(df,'PRIS','ANDET')
df


# %%
df['A/P']=df['AFREGNING'].div(df['PUBLIKUM'])
df['A/P']

# %%
pris_dick=functions.sub_dick(df,'PRIS')
pris_dick[1]

# %%
orig_dick=functions.sub_dick(df,'original') 
orig_dick[1]


# %%
event_dick=functions.sub_dick(df,'EVENT')
event_dick[1]

# %%
event_dick[0]['x'] #Når der er lavet et event

# %%
ig_dick=functions.sub_dick(df,'IG POST')
print(ig_dick[1])
ig_dick[0]['x']

# %%
press_dick=functions.sub_dick(df,'INDHOLD PRESS')
press_dick

# %%
genre_dick=functions.sub_dick(df,'GENRE')
genre_dick