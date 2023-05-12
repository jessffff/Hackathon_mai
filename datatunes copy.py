#
import pandas as pd
import streamlit as st
import requests
import toml
  
# =============================================================================
# # Charger les informations de configuration à partir du fichier config.toml
# config = toml.load("config.toml")
# 
# # Utiliser les informations de configuration dans la fonction st.set_page_config()
# st.set_page_config(
#     page_title=config["app"]["title"],
#     page_icon=config["app"]["favicon"],
#     layout="wide",
#     initial_sidebar_state="expanded",
#     menu_items=None,
#     primary_color=config["theme"]["primary_color"],
#     background_color=config["theme"]["background_color"],
#     secondary_background_color=config["theme"]["secondary_background_color"],
#     text_color=config["theme"]["text_color"],
#     font=config["theme"]["font"]
# )
# 
# =============================================================================
genres=('disco','electro','hiphop','house','pop','jazz','metal','r&b','ragga','rock','classical','country','latin','bossa nova')
diffusion=('Radio','Online','Vinyles')

Avg_Pay_per_Stream = {
    0.00348: 'Spotify',
    0.00675: 'Apple Music',
    0.00426: 'Amazon Music',
    0.00154: 'YouTube',
    0.00562: 'Deezer',
    0.00203: 'Pandora'
}

genres_radio= {'Rock': 'Virgin','Rap': 'Skyrock',}

imprimeurs_vinyles = ['Imprimeur 1', 'Imprimeur 2', 'Imprimeur 3', 'Imprimeur 4', 'Imprimeur 5']


st.title('_:red[DATATUNES]_')
st.title('hackathon')
st.header('hackathon')
st.subheader("hackathon")
st.write("hackathon")

def creation_onglet():
    st.title("Création de contenu")
    col1, col2 = st.columns([1,1])
    with st.form("form 1"):
        with col1:
            genre_input = st.selectbox("", genres, format_func=lambda x: x)
    col1, col2 = st.columns([1,1])
    with st.form("form 2"):
        with col1:
            danceability = st.slider('Danceability : ', 0.0, 10.0, (0.0, 10.0), step=0.5)
            energy = st.slider('Energy : ', 0.0, 10.0, (0.0, 10.0), step=0.5)
            loudness = st.slider('Loudness : ', 0.0, 10.0, (0.0, 10.0), step=0.5)
            speechiness = st.slider('Speechiness : ', 0.0, 10.0, (0.0, 10.0), step=0.5)
            acousticness = st.slider('Acousticness : ', 0.0, 10.0, (0.0, 10.0), step=0.5)
            st.empty()
        with col2:
            instrumentalness = st.slider('Instrumentalness : ', 0.0, 10.0, (0.0, 10.0), step=0.5)
            liveness = st.slider('Liveness : ', 0.0, 10.0, (0.0, 10.0), step=0.5)
            valence = st.slider('Valence : ', 0.0, 10.0, (0.0, 10.0), step=0.5)
            tempo = st.slider('Tempo : ', 0.0, 10.0, (0.0, 10.0), step=0.5)
            duration_ms = st.slider('Durée : ', 0.0, 6.0, (0.0, 6.0), step=0.1)
        submit1 = st.form_submit_button("Submit")


     
def diffusion_onglet():
    st.title("Diffusion de contenu")
    
    with st.form("form 1"):
        st.write("Quelle diffusion ?")
        online_input = st.radio("", diffusion)
        
        submit1 = st.form_submit_button('Next')
        submit2 = False
        
        if submit1 and online_input == 'Online':
            st.write('\n\nSélectionnez la moyenne de paiement par stream :')
            moyenne_paiement_input = st.selectbox('', list(Avg_Pay_per_Stream.keys()))
            submit2 = st.form_submit_button('Submit')

        if submit2:
            selected_diffuseur = Avg_Pay_per_Stream.get(moyenne_paiement_input)
            st.success('Moyenne de paiement sélectionnée: {}'.format(moyenne_paiement_input))
            
            if selected_diffuseur:
                st.success("Le diffuseur correspondant à la sélection est: {}".format(selected_diffuseur))
            else:
                st.warning('Aucun diffuseur correspondant à la sélection.')

        elif submit1 and online_input == 'Radio':
            st.write('\n\nQuel genre de musique souhaitez-vous diffuser ?')
            genre_input = st.selectbox('', list(genres_radio.keys()))
            submit2 = st.form_submit_button('Submit')

        if submit2:
            selected_diffuseur = genres_radio.get(genre_input)
            st.success('Genre musical sélectionné: {}'.format(genre_input))
            
            if selected_diffuseur:
                st.success("Le diffuseur correspondant à la sélection est: {}".format(selected_diffuseur))
            else:
                st.warning('Aucun diffuseur correspondant à la sélection.')

        elif submit1 and online_input == 'Vinyles':
            st.write('\n\nSélectionnez un imprimeur de vinyles :')
            imprimeur_input = st.selectbox('', imprimeurs_vinyles)
            submit2 = st.form_submit_button('Submit')

        if submit2:
            selected_diffuseur = imprimeur_input
            st.success('Imprimeur de vinyles sélectionné: {}'.format(imprimeur_input))
            
            if selected_diffuseur:
                st.success("L'imprimeur correspondant à la sélection est: {}".format(selected_diffuseur))
            else:
                st.warning('Aucun imprimeur correspondant à la sélection.')

        
        
# =============================================================================
#         
#         if online_input == 'Online':
#             st.write('\n\nSélectionnez la moyenne de paiement par stream :')
#             moyenne_paiement_input = st.selectbox('', list(Avg_Pay_per_Stream.keys()))
#         
#         submit2 = st.form_submit_button('Submit')
# 
#         if submit2:
#             selected_diffuseur = Avg_Pay_per_Stream.get(moyenne_paiement_input)
#                        
#             if selected_diffuseur:
#                 st.write('Moyenne de paiement sélectionnée :', moyenne_paiement_input)
#                 st.write("Le diffuseur correspondant à la moyenne de paiement sélectionnée est :", selected_diffuseur)
#             else:
#                 st.write('Aucun diffuseur correspondant à la moyenne de paiement sélectionnée.')
# 
# 
# =============================================================================



tabs = {
    "Création": creation_onglet,
    "Diffusion": diffusion_onglet
}
selection = st.sidebar.radio("Sélectionnez un onglet", list(tabs.keys()))
tabs[selection]()


