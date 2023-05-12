import pandas as pd 

from sklearn.metrics.pairwise import cosine_similarity


df = pd.read_csv('Dataset_clean_3.csv')



def reco(df,genre,features):
    filtered_df = df[df['genre'] == genre]

    user_vector = [features]

    features_df = filtered_df[['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']]
    similarity_scores = cosine_similarity(features_df, user_vector)

    filtered_df['similarity'] = similarity_scores

    recommended_tracks = filtered_df.sort_values('similarity', ascending=False)[:5]
    
    recommended_tracks = recommended_tracks[['name_artists','name_tracks','release_year','duration_m','popularity_tracks','danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']]

    return recommended_tracks
