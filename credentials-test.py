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

    def test_save_multiple_Credentials(self):
        '''
        test_save_multiple_Credentials to check if we can save multiple Credentials
        objects to our Credentials_list
        '''
        self.new_Credentials.save__Credentials()
        test_Credentials = Credentials("instagram","rose","0788267443","roro@user.com") # new Credentials
        test_Credentials.save__Credentials()
        self.assertEqual(len(Credentials.Credentials_list),2)

# setup and class creation up here
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.Credentials_list = []

# other test cases here
    def test_save_multiple_Credentials(self):
        '''
        test_save_multiple_Credentials to check if we can save multiple Credentials
        objects to our Credentials_list
        '''
        self.new_Credentials.save__Credentials()
        test_Credentials = Credentials("instagram","aline","0783691714","tete@user.com") # new Credentials
        test_Credentials.save__Credentials()
        self.assertEqual(len(Credentials.Credentials_list),2)

# More tests above
    def test_delete__Credentials(self):
        '''
        test_delete_Credentials to test if we can remove a Credentials from our Credentialslist
        '''
        self.new_Credentials.save__Credentials()
        test__Credentials = Credentials("instagram","rose","0788267443","roro@user.com") # new Credentials
        test__Credentials.save__Credentials()

        self.new_Credentials.delete__Credentials()# Deleting a Credentials object
        self.assertEqual(len(Credentials.Credentials_list),1)
    def test_find__Credentials_by_number(self):
        '''
        test to check if we can find a Credentials by phone number and display information
        '''

        self.new_Credentials.save__Credentials()
        test__Credentials = Credentials("instagram","mazimpak","0786950337","rose@gmail.com") # new Credentials
        test__Credentials.save__Credentials()

        found__Credentials= Credentials.find_by_number("0786950337")

        self.assertEqual(found__Credentials.email,test__Credentials.email) 

    def test_Credentials_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the Credentials.
        '''

        self.new_Credentials.save__Credentials()
        test_Credentials= Credentials("instagram","mazimpak","0786950337","rose@gmail.com") # new Credentials
        test__Credentials.save__Credentials()

        _account_exists = Account.account_exist("0788267443")

        self.assertTrue(_account_exists)
    def test_display_all__account(self):
        '''
        method that returns a list of all contacts saved
        '''

        self.assertEqual(Account.display_accounts(),Account.account_list)
   

    

   
if __name__ == '__main__':
    unittest.main()
    