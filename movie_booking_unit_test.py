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
        self.theater.screens.append(screen)
        self.system.add_theater(self.theater)
        
        self.show = Show("show1", self.movie, self.theater, screen, datetime(2025, 8, 2, 16, 0))  
        self.system.add_show(self.show)
        
    def test_movie_search_success(self):
        results = self.system.search_movies("incepTion")
        self.assertTrue(self.movie in results)
        
    def test_seat_booking_success(self):
        result = self.system.book_seats("show1", ["A1", "A2"], user="fulati")
        self.assertTrue(result)
        # Check if A1 and A2 are booked
        self.assertIn("A1", self.show.booked_seats)
        self.assertIn("A2", self.show.booked_seats)
    
    def test_seat_booking_double_booking(self):
        self.system.book_seats("show1", ["A1"], user="fulati")
        # Book A1 again
        result = self.system.book_seats("show1", ["A1"], user="guest")
        self.assertFalse(result)
    
if __name__ == '__main__': 
    unittest.main()
        