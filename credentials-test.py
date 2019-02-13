import unittest 
from Credentials import Credentials
# import pyperclip


class TestCredentials(unittest.TestCase):

        '''
        Test class that defines test cases for the Credentials class behaviours.

        Args:
            unittest.TestCase: TestCase class that helps in creating test cases
        '''
   # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_Credentials = Credentials("instagram","Mazimpak","0786950337","rose@gmail.com") # create Credentials object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_Credentials.account_name,"instagram")
        self.assertEqual(self.new_Credentials.user_name,"Mazimpak")
        self.assertEqual(self.new_Credentials.phone_number,"0786950337")
        self.assertEqual(self.new_Credentials.email,"rose@gmail.com")



   
    def test_save_Credentials(self):
        '''
        test_save_Credentials test case to test if the Credentials object is saved into
                the Credentials list
        '''
        self.new_Credentials.save__Credentials() # saving the new Credentials
        self.assertEqual(len(Credentials.Credentials_list),1)

# Items up here...

    def test_save_multiple_account(self):
        '''
        test_save_multiple_contact to check if we can save multiple contact
        objects to our contact_list
        '''
        self.new_account.save__account()
        test_account = Account("twitter","rose","0788267443","roro@user.com") # new contact
        test_account.save__account()
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
        test_save_multiple_contact to check if we can save multiple contact
        objects to our contact_list
        '''
        self.new_account.save__account()
        test_account = Account("twitter","rose","0788267443","roro@user.com") # new contact
        test_account.save__account()
        self.assertEqual(len(Account.account_list),2)

# More tests above
    def test_delete__account(self):
        '''
        test_delete_contact to test if we can remove a contact from our contact list
        '''
        self.new_account.save__account()
        test__account = Account("twitter","rose","0788267443","roro@user.com") # new contact
        test__account.save__account()

        self.new_account.delete__account()# Deleting a contact object
        self.assertEqual(len(Account.account_list),1)
    def test_find__account_by_number(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''

        self.new_account.save__account()
        test__account = Account("twitter","rose","0788267443","roro@user.com") # new contact
        test__account.save__account()

        found__account= Account.find_by_number("0788267443")

        self.assertEqual(found__account.email,test__account.email) 
    def test_contact_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''

        self.new_account.save__account()
        test__account= Account("twitter","rose","0788267443","roro@user.com") # new contact
        test__account.save__account()

        _account_exists = Account.account_exist("0788267443")

        self.assertTrue(_account_exists)
    def test_display_all__account(self):
        '''
        method that returns a list of all contacts saved
        '''

        self.assertEqual(Account.display_accounts(),Account.account_list)
   

    

   
if __name__ == '__main__':
    unittest.main()
    