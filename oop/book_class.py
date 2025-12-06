# Dive into Python Magic Methods


class Book:
    #Initializes a Book instance with title, author, and year.
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

        #Deleting (title of the book)
    def __del__(self):
        print(f"Deleting {self.title}")

      #Returns a string in the format "(title) by (author), published in (year)".
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
     
       #Official Representation 
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"