
genres=['disco','electro','hiphop','house','pop','jazz','metal','r&b','rock','classical','country','latin','bossa nova']

genre_bornes = {
    'disco': {
        'danceability': (0.532, 0.872),
        'energy': (0.500, 0.910),
        'loudness': (-14.105, -3.851),
        'speechiness': (0.0251, 0.205),
        'acousticness': (0.0178, 0.405),
        'instrumentalness': (0.000, 0.605),
        'liveness': (0.034, 0.702),
        'valence': (0.537, 0.980),
        'tempo': (102.035, 136.282),
        'duration_m': (3.19, 8.20)
    },
    'electro': {
        'danceability': (0.590, 0.875),
        'energy': (0.297, 0.926),
        'loudness': (-14.116, -3.728),
        'speechiness': (0.031, 0.301),
        'acousticness': (0.000, 0.894),
        'instrumentalness': (0.000, 0.950),
        'liveness': (0.029, 0.381),
        'valence': (0.067, 0.963),
        'tempo': (90.039, 127.977),
        'duration_m': (3.36, 10.00)
    },
    'hiphop': {
        'danceability': (0.638, 0.970),
        'energy': (0.169, 0.993),
        'loudness': (-21.099, 0.642),
        'speechiness': (0.026, 0.875),
        'acousticness': (0.000, 0.971),
        'instrumentalness': (0.000, 0.954),
        'liveness': (0.022, 0.976),
        'valence': (0.033, 0.973),
        'tempo': (66.858, 209.910),
        'duration_m': (1.370, 12.060)
    },
    'house': {
        'danceability': (0.275, 0.979),
        'energy': (0.224, 0.993),
        'loudness': (-14.762, 1.634),
        'speechiness': (0.025, 0.375),
        'acousticness': (0.000, 0.772),
        'instrumentalness': (0.000, 0.948),
        'liveness': (0.037, 0.839),
        'valence': (0.089, 0.924),
        'tempo': (82.433, 179.998),
        'duration_m': (2.38, 9.06)
    },
    'pop': {
        'danceability': (0.144, 0.982),
        'energy': (0.016, 0.993),
        'loudness': (-32.244, -0.532),
        'speechiness': (0.023, 0.884),
        'acousticness': (0.000, 0.994),
        'instrumentalness': (0.000, 0.962),
        'liveness': (0.015, 0.989),
        'valence': (0.034, 0.979),
        'tempo': (40.217, 220.065),
        'duration_m': (0.63, 14.04)
    },
    'jazz': {
        'danceability': (0.304, 0.837),
        'energy': (0.304, 0.850),
        'loudness': (-26.813, -5.542),
        'speechiness': (0.027, 0.119),
        'acousticness': (0.003, 0.910),
        'instrumentalness': (0.000, 0.937),
        'liveness': (0.085, 0.239),
        'valence': (0.114, 0.875),
        'tempo': (51.533, 180.112),
        'duration_m': (2.79, 8.22)
    },
    'metal': {
        'danceability': (0.113, 0.820),
        'energy': (0.200, 0.998),
        'loudness': (-11.439, 1.023),
        'speechiness': (0.025, 0.420),
        'acousticness': (0.000, 0.909),
        'instrumentalness': (0.000, 0.927),
        'liveness': (0.022, 0.926),
        'valence': (0.039, 0.962),
        'tempo': (62.110, 200.024),
        'duration_m': (2.20, 11.89)
    },
    'r&b': {
        'danceability': (0.240, 0.913),
        'energy': (0.085, 0.885),
        'loudness': (-20.338, -3.310),
        'speechiness': (0.026, 0.567),
        'acousticness': (0.001, 0.983),
        'instrumentalness': (0.000, 0.786),
        'liveness': (0.032, 0.791),
        'valence': (0.034, 0.937),
        'tempo': (59.561, 210.164),
        'duration_m': (1.11, 9.88)
    }
    'rock': {
        'danceability': (0.120, 0.928),
        'energy': (0.023, 0.993),
        'loudness': (-19.537, -0.783),
        'speechiness': (0.022, 0.318),
        'acousticness': (0.000, 0.994),
        'instrumentalness': (0.026, 0.996),
        'liveness': (0.026, 0.990),
        'valence': (0.039, 0.973),
        'tempo': (54.134, 205.416),
        'duration_m': (1.83, 7.94)
    },
    'classical': {
        'danceability': (0.448, 0.521),
        'energy': (0.062, 0.502),
        'loudness': (-21.524, -8.521),
        'speechiness': (0.028, 0.034),
        'acousticness': (0.843, 0.886),
        'instrumentalness': (0.020, 0.406),
        'liveness': (0.133, 0.188),
        'valence': (0.175, 0.378),
        'tempo': (95.028, 104.311),
        'duration_m': (2.92, 4.02)
    },
    'country': {
        'danceability': (0.276, 0.907),
        'energy': (0.056, 0.976),
        'loudness': (-16.225, -1.721),
        'speechiness': (0.023, 0.668),
        'acousticness': (0.000, 0.919),
        'instrumentalness': (0.000, 0.886),
        'liveness': (0.021, 0.962),
        'valence': (0.110, 0.972),
        'tempo': (48.718, 208.067),
        'duration_ms': (1.57, 5.75)
    },
    'latin': {
        'danceability': (0.248, 0.928),
        'energy': (0.188, 0.993),
        'loudness': (-16.692, -1.998),
        'speechiness': (0.024, 0.484),
        'acousticness': (0.000, 0.985),
        'instrumentalness': (0.000, 0.206),
        'liveness': (0.019, 0.963),
        'valence': (0.050, 0.978),
        'tempo': (70.171, 209.795),
        'duration_m': (2.12, 6.27)
    },
    'bossa nova': {
        'danceability': (0.418, 0.671),
        'energy': (0.499, 0.836),
        'loudness': (-10.799, -6.672),
        'speechiness': (0.029, 0.084),
        'acousticness': (0.197, 0.889),
        'instrumentalness': (0.000, 0.000),
        'liveness': (0.132, 0.951),
        'valence': (0.0209, 0.837),
        'tempo': (113.02, 169.880),
        'duration_m': (2.89, 5.14)
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
