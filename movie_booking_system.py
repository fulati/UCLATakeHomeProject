#Imports
from typing import List


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


#Show Class (show_id, movie, screen, time)


#Booking Class (user, show, seats)


#MovieBookingSystem Class with (movies, theaters, shows, bookings)

    #search_movies function


    #list_showtime function


    #book_seats function


    #cancel_bookings function



#Main

