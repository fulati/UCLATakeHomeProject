from classes import Movie, Theater, Screen, Show
from datetime import datetime

# Movies
def get_movies():
    return [
        Movie("Inception", "Sci-Fi", 148, 8.8),
        Movie("Tenet", "Sci-Fi", 150, 7.3),
        Movie("Interstellar", "Sci-Fi", 169, 8.7),
        Movie("Shutter Island", "Thriller", 138, 8.2),
        Movie("The Dark Knight", "Crime", 152, 9.1),
        Movie("The Prestige", "Drama", 130, 8.5),
        Movie("Dunkirk", "War", 106, 7.9),
        Movie("Oppenheimer", "Biography", 180, 8.6),
        Movie("Memento", "Mystery", 113, 8.4),
        Movie("Parasite", "Thriller", 132, 8.6),
        Movie("La La Land", "Romance", 128, 8.0),
    ]

# Theaters
def get_theaters():
    locations = [
        ("AMC The Grove 14", "Los Angeles, CA"),
        ("AMC The Americana at Brand 18", "Glendale, CA"), 
        ("AMC Marina Marketplace 6", "Marina Del Rey, CA"),
        ("Regal LA Live", "Downtown Los Angeles, CA"),
        ("Cinemark Playa Vista", "Playa Vista, CA"),
    ]
    
    theaters = []
    for name, location in locations:
        theater = Theater(name, location)
        for i in range(4):
            screen_id = name.replace(' ', '_').lower() + "_screen_" + str(i+1)
            screen = Screen(screen_id)
            theater.screens.append(screen)
        theaters.append(theater)
    
    return theaters

# Shows
def get_shows(movies, theaters):
    return [
        Show("show1", movies[0], theaters[0], theaters[0].screens[0], datetime(2025, 7, 27, 16, 0)),   # July 27, 2025, 4:00 PM
        Show("show2", movies[1], theaters[0], theaters[0].screens[1], datetime(2025, 7, 29, 18, 0)),   # July 29, 2025, 6:00 PM
        Show("show3", movies[2], theaters[1], theaters[1].screens[0], datetime(2025, 8, 1, 17, 0)),    # Aug 1, 2025, 5:00 PM
        Show("show4", movies[3], theaters[1], theaters[1].screens[2], datetime(2025, 8, 3, 19, 30)),   # Aug 3, 2025, 7:30 PM
        Show("show5", movies[4], theaters[2], theaters[2].screens[1], datetime(2025, 8, 5, 21, 0)),    # Aug 5, 2025, 9:00 PM
        Show("show6", movies[5], theaters[2], theaters[2].screens[2], datetime(2025, 8, 7, 20, 0)),    # Aug 7, 2025, 8:00 PM
        Show("show7", movies[6], theaters[3], theaters[3].screens[0], datetime(2025, 8, 10, 15, 0)),   # Aug 10, 2025, 3:00 PM
        Show("show8", movies[7], theaters[3], theaters[3].screens[1], datetime(2025, 8, 12, 17, 30)),  # Aug 12, 2025, 5:30 PM
        Show("show9", movies[8], theaters[4], theaters[4].screens[0], datetime(2025, 8, 15, 19, 45)),  # Aug 15, 2025, 7:45 PM
        Show("show10", movies[9], theaters[4], theaters[4].screens[2], datetime(2025, 8, 17, 22, 15)), # Aug 17, 2025, 10:15 PM
    ]
