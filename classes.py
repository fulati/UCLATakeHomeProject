#Imports
import uuid
from typing import List, Set
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

#Screen Class (screen_id, rows, seats_per_row)
class Screen:
    def __init__(self, screen_id: str, rows: int = 10, seats_per_row: int = 10):
        self.screen_id = screen_id
        self.seats = []
        self.seat_ids = set()
        
        #Create 10 x 10 seats selection from "A1" to "J10".
        for r in range(rows):
            row_list = []
            row_char = chr(65 + r) #row 'A' to 'J'
            for seat_num in range(1, seats_per_row + 1): # seats 1 - 10
                seat_id = row_char + str(seat_num)
                row_list.append(seat_id)
                self.seat_ids.add(seat_id)
            self.seats.append(row_list)

#Show Class (show_id, movie, screen, time)
class Show:
    def __init__(self, show_id: str, movie: Movie, theater: Theater, screen: Screen, time: datetime):
        self.show_id = show_id
        self.movie = movie
        self.theater = theater
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