def calculateTax(income):
    if income <= 11850:
        return "0"
    if income > 11850:
        tax = income * 0.2
    if income > 34500:
        tax = income * 0.4
    if income > 150000:
        tax = income * 0.45
    return tax

while True:
    try:
        income = float(input(f"Please enter your income: "))
        if ValueError == True:
            raise ValueError
        else:
            print(f"The total tax you must pay is {calculateTax(income)}")
            break
    except ValueError:
        print("Please enter a valid float input")

