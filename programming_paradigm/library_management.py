#library_management

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out= False

    def check_out(self):
       """Mark the book as checked out if it is not already."""
       if not self._is_checked_out:
        self._is_checked_out = True
        return True
       return False
         
    def return_book(self):
       """Mark the book as available again."""
       if self._is_checked_out:
          self._is_checked_out = False
          return True
       return False
       
    def is_available(self):
       """Return True if the book is not checked out."""
       return not self._is_checked_out



class Library:
   
    def __init__(self):
        self._books = []  # private list of book objects

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"'{title}' has been checked out.")
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"Book titled '{title}' not found in the library.")

    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"'{title}' has been returned.")
                else:
                    print(f"'{title}' was not checked out.")
                return
        print(f"Book titled '{title}' not found in the library.")

    def list_available_books(self):
        """Print all available books."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")