import numpy as np
import pandas as pd 
from kmodes.kmodes import KModes
import string

#récupérer et transformer les données
df = pd.read_csv('/features_with_plan_france.csv',';')
df = df.drop("Unnamed: 0", axis=1)

#Créer 7 cluster avec la méthode des KMeans
kmode = KModes(n_clusters=7, init = "random", n_init = 5, verbose=1)
clusters = kmode.fit_predict(df) 


##determination de classes de dangerosité selon le nombre maximal de personne dans le cluster
def class_of_dangerosity(dictionnary,center):
  letters = list(string.ascii_lowercase)
  dangerosityClass = dict()
  new_center = dict()
  c = 0
  dangerosityList = list(dictionnary.values())
  while c < len(dangerosityList) :
    min = 100000000
    i_min = 0
    for i in range(len(dangerosityList)):
      if dangerosityList[i] < min :
        min = dangerosityList[i]
        i_min = i
    dangerosityList[i_min] = 100000000
    dangerosityClass[letters[c]] = [min,i_min]
    new_center[letters[c]] = center[i_min]
    c += 1 
    
  return dangerosityClass,new_center


def dangerosity(x,dictionnary,center):
  dangerosityDict, new_center= class_of_dangerosity(dictionnary,center)
  new_x = list()
  
  for e in x:
    for i in range(len(dangerosityDict)):
      if e == list(dangerosityDict.values())[i][1]:
        new_x.append(list(dangerosityDict)[i][0])

  return np.asarray(new_x), new_center




#trouver les centre des clusters selon leurs features 
def func_center(center,df):
  dict_center=[]
  for i in range(len(center)):
    dict_inter = dict(zip(df.columns, list(center.values())[i]))
    dict_center.append(dict_inter)

  return dict(zip(list(center),np.asarray(dict_center)))


#récupérer les clusters les plus dangereux selon une lettre A (dangereux) --> F (sûr)
unique_c, counts_c = np.unique(clusters, return_counts=True)
label_of_dangerosity,center = dangerosity(clusters,dict(zip(unique_c,counts_c)),kmode.cluster_centroids_)
unique_d, counts_d = np.unique(label_of_dangerosity, return_counts=True)

#récupérer les features les plus impactant selon les clusters les plus dangereux
center_of_dangerosity = func_center(center,df)


#affichage
import plotly.express as px
fig = px.bar(y=counts_d2, x=unique_d2)
fig.show()

#enregistrement et réharmonisation des lettres selon les clusters avec un nombre d'individus équivalent 
df_centers2['class_of_dangerosity'] = list(center_of_dangerosity2)
for i in range(len(list(center_of_dangerosity2))):
  if df_centers2.index[i]=='a':
    df_centers2['class_of_dangerosity'][i]='A'
  if df_centers2.index[i]=='b' :
    df_centers2['class_of_dangerosity'][i]='B'
  if df_centers2.index[i]=='c' or df_centers2.index[i]=='d' or df_centers2.index[i]=='e':
    df_centers2['class_of_dangerosity'][i]='C'
  if df_centers2.index[i]=='f':
    df_centers2['class_of_dangerosity'][i]='D'
  if df_centers2.index[i]=='g':
    df_centers2['class_of_dangerosity'][i]='E'

df_centers2.to_csv('/cluster.csv')

