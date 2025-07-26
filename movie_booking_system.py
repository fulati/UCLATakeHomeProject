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
        
    #show_available_seats function
    def show_available_seats(self, show_id: str) -> None:
        show = self.shows.get(show_id)
        
        #Check if valid show_id
        if not show:
            print("Show not found.")
            return 
        
        theater = show.screen.theater
        print("Available seats for " + show.movie.title + " at " + show.time + " in " + theater.name + " (" + theater.location + "): ")
        
        for row in show.screen.seats: 
            row_seats = []
            for seat in row:
                if seat in show.booked_seats: 
                    row_seats.append("XX")
                else: 
                    row_seats.append(seat)
            print(" ".join(row_seats))

    #search_movies function
    def search_movies(self, query: str) -> List[Movie]: 
        results: List[Movie] = []
        
        for movie in self.movies:
            if query.lower() in movie.title.lower():
                results.append(movie)
        
        return results

    #list_showtime function
    def list_showtimes(self, movie_title: str) -> List[Show]:
        results: List[Show] = []
        
        for show in self.shows.values(): 
            if show.movie.title.lower() == movie_title.lower():
                results.append(show)
        
        return results

    #book_seats function
    def book_seats(self, show_id: str, seats: List[str], user: str = "anonymous") -> bool: 
        show = self.shows.get(show_id)

        #Check if valid show_id
        if not show:
            print("Show not found.")
            return False
        
        #Store all seat ID in a list
        all_seats = []
        for row in show.screen.seats:
            for seat in row:
                all_seats.append(seat)

        #Store invalid seats
        invalid = []
        for seat in seats: 
            if seat not in all_seats: 
                invalid.append(seat)  
                
        #Check if valid seat ID
        if invalid:
            print("Invalid seats: " + ", ".join(invalid))
            return False

        #Store already booked seats
        already_booked = []
        for seat in seats:
            if seat in show.booked_seats: 
                already_booked.append(seat)
                
        #Check if seat already booked       
        if already_booked: 
            print("Seats already booked: " + ", ".join(already_booked))
            return False
        
        #Purchase the seats
        for seat in seats: 
            show.booked_seats.add(seat)
        
        booking = Booking(user, show, seats)
        self.bookings[booking.booking_id] = booking
        print("Successfully booked seats: " + str(seats))
        print("Your Booking ID is: " + booking.booking_id)
        return True


    #cancel_bookings function
    def cancel_booking(self, booking_id: str) -> bool: 
        booking = self.bookings.get(booking_id)
        
        if not booking: 
            print("Booking doesn't exist!")
            return False
    
        for seat in booking.seats: 
            booking.show.booked_seats.discard(seat)
            
        del self.bookings[booking_id]
        print("Booking cancelled!")
        return True


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
    
    show_counter = 1
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


    #Command Line Interface
    print("Welcome to Movie Booking System")
    
    while True:
        print("\n---------------------- OPTIONS: ----------------------")
        print("1. View all movies")
        print("2. Search movie")
        print("3. View all shows")
        print("4. View showtimes for a movie")
        print("5. Show available seats for a show")
        print("6. Book seats")
        print("7. Cancel a booking")
        print("8. Show all bookings by user")
        print("0. Exit")
        print()


        choice = input("Select an option: ")
        
        if choice == "1":
            print()
            for movie in system.movies:
                print("* " + movie.title + " (" + movie.genre + ", " + str(movie.duration) + " mins, Rating: " + str(movie.rating) + ")")

        elif choice == "2":
            print()
            title = input("Enter movie title to search: ")
            results = system.search_movies(title)
            if results:
                print("Movies Found: ")
                for movie in results:
                    print("* " + movie.title)
            else:
                print("No movie found.")

        elif choice == "3":
            print()
            for show_id, show in system.shows.items():
                print(show_id + ": " + show.movie.title + " at " + show.time + " in " + show.screen.screen_id)

        elif choice == "4":
            print()
            title = input("Enter movie title: ")
            results = system.list_showtimes(title)
            if results:
                print("Show times for " + title)
                for show in results:
                    print(show.show_id + ": " + show.movie.title + " at " + show.time)
            else:
                print("No showtimes found.")

        elif choice == "5":
            print()
            show_id = input("Enter show ID: ")
            system.show_available_seats(show_id)

        elif choice == "6":
            print()
            user = input("Enter your name: ").strip()
            if not user: 
                print("Name cannot be empty.")
                continue
            show_id = input("Enter show ID: ")
            seats = input("Enter seat IDs separated by commas (e.g. A1,A2): ").replace(" ", "").split(",")
            booked = system.book_seats(show_id, seats, user)
            if not booked: 
                print("Booking failed.")

        elif choice == "7":
            print()
            booking_id = input("Enter booking ID to cancel: ")
            system.cancel_booking(booking_id)
            
        elif choice == "8":
            print()
            name = input("Enter your name: ").strip()
            found = False
            for booking in system.bookings.values():
                if booking.user.lower() == name.lower():
                    found = True
                    print("* Booking ID: " + booking.booking_id)
                    print("  Show: " + booking.show.movie.title + " at " + booking.show.time)
                    print("  Seats: " + ", ".join(booking.seats))
                    print("  Theater: " + booking.show.screen.theater.name)
                    print()
            if not found: 
                print("No bookings found for " + name + ".")

        elif choice == "0":
            print()
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
