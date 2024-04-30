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


if __name__ == '__main__':
    unittest.main()