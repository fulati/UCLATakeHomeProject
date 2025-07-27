from classes import Movie, Theater, Screen, Show

#Movies
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

#Theaters
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
            screen = Screen(screen_id, theater)
            theater.screens.append(screen)
        theaters.append(theater)
    
    return theaters

#Shows
def get_shows(movies, theaters):
    return [
        Show("show1", movies[0], theaters[0].screens[0], "4:00 PM"),
        Show("show2", movies[1], theaters[0].screens[1], "6:00 PM"),
        Show("show3", movies[2], theaters[1].screens[0], "5:00 PM"),
        Show("show4", movies[3], theaters[1].screens[2], "7:30 PM"),
        Show("show5", movies[4], theaters[2].screens[1], "9:00 PM"),
        Show("show6", movies[5], theaters[2].screens[2], "8:00 PM"),
        Show("show7", movies[6], theaters[3].screens[0], "3:00 PM"),
        Show("show8", movies[7], theaters[3].screens[1], "5:30 PM"),
        Show("show9", movies[8], theaters[4].screens[0], "7:45 PM"),
        Show("show10", movies[9], theaters[4].screens[2], "10:15 PM"),
    ]
