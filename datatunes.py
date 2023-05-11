import pandas as pd
import streamlit as st
import requests
import toml
  
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)



genres=('disco','electro','hiphop','house','pop','jazz','metal','r&b','ragga','rock','classical','country','latin','bossa nova')
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



st.title('_:red[DATATUNES]_')

def creation_onglet():
    st.title("Création de contenu")
    col1, col2 = st.columns([1,1])
    with st.form("form 1"):
        with col1:
            genre_input = st.selectbox("", genres, format_func=lambda x: x)
    col1, col2 = st.columns([1,1])
    with st.form("form 2"):
        with col1:
            danceability = st.slider('Danceability : ', 0.0, 10.0, (3.0, 8.0), step=0.5)
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
    with st.form('form1'):
        with st.expander("Radio"):
            st.markdown(f"<h1 style='text-align: center;'>Radio</h1>", unsafe_allow_html=True,)
            st.subheader('\n\nQuel genre de musique souhaitez-vous diffuser ?')
            genre_input = st.selectbox('', list(set([genre.strip() for genres in df_genre_radio['genres'] for genre in genres.split(",")])))

        submit2 = st.form_submit_button('Submit')

        if submit2:
            selected_diffuseur = df_genre_radio[df_genre_radio['genres'].apply(lambda x: genre_input in x)]

            if not selected_diffuseur.empty:
                st.success("Le(s) diffuseur(s) correspondant(s) à la sélection :")
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
           # st.success('Moyenne de paiement sélectionnée : {}'.format(moyenne_paiement_input))

            if selected_diffuseur:
                st.success("Le diffuseur correspondant à la sélection est : {}".format(selected_diffuseur))
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
         #   st.success('Imprimeur de vinyles sélectionné : {}'.format(imprimeur_input))

            if selected_diffuseur:
                st.success("L'imprimeur correspondant à la sélection est : {}".format(selected_diffuseur))
            else:
                st.warning('Aucun imprimeur correspondant à la sélection.')

  
# =============================================================================
#      
# def diffusion_onglet():
#     st.title("Diffusion de contenu")
# 
#     with st.form("form1"):
#         st.write("Quelle diffusion ?")
#         online_input = st.selectbox("", diffusion)
#         submit1 = st.form_submit_button("Next")
# 
#     if submit1 and online_input == "Online":
#         with st.form("form2"):
#             st.write("\n\nSélectionnez la moyenne de paiement par stream :")
#             moyenne_paiement_input = st.selectbox("", list(Avg_Pay_per_Stream.keys()))
#             submit2 = st.form_submit_button("Submit")
# 
#             if submit2:
#                 selected_diffuseur = Avg_Pay_per_Stream.get(moyenne_paiement_input)
#                 st.success("Moyenne de paiement sélectionnée: {}".format(moyenne_paiement_input))
# 
#                 if selected_diffuseur:
#                     st.success("Le diffuseur correspondant à la sélection est: {}".format(selected_diffuseur))
#                 else:
#                     st.warning("Aucun diffuseur correspondant à la sélection.")
# 
#     elif submit1 and online_input == "Radio":
#         with st.form("form3"):
#             st.write("\n\nQuel genre de musique souhaitez-vous diffuser ?")
#             genre_input = st.selectbox("", list(genres_radio.keys()))
#             submit3 = st.form_submit_button("Submit")
# 
#             if submit3:
#                 selected_diffuseur = genres_radio.get(genre_input)
#                 st.success("Genre musical sélectionné: {}".format(genre_input))
# 
#                 if selected_diffuseur:
#                     st.success("Le diffuseur correspondant à la sélection est: {}".format(selected_diffuseur))
#                 else:
#                     st.warning("Aucun diffuseur correspondant à la sélection.")
# 
#     elif submit1 and online_input == "Vinyles":
#         with st.form("form4"):
#             st.write("\n\nSélectionnez un imprimeur de vinyles :")
#             imprimeur_input = st.selectbox("", imprimeurs_vinyles)
#             submit4 = st.form_submit_button("Submit")
# 
#             if submit4:
#                 selected_diffuseur = imprimeur_input
#                 st.success("Imprimeur de vinyles sélectionné: {}".format(imprimeur_input))
# 
#                 if selected_diffuseur:
#                     st.success("L'imprimeur correspondant à la sélection est: {}".format(selected_diffuseur))
#                 else:
#                     st.warning("Aucun imprimeur correspondant à la sélection.")
# 
# 
# =============================================================================


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


