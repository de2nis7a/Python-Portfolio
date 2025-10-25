# FILE: art_gallery_management_system.py
# CONCEPT: Object-Oriented Programming (OOP) - Composition, Aggregation, and State Check
# DEMONSTRATES: Hierarchical relationship (Gallery holds Exhibitions, Exhibition holds ArtPieces), 
#               aggregation (total price calculation), and managing presentation state.

class ArtPiece:

    def __init__(self, title, artist, initial_price):
        self.title = title
        self.artist = artist
        self._price = initial_price
        
    @property
    def price(self):
        return self._price
    
    def increase_price(self, amount):
        self._price += amount
        
    def __str__(self):
        output = f"Art Piece '{self.title}' by {self.artist} (Value: {self._price})"
        return output
    
class Exhibition:
    
    def __init__(self, name, start_date, end_date):
        self.name = name
        self.pieces = set()
        self._price = 0
        self.start_date = start_date
        self.end_date = end_date
        
    def add_art_piece(self, art_piece):
        self.pieces.add(art_piece)
        
    def remove_art_piece(self, art_piece):
        self.pieces.remove(art_piece)
        
    # NOTE: Calculated properties should be methods, not simple attributes
    @property
    def price(self):
        # Calculate price dynamically based on current pieces
        total_price = sum(piece.price for piece in self.pieces)
        return total_price
    
    @property
    def nr_pieces(self):
        return len(self.pieces)
        
    def __str__(self):
        output = f"Exhibition '{self.name}' ({self.start_date} - {self.end_date}). Total Value: {self.price}. Pieces:"
        for piece in self.pieces:
            output += f" \n - {piece}"
        return output
    
class Gallery:
    
    def __init__(self, name):
        self.name = name
        self.exhibitions = [] # Use instance attribute
        self._total_value = 0
    
    @property
    def total_value(self):
        # Calculate total value dynamically
        return sum(exh.price for exh in self.exhibitions)
    
    @property
    def nr_exhibitions(self):
        return len(self.exhibitions)
        
    def add_exhibition(self, exhibition):
        self.exhibitions.append(exhibition)
        
    def remove_exhibition(self, exhibition):
        if exhibition in self.exhibitions:
            self.exhibitions.remove(exhibition)
        
    def present_exhibition(self, nr_exhibition):
        # Convert 1-based index to 0-based
        index = nr_exhibition - 1
        
        if 0 <= index < len(self.exhibitions):
            exhibition = self.exhibitions[index]
            
            if isinstance(exhibition, Exhibition):
                 output = f"\n The exhibition number {nr_exhibition} is: \n {exhibition}"
                 # Mark as 'presented' by changing the list element (simulating state change)
                 self.exhibitions[index] = "presented" 
            else:
                 output = f"\n The exhibition {nr_exhibition} was already presented (State: {exhibition})"
        else:
            output = f"Exhibition number {nr_exhibition} does not exist."
        return output
        
    def __str__(self):
         output = f"Gallery '{self.name}' comprising {self.nr_exhibitions} exhibitions. Total Art Value: {self.total_value}."
         return output
    
    
def test_galley():
    piece = ArtPiece("A1", "Ion", 1000)
    piece2 = ArtPiece("A2", "Io", 100)
    piece3 = ArtPiece("A3", "Iodd", 100)
    
    exhibition1 = Exhibition("Modern Abstracts", "22.04.2000", "22.09.2000")
    exhibition2 = Exhibition("Romanian Masters", "22.04.2009", "22.09.2010")
    
    exhibition1.add_art_piece(piece)
    exhibition1.add_art_piece(piece2)
    exhibition2.add_art_piece(piece3)
    
    gallery = Gallery("National Gallery")
    gallery.add_exhibition(exhibition1)
    gallery.add_exhibition(exhibition2)
    
    print(gallery)
    print(gallery.present_exhibition(2))
    
    exhibition1.remove_art_piece(piece) # Total value should update
    piece2.increase_price(100)
    
    print(gallery) # Check updated total value
    print(gallery.present_exhibition(2)) # Should say "already presented"
    print(gallery.present_exhibition(1)) # Should print details and set to "presented"

if __name__ == "__main__":
    test_galley()
