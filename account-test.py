import unittest # Importing the unittest module
from account import accountt # Importing the account class

class TestAccount(unittest.TestCase):

    '''
    Test class that defines test cases for the account  class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    'def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = account("facebook","mazimpaka","0786950337ro") # create account object
''

def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.first_name,"facebook")
        self.assertEqual(self.new_account.last_name,"mazimpakar")
        self.assertEqual(self.new_account.password,"0786950337ro")
        


if __name__ == '__main__':
    unittest.main()
