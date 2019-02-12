import unittest 
from Account import account

class TestAccount(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
   # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = account("facebook","Mazimpak","0786950337","rose@gmail.com") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.account_name,"facebook")
        self.assertEqual(self.new_account.last_name,"Mazimpak")
        self.assertEqual(self.new_account.phone_number,"0786950337")
        self.assertEqual(self.new_account.email,"rose@gmail.com")



   
    def test_save_account(self):
        '''
        test_save_contact test case to test if the contact object is saved into
            the contact list
        '''
        self.new_account.save_account() # saving the new contact
        self.assertEqual(len(account.account_list),1)

# Items up here...

    def test_save_multiple_account(self):
            '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
            self.new_account.save_account()
            test_account = account("facebook","rose","0788267443","roro@user.com") # new contact
            test_account.save_account()
            self.assertEqual(len(account.account_list),2)

# setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            account.account_list = []

# other test cases here
    def test_save_multiple_account(self):
            '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
            self.new_account.save_account()
            test_account = account("facebook","rose","0788267443","roro@user.com") # new contact
            test_account.save__account()
            self.assertEqual(len(_account._account_list),2)

# More tests above
    def test_delete__account(self):
            '''
            test_delete_contact to test if we can remove a contact from our contact list
            '''
            self.new__account.save__account()
            test__account = _account("facebook","rose","0788267443","roro@user.com") # new contact
            test__account.save__account()

            self.new__account.delete__account()# Deleting a contact object
            self.assertEqual(len(_account._account_list),1)
    def test_find__account_by_number(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''

        self.new__account.save__account()
        test__account = contact("facebook","rose","0788267443","roro@user.com") # new contact
        test__account.save__account()

        found__account= _account.find_by_number("0788267443")

        self.assertEqual(found__account.email,test__account.email) 
    def test_contact_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''

        self.new__account.save__account()
        test__account= _account("facebook","rose","0788267443","roro@user.com") # new contact
        test__account.save__account()

        _account_exists = _account._account_exist("0788267443")

        self.assertTrue(_account_exists)
    def test_display_all__account(self):
        '''
        method that returns a list of all contacts saved
        '''

        self.assertEqual(_account.display__account(),_account._account_list)

   
if __name__ == '__main__':
    unittest.main()
    