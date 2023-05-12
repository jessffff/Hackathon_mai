
import pandas as pd
import streamlit as st
from PIL import Image  
from genres import genre_bornes
from genres import genre_radio
from genres import genres
from Reco import reco

df = pd.read_csv('Dataset_clean_2.csv')

st.set_page_config(layout='wide')

image=Image.open('STARTER.png')
col1, col2,col3= st.columns([1,1,1])
col2.image(image,use_column_width=True)


diffusion=('Radio','Online','Vinyles')

Avg_Pay_per_Stream = {
    0.00154: 'YouTube',
    0.00203: 'Pandora',
    0.00348: 'Spotify',
    0.00426: 'Amazon Music',
    0.00562: 'Deezer',
    0.00675: 'Apple Music'}

imprimeurs_vinyles = {'Imprimeur' : ['Ovnyl','Conflikarts','Lacontrebande','Creation-vinyle'],
                      'Price' : ['35 $/U','5,44 $/U pour 1600u','34 $/U','35$'],
                      'Logos' : [Image.open('ovnyl.png'),Image.open('conflikart.jpg'),Image.open('Lacontrebande.png'), Image.open('Creation_vinyle.png') ]}
  
data = {'Distributeur': ['Distro kid', 'Tunecore', 'AWAL', 'Ditto', 'CD Baby'],
        'Price': ['20$/year', '30$/year', '15% fee', '19$/year', '5$/album + 9% fee']}
distrib_spotify = pd.DataFrame(data)


df_genre_radio = pd.DataFrame.from_dict(genre_radio, orient='index', columns=['genres'])



def creation_onglet():
    st.markdown(
        f"<h1 style='text-align: center;'>Création de contenu</h1>",
        unsafe_allow_html=True
    )
    col1, col2,col3= st.columns([1,1,1])
    with st.form("form 1"):
        with col2:
            genre_input = st.selectbox("", genres, format_func=lambda x: x)
            genre_bornes_selected = genre_bornes[genre_input]

    col1, col2,col3,col4 = st.columns([1,1,1,1])
    with st.form("form 2"):
        with col1:
            st.empty()
        with col2:
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
        with col3:
            instrumentalness_min, instrumentalness_max = genre_bornes_selected['instrumentalness']
            instrumentalness = st.slider('Instrumentalness : ', instrumentalness_min, instrumentalness_max)
            liveness_min, liveness_max = genre_bornes_selected['liveness']
            liveness = st.slider('Liveness : ', liveness_min, liveness_max)
            valence_min, valence_max = genre_bornes_selected['valence']
            valence = st.slider('Valence : ', valence_min, valence_max)
            tempo_min, tempo_max = genre_bornes_selected['tempo']
            tempo = st.slider('Tempo : ', tempo_min, tempo_max)
            #duration_ms_min, duration_ms_max = genre_bornes_selected['duration_ms']
            #duration_ms = st.slider('Durée : ', duration_ms_min, duration_ms_max)
        with col4:
            st.empty()
        submit1 = st.form_submit_button("Submit")
    if submit1:
            features = [danceability,energy,loudness,speechiness,acousticness,instrumentalness,liveness,valence,tempo]
            recommandation=reco(df,genre_input,features)
            st.subheader('Recommandations :')
            hide_table_row_index = """
                   <style>
                   thead tr th:first-child {display:none}
                   tbody th {display:none}
                   </style>
                   """
            st.markdown(hide_table_row_index, unsafe_allow_html=True)
            st.table(recommandation)

def diffusion_onglet():
    st.markdown(
        f"<h1 style='text-align: center;'>Diffusion</h1>",
        unsafe_allow_html=True
    )
    with st.form('form1'):
        with st.expander("Radio"):
            st.markdown(f"<h2 style='text-align: center;'>Radio</h2>", unsafe_allow_html=True,)
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
            st.markdown(f"<h2 style='text-align: center;'>Online</h2>", unsafe_allow_html=True,)
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
            st.markdown(f"<h2 style='text-align: center;'>Vinyles</h2>", unsafe_allow_html=True,)
            st.subheader('\n\nSélectionnez un imprimeur de vinyles :')
            imprimeur_input = st.selectbox('', imprimeurs_vinyles)
        submit4 = st.form_submit_button('Submit')
            
        if submit4:
            selected_diffuseur = imprimeur_input
            if selected_diffuseur:
                col1, col2 = st.columns([1,1])
                #st.write("L'imprimeur correspondant à la sélection est : {}".format(selected_diffuseur))
                #logo_column = st.columns(1)
                
                #col1.image(logo_ovnyl)
                st.write("L'imprimeur correspondant à la sélection est : {}".format(selected_diffuseur))
            else:
                st.warning('Aucun imprimeur correspondant à la sélection.')




tabs = {
    "Création": creation_onglet,
    "Diffusion": diffusion_onglet
}
selection = st.sidebar.radio("Sélectionnez un onglet", list(tabs.keys()))

tabs[selection]()
