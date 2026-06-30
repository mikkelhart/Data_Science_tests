# %%
import pandas as pd

# %%
df=pd.read_csv(r"C:\Users\mikke\Documents\Job\Drop_Inn_tal\Kopi af Copy of MASTER DOKUMENT 2025 - Sheet1.csv", header=0,dtype=str)
df=df.drop(columns=['@dropdown','Unnamed: 21','Unnamed: 22','#NAME?'])

# %%
import numpy as np
import re

# %%
df['ANDET']=np.nan

#print(df.columns)


# %%
#Til næste gang: Jeg skal lave denne funktion, så den laver en 
#ny kolonne, som indikerer, hvornår der blev afregnet med 'dør'
#eller variationer deraf, og som så fjerner stringen 'dør'. 
def make_num(DF:pd.DataFrame, col:str,bincol:str):
    for i in range(len(DF))[1:-1]:
        
        #hvis der er andre symboler end tal OG værdien ikke er NaN
        if type(DF.loc[i,col])==str:
            if re.search("[^0-9]",DF.loc[i,col])==None: 
                DF.loc[i,col]=float(DF.loc[i,col]) #så lav indgangen om til et tal
            else:
                #det her er ikke god skik, men jeg kan ikke huske, hvordan man indsætter en standard parameter
                DF.loc[i,bincol]=DF.loc[i,col]
                DF.loc[i,col]=1    
        else:
            pass #ellers lad det være
    return DF

# %%

# %%
def sub_dick(DF:pd.DataFrame,column:str):
    
    l_o_c=DF[f'{column}'].unique().tolist()
    col_dick = {}
    for value in l_o_c:
        c_df=DF[DF[f'{column}']==value]
    
    #p_df=g_df['PUBLIKUM']     
    #p_list=p_df.values.tolist()
    #print(p_list)
    
        col_dick[value]=c_df
    return [col_dick,l_o_c]





