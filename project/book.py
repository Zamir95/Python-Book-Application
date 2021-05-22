class Book:
    def __init__(self, id, name, description, isbn, page_count, issued, author, year): # set variables for each when looking up the book
        self.id = id 
        self.name = name
        self.description = description
        self.isbn = isbn
        self.page_count = page_count
        self.issued = issued
        self.author = author
        self.year = year
    # to_dict method

    def to_dict(self):
        dictionary = {
            "id": self.id, #gets 1d
            "name": self.name, #gets name of book
            "description": self.description, #gets description of book
            "isbn": self.isbn, #gets isbn of book
            "page_count": self.page_count, #gets page count of book
            "issued": self.issued, #gets whether book is published or not
            "author": self.author, #gets author name
            "year": self.year #gets year book was published
        } 
        return dictionary


#book = Book(12, "atomic habits", "building habits", "213--52-325-23", 234, True, "Zamir Lalji", 2018) # array is printed once you return Dictionary 

#print(book.to_dict())