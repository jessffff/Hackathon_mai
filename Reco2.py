import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('dataset_clean.csv')


df_cos = df.drop(columns = ['Unnamed: 0','id_artists','id_artists','id_tracks_df','popularity_artists_df','followers','time_signature',"duration_ms"])

df_cos['Tag'] = df_cos[df_cos.columns[5:]].apply(lambda x: ', '.join(x.astype(str)),axis=1)

list_features = ["X","","","","","","","","","","","","","",""]

df_cos.loc[len(df)] = list_features 


def search2(df_cos,genre,features):
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df_cos["Tag"])
    similarity_scores = cosine_similarity(count_matrix)
    df_cos.reset_index(inplace =True, drop =True)
    df_cos.drop([df_cos.index[-1]])
   
    list_result =[]
    y = df_cos.index[-1]
    Nmovie = 5
    ind = y

    max_indices = np.argpartition(similarity_scores,-Nmovie)[ind]
    Best_simil  = max_indices[-Nmovie:][::]
    
    # Best simil 
    for i in Best_simil :
        x = df_cos.iloc[i][['name_artists_df','name_tracks_df','release_year','duration_m','popularity_tracks_df']]
        list_result.append(x)
        
    return list_result[1:]