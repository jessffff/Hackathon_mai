import pandas as pd
import streamlit as st
import requests
import toml
from PIL import Image


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


image=Image.open('STARTER.png')
st.image(image,use_column_width=True)


genres=('disco','electro','hiphop','house','pop','jazz','metal','r&b','ragga','rock','classical','country','latin','bossa nova')
diffusion=('Radio','Online','Vinyles')
genre_bornes = {
    'disco': {
        'danceability': (6.0, 10.0),
        'energy': (6.0, 10.0),
        'loudness': (-30.0, -10.0),
        'speechiness': (2.0, 8.0),
        'acousticness': (0.0, 4.0),
        'instrumentalness': (0.0, 6.0),
        'liveness': (4.0, 10.0),
        'valence': (6.0, 10.0),
        'tempo': (100.0, 140.0),
        'duration_ms': (180000.0, 300000.0)
    },
    'electro': {
        'danceability': (7.0, 10.0),
        'energy': (7.0, 10.0),
        'loudness': (-30.0, -5.0),
        'speechiness': (2.0, 6.0),
        'acousticness': (0.0, 6.0),
        'instrumentalness': (6.0, 10.0),
        'liveness': (4.0, 10.0),
        'valence': (4.0, 8.0),
        'tempo': (120.0, 160.0),
        'duration_ms': (180000.0, 300000.0)
    },
    'hiphop': {
        'danceability': (5.0, 8.0),
        'energy': (5.0, 8.0),
        'loudness': (-30.0, -5.0),
        'speechiness': (6.0, 10.0),
        'acousticness': (0.0, 6.0),
        'instrumentalness': (0.0, 6.0),
        'liveness': (4.0, 10.0),
        'valence': (2.0, 8.0),
        'tempo': (60.0, 100.0),
        'duration_ms': (180000.0, 300000.0)
    },
    'house': {
        'danceability': (7.0, 10.0),
        'energy': (7.0, 10.0),
        'loudness': (-30.0, -5.0),
        'speechiness': (2.0, 6.0),
        'acousticness': (0.0, 6.0),
        'instrumentalness': (6.0, 10.0),
        'liveness': (4.0, 10.0),
        'valence': (4.0, 8.0),
        'tempo': (120.0, 140.0),
        'duration_ms': (180000.0, 300000.0)
    },
    'pop': {
        'danceability': (6.0, 9.0),
        'energy': (4.0, 8.0),
        'loudness': (-30.0, -5.0),
        'speechiness': (2.0, 8.0),
        'acousticness': (0.0, 6.0),
        'instrumentalness': (6.0, 10.0),
        'liveness': (4.0, 10.0),
        'valence': (4.0, 8.0),
        'tempo': (120.0, 140.0),
        'duration_ms': (180000.0, 300000.0)
    },
    'jazz': {
        'danceability': (7.0, 10.0),
        'energy': (7.0, 10.0),
        'loudness': (-30.0, -5.0),
        'speechiness': (2.0, 6.0),
        'acousticness': (0.0, 6.0),
        'instrumentalness': (6.0, 10.0),
        'liveness': (4.0, 10.0),
        'valence': (4.0, 8.0),
        'tempo': (120.0, 160.0),
        'duration_ms': (180000.0, 300000.0)
    },
    'metal': {
        'danceability': (6.0, 10.0),
        'energy': (6.0, 10.0),
        'loudness': (-30.0, -10.0),
        'speechiness': (2.0, 8.0),
        'acousticness': (0.0, 4.0),
        'instrumentalness': (0.0, 6.0),
        'liveness': (4.0, 10.0),
        'valence': (6.0, 10.0),
        'tempo': (100.0, 140.0),
        'duration_ms': (180000.0, 300000.0)
    },
    'r&b': {
        'danceability': (7.0, 10.0),
        'energy': (7.0, 10.0),
        'loudness': (-30.0, -5.0),
        'speechiness': (2.0, 6.0),
        'acousticness': (0.0, 6.0),
        'instrumentalness': (6.0, 10.0),
        'liveness': (4.0, 10.0),
        'valence': (4.0, 8.0),
        'tempo': (120.0, 140.0),
        'duration_ms': (180000.0, 300000.0)
    },
    'ragga': {
        'danceability': (6.0, 9.0),
        'energy': (4.0, 8.0),
        'loudness': (-30.0, -5.0),
        'speechiness': (2.0, 8.0),
        'acousticness': (0.0, 6.0),
        'instrumentalness': (6.0, 10.0),
        'liveness': (4.0, 10.0),
        'valence': (4.0, 8.0),
        'tempo': (120.0, 140.0),
        'duration_ms': (180000.0, 300000.0)
    },
    'rock': {
        'danceability': (6.0, 10.0),
        'energy': (6.0, 10.0),
        'loudness': (-30.0, -10.0),
        'speechiness': (2.0, 8.0),
        'acousticness': (0.0, 4.0),
        'instrumentalness': (0.0, 6.0),
        'liveness': (4.0, 10.0),
        'valence': (6.0, 10.0),
        'tempo': (100.0, 140.0),
        'duration_ms': (180000.0, 300000.0)
    },
    'classical': {
        'danceability': (6.0, 10.0),
        'energy': (6.0, 10.0),
        'loudness': (-30.0, -10.0),
        'speechiness': (2.0, 8.0),
        'acousticness': (0.0, 4.0),
        'instrumentalness': (0.0, 6.0),
        'liveness': (4.0, 10.0),
        'valence': (6.0, 10.0),
        'tempo': (100.0, 140.0),
        'duration_ms': (180000.0, 300000.0)
    },
    'country': {
        'danceability': (5.0, 8.0),
        'energy': (5.0, 8.0),
        'loudness': (-30.0, -5.0),
        'speechiness': (6.0, 10.0),
        'acousticness': (0.0, 6.0),
        'instrumentalness': (0.0, 6.0),
        'liveness': (4.0, 10.0),
        'valence': (2.0, 8.0),
        'tempo': (60.0, 100.0),
        'duration_ms': (180000.0, 300000.0)
    },
    'latin': {
        'danceability': (6.0, 10.0),
        'energy': (6.0, 10.0),
        'loudness': (-30.0, -10.0),
        'speechiness': (2.0, 8.0),
        'acousticness': (0.0, 4.0),
        'instrumentalness': (0.0, 6.0),
        'liveness': (4.0, 10.0),
        'valence': (6.0, 10.0),
        'tempo': (100.0, 140.0),
        'duration_ms': (180000.0, 300000.0)
    },
    'bossa nova': {
        'danceability': (6.0, 10.0),
        'energy': (6.0, 10.0),
        'loudness': (-30.0, -10.0),
        'speechiness': (2.0, 8.0),
        'acousticness': (0.0, 4.0),
        'instrumentalness': (0.0, 6.0),
        'liveness': (4.0, 10.0),
        'valence': (6.0, 10.0),
        'tempo': (100.0, 140.0),
        'duration_ms': (180000.0, 300000.0)
    } 
}
Avg_Pay_per_Stream = {
    0.00154: 'YouTube',
    0.00203: 'Pandora',
    0.00348: 'Spotify',
    0.00426: 'Amazon Music',
    0.00562: 'Deezer',
    0.00675: 'Apple Music'}
