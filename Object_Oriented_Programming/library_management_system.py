# FILE: library_management_system.py
# CONCEPT: Object-Oriented Programming (OOP) - Polymorphism and State Tracking
# DEMONSTRATES: Managing availability state, inheritance (DigitalBook), and polymorphism 
#               (overriding methods like borrow/return in DigitalBook).

class Book:

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self._available = True
        
    @property
    def available(self):
        # Corrected typo in original code
        return self._available 

    def borrow_book(self):
        self._available = False

    def return_book(self):
        self._available = True

    def __str__(self):
        output = f"Book's title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"
        output += f"\n  Available: {self._available}"
        return output


class DigitalBook(Book):
    
    compatible_devices = {"PDF", "Kindle", "Apple"}

    def __init__(self, title, author, isbn):
        super().__init__(title, author, isbn)
        self._compatibility = {"Kindle"}
        
    @property    
    def compatibility(self):
        return self._compatibility
    
    @compatibility.setter
    def compatibility(self, new_compatibility):
        if new_compatibility in self.compatible_devices:
            # Adds the new device to the set of compatible devices
            self._compatibility.add(new_compatibility)
        
    def borrow_book(self):
        pass

    def return_book(self):
        pass
    
    def __str__(self):
        output = f"Digital Book: {self.title}, Author: {self.author}, ISBN: {self.isbn}"
        output += f"\n  Available: Always. Compatibility: {', '.join(self._compatibility)}"
        return output


class Library:

    def __init__(self):
        self.books = []
        self.messages = []
        
    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and isinstance(book, Book):
                if book.available == True:
                    book.borrow_book()
                    self.messages.append(f"Successfully borrowed: {title}")
                else:
                    self.messages.append(f"The book '{title}' is not available for physical borrowing.")
                return 

    def return_book(self, title):
        for book in self.books:
            if book.title == title and isinstance(book, Book):
                if book.available == False:
                    book.return_book()
                    self.messages.append(f"Successfully returned: {title}")
                else:
                    self.messages.append(f"The book '{title}' is already returned or is digital.")
                return

    def __str__(self):
        output = "--- Library Catalog ---\n"
        for book in self.books:
            output += f"{book}\n"
        output += "\n--- Library Messages ---\n"
        output += "\n".join(self.messages)
        return output


def test_book():
    book = Book('Frankenstein', 'Mary Shelley', '978-0486282114')
    
    digital_book = DigitalBook(
        'Orlando: A Biography', 'Virginia Woolf', '978-0156031516')
    digital_book.compatibility = "PDF"
    digital_book.compatibility = "Kindle"
    digital_book.compatibility = "Apple"
    
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")
    book2 = Book("1984", "George Orwell", "978-0451524935")
    
    library = Library()
    library.add_book(book)
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(digital_book)
    
    library.borrow_book('Frankenstein')
    library.borrow_book('Frankenstein') # Test unavailable
    library.return_book('Frankenstein')
    library.return_book('Frankenstein') # Test already returned
    
    print(library)


if __name__ == "__main__":
    test_book()
