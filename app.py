print("Hello world")

# Exercise 1

books = {"author1" : ["book1", "book2", "book3"], "author2" : ["book1", "book2"]}

author = books.get(input("Please enter an author: "), "nope")

if author != "nope":
    authStr = ', '.join(author)
    print(authStr)
else:
    print("nah homie")
