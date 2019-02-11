import unittest # Importing the unittest module
from user import Account # Importing the account class

class TestAccount(unittest.TestCase):

    '''
    Test class that defines test cases for the account  class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
        '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = Account("facebook","mazimpaka","0786950337ro") # create account object
        ''

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.account_name,"facebook")
        self.assertEqual(self.new_account.user_name,"mazimpaka")
        self.assertEqual(self.new_account.password,"0786950337ro")
        


if __name__ == '__main__':
    unittest.main()

    def test_save_account(self):
        '''
        test_save_account test case to test if the account object is saved into
         the account list
        '''
        self.new_account.save_account() # saving the new account
        self.assertEqual(len(Account.account_list),1)

if __name__ ==  '__main__':
    unittest.main()  
