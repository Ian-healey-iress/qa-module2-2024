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


#  Exercose 3

weight = float(input("Enter Weight: "))

userIn = "invalid"

while True:
    unit = input("Select unit (1 for kg or 2 for lbs): ")
    if unit == "1" or unit == "2":
        break
    else:
        print("Invalid input, please try again")
        
if unit == "1":
    print(f"Your weight is {weight} kgs, or {round(weight * 2.2, 2)} lbs")
else:
    print(f"Your weight is {weight} lbs, or {round(weight / 2.2, 2)} kgs")
