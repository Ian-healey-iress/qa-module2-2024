# write an application that checks the strength of a password.
# Requirements:
# 
# Write a class that has a method that checks the password strength.
# Use factors like length, upper/lower case and if it has a number and special character.
# ratings should be very weak - weak - moderate - strong - very strong 
# Check against a list of common passwords 10-20 common password = very weak
# User input that loops until the user quits

# 1st stretch goal: A dictionary that returns a history of passwords/strengths whilst in the loop.

# 2nd Stretch goal:
# write tests and achieve a high score in pylint.

# Code must be pushed to a repo or emailed to me. 

# Deadline is 3pm. 

"""Module that checks the strength of a password"""

class Pass:
    """Class for actual password object"""
    def __init__(self, password):
        """Init method that sets attributes and determines characteristics of password"""
        self.password = password
        self.passLength = len(password)
        self.specialChars = "!\"#$%&'()*+,-./:;<=>?@[]^_`{|}~\\"
        self.commonPasses = ["pass", "Pass", "password", "Password", "password123", "Password123", "password999", "Password999", "password123!", "Password123!", "password999!", "Password999!"]
        self.isCommonPass = False
        if any(c in self.specialChars for c in self.password):
            self.containsSpecialChars = True
        else:
            self.containsSpecialChars = False
        if any(c.isupper() for c in self.password):
            self.containsUpperChars = True
        else:
            self.containsUpperChars = False
        if any(c.islower() for c in self.password):
            self.containsLowerChars = True
        else:
            self.containsLowerChars = False
        if any(c.isdigit() for c in self.password):
            self.containsNums = True
        else:
            self.containsNums = False
        if self.passLength >= 8:
            self.sufficientLength = True
        else:
            self.sufficientLength = False
        for c in self.commonPasses:
            if password == c:
                self.isCommonPass = True


    def __str__(self):
        """str method to return a string representation"""
        return f"Pass: {self.password} - Special: {self.containsSpecialChars} - Uppercase: {self.containsUpperChars} - Lowercase: {self.containsLowerChars} - Numbers: {self.containsNums}"

class PassCheck:
    """Class that contains password check logic"""
    def __init__(self):
        """Init method to set attributes"""
        self.passScore = 0
        self.passImprovements = []
        
    def returnScore(self):
        """Function that returns string based on password score, there is no 0 check as the user will not be able to enter empty password"""
        if self.passScore == 1:
            return "very weak"
        elif self.passScore == 2:
            return "weak"
        elif self.passScore == 3:
            return "moderate"
        elif self.passScore == 4:
            return "strong"
        else:
            return "very strong"

    def returnImprovements(self):
        """Function that returns the improvements for a password"""
        if not self.passImprovements:
            return "The password doesn't require improvments"
        else:
            return self.passImprovements
        
    def checkPassword(self, password):
        """Function that checks attributes of password object, returns the password strength and list of improvements"""
        self.__init__()
        if password.containsSpecialChars is True:
            self.passScore += 1
        else:
            self.passImprovements.append("Add special characters")
        if password.containsUpperChars is True:
            self.passScore += 1
        else:
            self.passImprovements.append("Add uppercase characters")
        if password.containsLowerChars is True:
            self.passScore += 1
        else:
            self.passImprovements.append("Add lowercase characters")
        if password.containsNums is True:
            self.passScore += 1
        else:
            self.passImprovements.append("Add numbers")
        if password.sufficientLength is True:
            self.passScore += 1
        else:
            self.passImprovements.append("Make sure password contains more than 8 charaters")
        if password.isCommonPass is True:
            self.passScore = 1
            self.passImprovements = ["Refrain from using a password that is commonly used by others (password, password123, etc.)"]
        return self.returnScore(), self.returnImprovements()
    
    def __str__(self):
        """str method to return a string representation"""
        return f"Name: {__class__.__name__} PassScore: {self.passScore} - PassImprovements: {self.passImprovements}"

class PassHistory:
    """Class that stores the history and strength of previously inputted passwords"""
    def __init__(self):
        """Function that initializes the class and its attributes"""
        self.passHistory = []
    
    def addPass(self, password, strength):
        """Function that adds a password and strength to the passHistory list"""
        self.passHistory.append([password, strength])
    
    def getPassHistory(self):
        """Function that returns the list of previous passwords"""
        return self.passHistory
    
check = PassCheck()
passHist = PassHistory()

mainMenu = {
    1 : "Check a password's strength",
    2 : "Retrieve password history",
    3 : "Quit"
}
def main():
    while True:
        try:
            print("Menu:")
            for x in mainMenu:
                print(f"{list(mainMenu.keys())[x-1]}.\t{list(mainMenu.values())[x-1]}")
            selected = int(input("Please select: "))
            if ValueError is True or selected > 3 or selected < 1:
                raise ValueError
            else:
                if selected == 1:
                    password = Pass(input("Please enter a password: "))
                    print(f"Your password's strength is {check.checkPassword(password)[0]}")

                    count = 1
                    if check.checkPassword(password)[1] == "The password doesn't require improvments":
                        print(check.checkPassword(password)[1])
                    else:
                        print("To improve your password you should: ")
                        for i in check.checkPassword(password)[1]:
                            print(f"{count}.\t{i}")
                            count += 1
                    passHist.addPass(password, check.checkPassword(password)[0])
                elif selected == 2:
                    print("Previous Passwords: ")
                    for p in passHist.getPassHistory():
                        print(f"Password: {p[0].password}, Strength: {p[1]}")
                elif selected == 3:
                    quit()
        except ValueError:
            print("Please enter a valid input (1-5)")
