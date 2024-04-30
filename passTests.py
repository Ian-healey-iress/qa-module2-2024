import unittest
from passChecker import Pass, PassCheck, PassHistory

"""Module that unit tests the objects in passChecker.py"""

class TestPass(unittest.TestCase):

    def test_pass_class_exists(self):
        password = Pass("Test")
        self.assertIsInstance(password, Pass)

    def test_passCheck_class_exists(self):
        passCheck = PassCheck()
        self.assertIsInstance(passCheck, PassCheck)
    
    def test_passHistory_class_exists(self):
        passHist = PassHistory()
        self.assertIsInstance(passHist, PassHistory)

    def test_passCheck_checkPassword_returns_correct_object_type(self):
        password = Pass("Test")
        passCheck = PassCheck()
        self.assertIsInstance(passCheck.checkPassword(password), tuple)

    def test_passCheck_checkPassword_returns_correct_strengths(self):
        passwordVeryWeak = Pass("Password")
        passwordWeak = Pass("Test")
        passwordModerate = Pass("Test1")
        passwordStrong = Pass("Test1234")
        passwordVeryStrong = Pass("Test1234!?!")
        passCheck = PassCheck()
        self.assertEqual(passCheck.checkPassword(passwordVeryWeak)[0], ('very weak'))
        self.assertEqual(passCheck.checkPassword(passwordWeak)[0], ('weak'))
        self.assertEqual(passCheck.checkPassword(passwordModerate)[0], ('moderate'))
        self.assertEqual(passCheck.checkPassword(passwordStrong)[0], ('strong'))
        self.assertEqual(passCheck.checkPassword(passwordVeryStrong)[0], ('very strong'))

    def test_passCheck_checkPassword_returns_correct_improvements(self):
        improveList = ["Add special characters", "Add uppercase characters", "Add lowercase characters", "Add numbers", "Make sure password contains more than 8 charaters", "Refrain from using a password that is commonly used by others (password, password123, etc.)"]
        passwordSpecial = Pass("Test1234")
        passwordUpper = Pass("test1234!")
        passwordLower = Pass("TEST1234!?!")
        passwordNumbers = Pass("Test!?!?!")
        passwordShort = Pass("Tes1!")
        passwordCommon = Pass("Password")
        passCheck = PassCheck()
        self.assertEqual(passCheck.checkPassword(passwordSpecial)[1], [improveList[0]])
        self.assertEqual(passCheck.checkPassword(passwordUpper)[1], [improveList[1]])
        self.assertEqual(passCheck.checkPassword(passwordLower)[1], [improveList[2]])
        self.assertEqual(passCheck.checkPassword(passwordNumbers)[1], [improveList[3]])
        self.assertEqual(passCheck.checkPassword(passwordShort)[1], [improveList[4]])
        self.assertEqual(passCheck.checkPassword(passwordCommon)[1], [improveList[5]])


if __name__ == '__main__':
    unittest.main()