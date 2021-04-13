class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

print(b1.title)
print(b2.author)

#TODO: print the book itself - dataclasses implement __repr__


#TODO: comparing two dataclasses - they implement __eq__