imprimeurs_vinyles = {
    'ovnyl'	: '35 $/U',
    'confliktarts' : '5,44 $/U pour 1600u',
    'lacontrebande' : '34 $/U',
    'creation-vinyle' : '35$'} 
data = {'Distributeur': ['Distro kid', 'Tunecore', 'AWAL', 'Ditto', 'CD Baby'],
        'Price': ['20$/year', '30$/year', '15% fee', '19$/year', '5$/album + 9% fee']}
distrib_spotify = pd.DataFrame(data)

genre_radio = {
    'France Inter': 'années 80, pop musique, rap, jazz, chanson française, rock',
    'RMC': 'pop, rock, rap, electro, world, jazz, chanson française',
    'Franceinfo': 'pop, rock, rap, electro, world, jazz, chanson française',
    'RTL': 'pop rock, pop',
    'NRJ': 'chanson française, dance, dancehall, electro, funk, gangsta rap, hiphop, latino, pop, pop-rock, rap, reggae, reggaeton, r&b, rock, soul, techno, zouk, electro, house, latin',
    'Nostalgie': 'disco, années 80, années 90, country',
    'FIP': 'jazz, electro, rock, pop, groove',
    'Cherie FM': 'féminin, pop rock, pop',
    'Skyrock': 'rap, r&b, ragga',
    'France Culture': 'classique, chanson française',
    'RTL2': 'pop rock, rock',
    'Radio Classique': 'classical, bossa nova',
    'Fun Radio': 'electro, dance, Techno, house, latin',
    'Rire et Chansons': 'pop rock, chanson française, rock',
    'Sud Radio': 'pop rock, pop, chanson française',
    'Radio Orient': 'chanson arabe',
    'France Musique': 'classical, jazz, bossa nova',
    'M Radio': 'chanson française',
    'Chante France': 'chanson française',
    'Oui FM': 'rock, punk, electro, house, metal, country'
}
df_genre_radio = pd.DataFrame.from_dict(genre_radio, orient='index', columns=['genres'])




