#Imports
import uuid
from typing import List, Set, Dict
from datetime import datetime


#Movie Class (title, genre, duration, rating)
class Movie:
    def __init__(self, title: str, genre: str, duration: int, rating: float):
        self.title = title
        self.genre = genre
        self.duration = duration  # in minutes
        self.rating = rating  # based on IMDB

#Theater Class (name, location)
class Theater:
    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location
        self.screens: List[Screen] = []

#Screen Class (screen_id, theater, rows, seats_per_row)
class Screen:
    def __init__(self, screen_id: str, theater: Theater, rows: int = 10, seats_per_row: int = 10):
        self.screen_id = screen_id
        self.theater = theater
        self.seats = []
        
        #Create 10 x 10 seats selection from "A1" to "J10".
        for r in range(rows):
            row_list = []
            row_char = chr(65 + r) #row 'A' to 'J'
            for seat_num in range(1, seats_per_row + 1): # seats 1 - 10
                row_list.append(row_char + str(seat_num))
            self.seats.append(row_list)

#Show Class (show_id, movie, screen, time)
class Show:
    def __init__(self, show_id: str, movie: Movie, screen: Screen, time: str):
        self.show_id = show_id
        self.movie = movie
        self.screen = screen
        self.time = time
        self.booked_seats: Set[str] = set()

#Booking Class (user, show, seats)
class Booking: 
    def __init__(self, user: str, show: Show, seats: List[str]):
        self.booking_id = str(uuid.uuid4()) #creates a random ID
        self.user = user
        self.show = show
        self.seats = seats
        self.timeStamp = datetime.now()

#MovieBookingSystem Class with (movies, theaters, shows, bookings)
class MovieBookingSystem: 
    def __init__(self):
        self.movies: List[Movie] = []
        self.theaters: List[Theater] = []
        self.shows: Dict[str, Show] = {}
        self.bookings: Dict[str, Booking] = {}
        
    #Add movies 
    def add_movie(self, movie: Movie) -> None:
        self.movies.append(movie)

    #Add theaters
    def add_theater(self, theater: Theater) -> None:
        self.theaters.append(theater)

    #Add shows
    def add_show(self, show: Show) -> None:
        self.shows[show.show_id] = show

    #search_movies function
    def search_movies(self, query: str) -> List[Movie]: 
        results: List[Movie] = []
        
        for movie in self.movies:
            if query.lower() in movie.title.lower():
                results.append(movie)
        
        return results

    #list_showtime function


    #book_seats function


    #cancel_bookings function



#Main
def main(): 
    system = MovieBookingSystem()
    
    #Adding movie
    system.add_movie(Movie("Inception", "Sci-Fi", 148, 8.8))
    system.add_movie(Movie("Tenet", "Sci-Fi", 150, 7.3))
    system.add_movie(Movie("Interstellar", "Sci-Fi", 169, 8.7))
    system.add_movie(Movie("Shutter Island", "Thriller", 138, 8.2))
    system.add_movie(Movie("The Dark Knight", "Crime", 152, 9.1))
    
    #Theater and Screens
    theater_list = [
        ("AMC The Grove 14", "Los Angeles, CA"),
        ("AMC The Americana at Brand 18", "Glendale, CA"), 
        ("AMC Marina Marketplace 6", "Marina Del Rey, CA")
    ]
    
    for name, location in theater_list: 
        theater = Theater(name, location)
        for i in range(3):
            screen_id = name.replace(' ', '_').lower() + "_screen_" + str(i+1)
            screen = Screen(screen_id, theater)
            theater.screens.append(screen)
        system.add_theater(theater)
    
    #Adding shows
    system.add_show(Show("show1", system.movies[0], system.theaters[0].screens[0], "4:00 PM"))
    system.add_show(Show("show2", system.movies[1], system.theaters[0].screens[1], "6:00 PM"))
    system.add_show(Show("show3", system.movies[2], system.theaters[1].screens[0], "5:00 PM"))
    system.add_show(Show("show4", system.movies[3], system.theaters[1].screens[2], "7:30 PM"))
    system.add_show(Show("show5", system.movies[4], system.theaters[2].screens[1], "9:00 PM"))

    # Print results
    print("\n--- Movies ---")
    for i, movie in enumerate(system.movies, 1):
        print(str(i) + ". " + movie.title + " (" + movie.genre + ", " + str(movie.duration) + " min, Rating: " + str(movie.rating) + ")")
    
    print("\n--- Theaters ---")
    for i, theater in enumerate(system.theaters, 1):
        print(str(i) + ". " + theater.name + " located in " + theater.location)

    print("\n--- Shows ---")
    for i, show in enumerate(system.shows.values(), 1):
        print(str(i) + ". " + show.movie.title + " - " + show.time + " in " + show.screen.screen_id + " (" + show.screen.theater.name + ")")

if __name__ == "__main__":
    main()
