print("Hello world")

# Exercise 1

books = {"author1" : ["book1", "book2", "book3"], "author2" : ["book1", "book2"]}

author = books.get("author1", "nope")
str = ', '.join(author)

print(str)
