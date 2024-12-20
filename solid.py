from abc import ABC, abstractmethod

# Abstract class for table reservation
class Reservation(ABC):
    """Abstract class representing a reservation system"""

    @abstractmethod
    def reserve_table(self, name, number_of_people):
        pass


# Class for regular reservation
class RegularReservation(Reservation):
    def reserve_table(self, name, number_of_people):
        print(f"Regular Reservation: Table reserved for {name} for {number_of_people} people.")


# Class for VIP reservation
class VIPReservation(Reservation):
    def reserve_table(self, name, number_of_people):
        print(f"VIP Reservation: Exclusive table reserved for {name} with priority service for {number_of_people} people.")


# Class for outdoor reservation
class OutdoorReservation(Reservation):
    def reserve_table(self, name, number_of_people):
        print(f"Outdoor Reservation: Table reserved for {name} in the outdoor seating area for {number_of_people} people.")


# Context class for managing reservations
class Restaurant:
    def __init__(self, reservation_strategy: Reservation):
        self.reservation_strategy = reservation_strategy

    def make_reservation(self, name, number_of_people):
        self.reservation_strategy.reserve_table(name, number_of_people)


# Usage
# Regular reservation
restaurant_regular = Restaurant(RegularReservation())
restaurant_regular.make_reservation("Alice", 4)

# VIP reservation
restaurant_vip = Restaurant(VIPReservation())
restaurant_vip.make_reservation("Bob", 2)

# Outdoor reservation
restaurant_outdoor = Restaurant(OutdoorReservation())
restaurant_outdoor.make_reservation("Charlie", 6)
