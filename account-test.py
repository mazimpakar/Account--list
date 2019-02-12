import unittest # Importing the unittest module
from user import Account # Importing the Account class

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
        




    def test_save_account(self):
        '''
        test_save_account test case to test if the account object is saved into
         the account list
        '''
        self.new_account.save_account() # saving the new account
        self.assertEqual(len(Account.account_list),1)

    def test_save_multiple_account(self):
            '''
            test_save_multiple_account to check if we can save multiple account
            objects to our account_list
            '''
            self.new_account.save_account()
            test_account = Account("facebook","doudou","0788267443ro") # new account
            test_account.save_account()
            self.assertEqual(len(Account.account_list),2)

# setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Account.account_list = []

# other test cases here
    def test_save_multiple_account(self):
            '''
            test_save_multiple_account to check if we can save multiple account
            objects to our account_list
            '''
            self.new_account.save_account()
            test_account = Account("facebook","tete","0788267443te") # new account
            test_account.save_account()
            self.assertEqual(len(Account.account_list),2)

# More tests above
    def test_delete_account(self):
            '''
            test_delete_account to test if we can remove a account from our account list
            '''
            self.new_account.save_account()
            test_account = Account("facebook","doudou","0788267443ro") # new account
            test_account.save_account()

            self.new_account.delete_account()# Deleting a account object
            self.assertEqual(len(Account.account_list),1)
 # More tests above
    def test_delete_account(self):
            '''
            test_delete_account to test if we can remove a account from our account list
            '''
            self.new_account.save_account()
            test_account = Account("facebook","doudou","0788267443ro") # new account
            test_account.save_account()

            self.new_account.delete_account()# Deleting a account object
            self.assertEqual(len(Account.account_list),1)
    def delete_account(self):

        '''
        delete_account method deletes a saved account from the account_list
        '''

        Account.account_list.remove(self)


    def test_find_account_by_user(self):
        '''
        test to check if we can find a account by user name and display information
        '''

        self.new_account.save_account()
        test_account = Account("facebook","doudou","0788267443ro") # new account
        test_accountt.save_account()

        found_account = Account.find_by_user("doudou")

        self.assertEqual(found_account.password,test_account.password)




        

    # def test_account_exists(self):
    #     '''
    #     test to check if we can return a Boolean  if we cannot find the account.
    #     '''

    #     self.new_account.save_account()
    #     test_account = Account("facebook","doudodu","0788267443ro") # new account
    #     test_account.save_account()

    #     account_exists = Account.account_exist("doudou")

    #     self.assertTrue(account_exists)   

    
if __name__ == '__main__':
    unittest.main()