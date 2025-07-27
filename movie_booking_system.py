from typing import List, Dict
from classes import Movie, Theater, Screen, Show, Booking
from data_file import get_movies, get_theaters, get_shows

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
        
        theater = show.theater
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

        #Store invalid seats
        invalid = []
        for seat in seats: 
            if seat not in show.screen.seat_ids: 
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
    
    # Load data
    movies = get_movies()
    theaters = get_theaters()
    shows = get_shows(movies, theaters)

    for movie in movies:
        system.add_movie(movie)

    for theater in theaters:
        system.add_theater(theater)

    for show in shows:
        system.add_show(show)


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
                    print(show.show_id + ": " + show.movie.title + " at " + show.time + " in " + show.screen.screen_id)
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
                    print("  Theater: " + booking.show.theater.name)
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
