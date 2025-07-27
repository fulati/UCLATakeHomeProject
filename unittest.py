import unittest
from datetime import datetime
from movie_booking_system import MovieBookingSystem
from classes import Movie, Theater, Screen, Show

class TestMovieBookingSystem(unittest.TestCase): 
    def setUp(self):
        self.system = MovieBookingSystem()
        self.movie = Movie("Inception", "Sci-Fi", 148, 8.8)
        self.system.add_movie(self.movie)
        
        self.theater = Theater("AMC The Grove 14", "Los Angeles, CA")
        screen = Screen("screen1")
        self.theater.screen.append(screen)
        self.system.add_theater(self.theater)
        
        self.show = Show("show1", self.movie, self.theater, screen, datetime(2025, 8, 2, 16, 0))  
        self.system.add_show(self.show)
        
    
        