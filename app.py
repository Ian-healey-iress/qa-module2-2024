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

def oddOrEven(num):
    if num%2 == 1:
        return "odd"
    else:
        return "even"

while True:
    try:
        num = int(input(f"Please enter a number: "))
        if ValueError == True:
            raise ValueError
        else:
            print(f"{num} is {oddOrEven(num)}.")
            break
    except ValueError:
        print("Please enter a valid integer input")  