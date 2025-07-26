#Imports
import uuid
from typing import List, Set
from datetime import datetime


#Movie Class (title, genre, duration, rating)
class Movie:
    def __init__(self, title: str, genre: str, duration: int, rating: int):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.rating = rating

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

    #search_movies function


    #list_showtime function


    #book_seats function


    #cancel_bookings function



#Main

