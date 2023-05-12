#
import pandas as pd
import streamlit as st
import requests
import toml
from PIL import Image  
from genres import genre_bornes
from genres import genre_radio
from genres import genres

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


diffusion=('Radio','Online','Vinyles')

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

