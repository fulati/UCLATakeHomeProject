# UCLATakeHomeProject

SWE Technical Challenge: Design a Movie Ticket Booking System

Problem Statement

Design and implement a simplified movie ticket booking system.

You should support:

Searching movies
Viewing available showtimes
Reserving seats for a show
Preventing double-booking of seats
Requirements

Entities to model:

Movie (title, genre, duration, rating)
Theater (name, location)
Screen (within a theater, has rows and seats)
Show (movie + screen + time)
Booking (user, show, seat(s), timestamp)
Features:

search_movies(query: str) -> List[Movie]
list_showtimes(movie_title: str) -> List[Show]
book_seats(show_id: str, seats: List[str]) -> bool
Return True if booking successful, False if any seat is already booked.
Optional: cancel_booking(booking_id: str)
 

Example Flow

system.search_movies("Inception")

system.list_showtimes("Inception")

system.book_seats("show_abc", ["A1", "A2"])  # ✅ Success

system.book_seats("show_abc", ["A2", "A3"])  # ❌ A2 already booked

 

Constraints

In-memory data store is fine.
You can assume a fixed layout for screens (e.g., 10 rows × 10 seats).
You may use any OOP language (Python, Java, etc.).
No need for user auth or payment — focus on core booking logic.