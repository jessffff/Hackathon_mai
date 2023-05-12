import pandas as pd 

from sklearn.metrics.pairwise import cosine_similarity


df = pd.read_csv('Dataset_clean_2.csv')


df = df.drop(columns = ['Unnamed: 0','id_artists','id_artists','id_tracks_df','popularity_artists_df','followers','time_signature',"duration_ms"])


def reco(df,genre,features):
    filtered_df = df[df['genre'] == genre]

    user_vector = [features]

    features_df = filtered_df[['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']]
    similarity_scores = cosine_similarity(features_df, user_vector)

    filtered_df['similarity'] = similarity_scores

    recommended_tracks = filtered_df.sort_values('similarity', ascending=False)[:5]
    
    recommended_tracks = recommended_tracks[['name_artists_df','name_tracks_df','release_year','duration_m','popularity_tracks_df']]

    return recommended_tracks
