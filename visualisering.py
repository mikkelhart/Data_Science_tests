import matplotlib.pylab as plt
import seaborn as sns
plt.style.use("ggplot")
import underdelingerne as undd
import functions as fcts
import pandas as pd
# %%

#df=pd.read_csv(r"C:\Users\mikke\Documents\Job\Drop_Inn_tal\Kopi af Copy of MASTER DOKUMENT 2025 - Sheet1.csv", header=0,dtype=str)
#df=df.drop(columns=['@dropdown','Unnamed: 21','Unnamed: 22','#NAME?'])

data=undd.df[pd.isnull(undd.df['A/P'])==False]
data.index

# %%
gnms_ratio=sum(data['A/P'])/len(data)
gnsm_pub=sum(data['PUBLIKUM'])/len(data)
gnms_afr=sum(data['AFREGNING'])/len(data)
print(gnms_afr,gnsm_pub,gnms_ratio,gnms_afr/gnsm_pub)

# %%
print(max(data['AFREGNING']),max(data['PUBLIKUM']))
14430/175

# %%


# %%
plt.plot(data['PUBLIKUM'])

# %%
#gnms_tabel_genre = pd.DataFrame(data=np.nan,index=genre_dick[1],columns=['AFREGNING','PUBLIKUM','A/P'])
"""Her er dep_col1 det kolonnenavn, som skal forklare, altså f.eks. 
genre, mens indep_col er den kolonne, vi er interesserede i at 
forklare, som publikumsantal. """
def gnms(DF:pd.DataFrame,liste1:list,dep_col1:str,indep_col1:str, liste2=[],liste3=[],indep_col2="",indep_col3="",dep_col2="",dep_col3=""):
    gnms_pik={}
    for val in liste1:
        sub_DF1 = DF[DF[indep_col1]==val]
        if len(sub_DF1)==0:
            gnms_pik[val]=[0,0,0,0]
        else:
            gnms1=sum(sub_DF1[dep_col1])/len(sub_DF1)
            s=0
            for i in sub_DF1.index:
                s+=sub_DF1.loc[i,dep_col1]**2 #bemærk, at vi skal estimere tal
            var1=s/len(sub_DF1)-gnms1**2
            M=max(sub_DF1[dep_col1])
            m=min(sub_DF1[dep_col1])
            gnms_pik[val]=[gnms1,var1,M,m,len(sub_DF1)]
    eff=['Mean', 'Var', 'Max', 'Min','Len']
    gnms_df=pd.DataFrame.from_dict(gnms_pik)
    gnms_df=gnms_df.transpose()
    gnms_df.columns=eff
    return gnms_df


# %%
genre_gnms=gnms(data,undd.genre_dick[1],'PUBLIKUM','GENRE')

genre_index={}
for i in range(len(undd.genre_dick[1]))[1:-1]:
    genre_index[i]=undd.genre_dick[1][i]

genre_index

# %%
genre_gnms=genre_gnms.reset_index()



# %%
plt.plot(genre_gnms['Mean'])

# %%
plt.plot(genre_gnms['Var'])

# %%
ig_gnms=gnms(data,undd.ig_dick[1],'PUBLIKUM','IG POST')
ig_gnms

# %%
pris_gnms=gnms(data,undd.pris_dick[1],'PUBLIKUM','PRIS')
pris_gnms

# %%
