print("Hello world")

# Exercise 1

# books = {"author1" : ["book1", "book2", "book3"], "author2" : ["book1", "book2"]}

# author = books.get(input("Please enter an author: "), "nope")

# if author != "nope":
#     authStr = ', '.join(author)
#     print(authStr)
# else:
#     print("nah homie")


# Exercise 2

# grade = int(input("Enter Grade: "))

# if grade >= 85:
#     print("Distinction")
# elif grade >= 65:
#     print("Pass")
# else:
#     print("Fail")


#  Exercise 3

# while True:     
#     try:
#         weight = float(input("Enter Weight: "))
#         if ValueError == True:
#             raise ValueError
#         else:
#             break
#     except ValueError:
#         print("Please enter a numberic input")

# userIn = "invalid"

# while True:
#     unit = input("Select unit (1 for kg or 2 for lbs): ")
#     if unit == "1" or unit == "2":
#         if unit == "1":
#             converted = round(weight * 2.2, 1)
#             convertedUnit = "lbs"
#         else:
#             converted = round(weight / 2.2, 1)
#             convertedUnit = "kgs"
#         break
#     else:
#         print("Invalid input, please try again")     

# print(f"your weight is {converted} {convertedUnit}")


# Exercise 4

# names = [print(f"{name} is great") for name in [input("Enter name: ") for x in range(5)]]


# Exercise 5

# def findBudget():
#     while True:     
#         try:
#             budget = float(input("Enter Budget: "))
#             if ValueError == True:
#                 raise ValueError
#             else:
#                 return budget
#         except ValueError:
#             print("Please enter a numberic input")

# def retriveUserIn():
#     while True:
#         try:
#             selected = int(input("Please select 1, 2, or 3: "))
#             if ValueError == True or selected > 3 or selected < 0:
#                 raise ValueError
#             else:
#                 return selected
#         except ValueError:
#             print("Please enter a valid input (1, 2, or 3)")

# shakes = {
#     "Shake 1" : 10,
#     "Shake 2" : 8.50,
#     "Shake 3" : 6.45
# }

# budget = findBudget()

# print("Menu:")
# counter = 0
# for shake in shakes:
#     counter+=1
#     print(f"{counter}.\t{shake}")

# purchased = []

# while True:
#     selected = retriveUserIn()
#     if list(shakes.values())[selected - 1] > budget:
#         print(f"you cant afford that, your budget is only {budget}")
#     else:
#         purchased.append(str(list(shakes.keys())[selected - 1]))
#         budget -= list(shakes.values())[selected - 1]
#         print("So far you have bought:")
#         for x in purchased:
#             print(x)
#         print(f"you have {round(budget, 1)} left")

#     if min(list(shakes.values())) > budget:
#         print("You haven't got enough money to buy anything, you have been kicked out")
#         quit()

# Exercise 6

# def oddOrEven(num):
#     if num%2 == 1:
#         return "odd"
#     else:
#         return "even"

# while True:
#     try:
#         num = int(input(f"Please enter a number: "))
#         if ValueError == True:
#             raise ValueError
#         else:
#             print(f"{num} is {oddOrEven(num)}.")
#             break
#     except ValueError:
#         print("Please enter a valid integer input")  


#Harder challenge (stretch goal): 

#Create a Book class and BookShelf class that can be used to manage a collection of books. 
#Create a Book class that has the following attributes: 
#title (str), author (str), publisher (str), publication year (int). 
#The class should also have a str method that returns the book's information in a 
#formatted string. 
#Create a BookShelf class that has the following attributes: 
#capacity (int), list of books (list). 
#The class should have the following methods: 
#- add_book: adds a book to the list of books if the shelf is not full 
#- remove_book: removes a book from the list of books if it exists on the shelf 
#- find_book_by_title: searches for a book by its title 
#and returns the book object if found 
#- find_books_by_author: searches for books by a specific author 
#and returns a list of book objects if found 
#The class should also have a str method that returns a string representation 
#of the books on the shelf. 

#Create four Book objects and add them to a BookShelf object with a capacity of three. 
#Test the BookShelf object by adding, removing, and finding books by title and author.
#Print the BookShelf object after each action.

class Book:
    def __init__(self, title, author, publisher, year):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year

    def __str__(self):
        return f"{self.title} - {self.author} - {self.publisher} - {self.year}"

class BookShelf:
    def __init__(self, capacity):
        self.capacity = capacity
        self.bookList = []
    
    def addBook(self, book):
        if len(self.bookList) < self.capacity:
            self.bookList.append(book)
            return f"Added {book.title} to bookshelf"
        else:
            return "Bookshelf full"

    def removeBook(self, book):
        if book in self.bookList:
            self.bookList.remove(book)
            return f"Removed {book.title} from bookshelf"
        else:
            return "Book not in bookshelf"
    
    def getBookByTitle(self, title):
        for b in self.bookList:
            if b.title == title:
                return b
            else:
                return "no books found"
    
    def getBookByAuthor(self, author):
        for b in self.bookList:
            if b.author == author:
                return b
            else:
                return "no books found"
    
    def __str__(self):
        books = [f"{b.__str__()}" for b in self.bookList]
        return books

book1 = Book("t1", "a1", "p1", "y1")
book2 = Book("t2", "a2", "p2", "y2")
shelf = BookShelf(1)

print(shelf.addBook(book1))
print(shelf.__str__())
print(shelf.addBook(book2))
print(shelf.__str__())
print(shelf.getBookByTitle('t1'))
print(shelf.getBookByTitle('x'))
print(shelf.getBookByAuthor('a1'))
print(shelf.getBookByAuthor('x'))
print(shelf.removeBook(book1))
print(shelf.__str__())
