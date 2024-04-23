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

names = [print(f"{name} is great") for name in [input("Enter name: ") for x in range(5)]]

