# Pythagoras Calculator

def calcAorB(nums):
    numB = nums[0]
    numC = nums[1]
    numA = (numC**2 - numB**2)**0.5
    return numA

def calcC(nums):
    numA = nums[0]
    numB = nums[1]
    numC = (numA**2 + numB**2)**0.5
    return numC

def valuesIn(lettersIn):
    while True:
        try:
            numbers = [float(input(f"Please enter value for {x}: ")) for x in lettersIn]
            if ValueError == True:
                raise ValueError
            else:
                return numbers
        except ValueError:
            print("Please enter a valid float input")



print("Welcome to Pythagoras' calculator \n1.\tFind the length of A.\n2.\tFind the length of B.\n3.\tFind the length of C.")

while True:
    try:
        selected = int(input("Please select 1, 2, or 3: "))
        if ValueError == True or selected > 3 or selected < 0:
            raise ValueError
        else:
            break
    except ValueError:
        print("Please enter a valid input (1, 2, or 3)")

if selected == 1:
    letters = ["B", "C"]
    valueOut = valuesIn(letters)
    print(f"The value for A is: {round(calcAorB(valueOut), 2)}")
elif selected == 2:
    letters = ["A", "C"]
    valueOut = valuesIn(letters)
    print(f"The value for B is: {round(calcAorB(valueOut), 2)}")
else:
    letters = ["A", "B"]
    valueOut = valuesIn(letters)
    print(f"The value for C is: {round(calcC(valueOut), 2)}")
    