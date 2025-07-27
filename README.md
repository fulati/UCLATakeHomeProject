# UCLATakeHomeProject

SWE Technical Challenge: Design a Movie Ticket Booking System

# Movie Ticket Booking System

## Overview

A command-line application to search movies, view showtimes, book and cancel seats given from the requirements.

## Features

- Search movies by title
- View available showtimes for a movie
- Reserve seats for a show 
- Cancel bookings by ID
- List all bookings for a user

## Core Methods

- `search_movies(query: str) -> List[Movie]`  
- `list_showtimes(movie_title: str) -> List[Show]`
- `book_seats(show_id: str, seats: List[str]) -> bool`  
- `cancel_booking(booking_id: str) -> bool` 

## How to Run

```bash
python movie_booking_system.py