def creation_onglet():
    st.title("Création de contenu")
    col1, col2 = st.columns([1,1])
    with st.form("form 1"):
        with col1:
            genre_input = st.selectbox("", genres, format_func=lambda x: x)
            genre_bornes_selected = genre_bornes[genre_input]
    col1, col2 = st.columns([1,1])
    with st.form("form 2"):
        with col1:
            danceability_min, danceability_max = genre_bornes_selected['danceability']
            danceability = st.slider('Danceability : ', danceability_min, danceability_max)
            energy_min, energy_max = genre_bornes_selected['energy']
            energy = st.slider('Energy : ', energy_min, energy_max)
            loudness_min, loudness_max = genre_bornes_selected['loudness']
            loudness = st.slider('Loudness : ', loudness_min, loudness_max)
            speechiness_min, speechiness_max = genre_bornes_selected['speechiness']
            speechiness = st.slider('Speechiness : ', speechiness_min, speechiness_max)
            acousticness_min, acousticness_max = genre_bornes_selected['acousticness']
            acousticness = st.slider('Acousticness : ', acousticness_min, acousticness_max)
            st.empty()
        with col2:
            instrumentalness_min, instrumentalness_max = genre_bornes_selected['instrumentalness']
            instrumentalness = st.slider('Instrumentalness : ', instrumentalness_min, instrumentalness_max)
            liveness_min, liveness_max = genre_bornes_selected['liveness']
            liveness = st.slider('Liveness : ', liveness_min, liveness_max)
            valence_min, valence_max = genre_bornes_selected['valence']
            valence = st.slider('Valence : ', valence_min, valence_max)
            tempo_min, tempo_max = genre_bornes_selected['tempo']
            tempo = st.slider('Tempo : ', tempo_min, tempo_max)
            duration_ms_min, duration_ms_max = genre_bornes_selected['duration_ms']
            duration_ms = st.slider('Durée : ', duration_ms_min, duration_ms_max)
        submit1 = st.form_submit_button("Submit")
 


def diffusion_onglet():
    st.title("Diffusion de contenu")
    with st.form('form1'):
        with st.expander("Radio"):
            st.markdown(f"<h1 style='text-align: center;'>Radio</h1>", unsafe_allow_html=True,)
            st.subheader('\n\nQuel genre de musique souhaitez-vous diffuser ?')
            genre_input = st.selectbox('', list(set([genre.strip() for genres in df_genre_radio['genres'] for genre in genres.split(",")])))

        submit2 = st.form_submit_button('Submit')

        if submit2:
            selected_diffuseur = df_genre_radio[df_genre_radio['genres'].apply(lambda x: genre_input in x)]

            if not selected_diffuseur.empty:
                st.write("Le(s) diffuseur(s) correspondant(s) à la sélection :")
                for index, row in selected_diffuseur.iterrows():
                    st.write(index)
            else:
                st.warning('Aucun diffuseur correspondant à la sélection.')

    with st.form('form2'):                
        with st.expander("Online"):
            st.markdown(f"<h1 style='text-align: center;'>Online</h1>", unsafe_allow_html=True,)
            st.subheader('\n\nSélectionnez la moyenne de paiement par stream :')
            moyenne_paiement_input = st.selectbox('', list(Avg_Pay_per_Stream.keys()))
        submit3 = st.form_submit_button('Submit')

        if submit3:
            selected_diffuseur = Avg_Pay_per_Stream.get(moyenne_paiement_input)
            if selected_diffuseur:
                st.write("Le diffuseur correspondant à la sélection est : {}".format(selected_diffuseur))
            else:
                st.warning('Aucun diffuseur correspondant à la sélection.')
                
            if selected_diffuseur == 'Spotify':
                st.subheader('Liste de distribteurs pour Spotify :')
                hide_table_row_index = """
                        <style>
                        thead tr th:first-child {display:none}
                        tbody th {display:none}
                        </style>
                        """
                st.markdown(hide_table_row_index, unsafe_allow_html=True)
                st.table(distrib_spotify)
            
    with st.form('form3'):
        with st.expander("Vinyles"):
            st.markdown(f"<h1 style='text-align: center;'>Vinyles</h1>", unsafe_allow_html=True,)
            st.subheader('\n\nSélectionnez un imprimeur de vinyles :')
            imprimeur_input = st.selectbox('', imprimeurs_vinyles)
        submit4 = st.form_submit_button('Submit')
            
        if submit4:
            selected_diffuseur = imprimeur_input
            if selected_diffuseur:
                st.write("L'imprimeur correspondant à la sélection est : {}".format(selected_diffuseur))
            else:
                st.warning('Aucun imprimeur correspondant à la sélection.')







tabs = {
    "Création": creation_onglet,
    "Diffusion": diffusion_onglet
}
selection = st.sidebar.radio("Sélectionnez un onglet", list(tabs.keys()))
tabs[selection]()


