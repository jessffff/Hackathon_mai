
genres=['disco','electro','hiphop','house','pop','jazz','metal','r&b','ragga','rock','classical','country','latin','bossa nova']

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