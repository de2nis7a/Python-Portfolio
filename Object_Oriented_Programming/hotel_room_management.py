# FILE: hotel_room_management.py
# CONCEPT: Object-Oriented Programming (OOP) - Conditional State
# DEMONSTRATES: Using methods (check_in, check_out) to manage state (occupancy) and boolean return values.

class HotelRoom:
    def __init__(self, room_number):
        self.room_number = room_number
        self.guest_name = ""
    
    def check_in(self, guest_name):
        if self.guest_name == "":
            self.guest_name = guest_name
            
    def check_out(self, name):
        if self.guest_name == name:
            self.guest_name = ""
        
    def is_occupied(self, name):
        if self.guest_name == "":
            return False
        elif self.guest_name == name:
            return True
        else:
            return False
    
    def __str__(self):
        if self.guest_name != "":
            return f"Room number {self.room_number} is occupied by {self.guest_name}"
        else:
            return f"Room number {self.room_number} is vacant"
            
def test_hotel_room():
    room = HotelRoom(101)
    occ = room.is_occupied("Winston")
    print(occ)
    print(room)
    room.check_in("Winston")
    print(room)
    occ = room.is_occupied("Winston")
    print(occ)
    room.check_out("Winston")
    print(room)

if __name__ == "__main__":
    test_hotel_room()
