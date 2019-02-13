# import pyperclip
class Account:
    """
    Class that generates new instances of account.
    """

    account_list = [] # Empty account list

    def __init__(self,account_name,user_name,number,email):

      # docstring removed for simplicity

        self.account_name = account_name
        self.user_name = user_name
        self.phone_number = number
        self.email = email
     # Empty contact list
 # Init method up here
    def save__account(self):

        '''
        save_account method saves account objects into account_list
        '''

        Account.account_list.append(self)
    def delete__account(self):

        '''
        delete_contact method deletes a saved account from the account_list
        '''

        Account.account_list.remove(self)    

    @classmethod
    def display_accounts(cls):
        '''
        method that returns the accountlist
        '''
        return cls.account_lis
    @classmethod
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns account that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            account  of person that matches the number.
        '''

        for account in cls.account_list:
            if account.phone_number == number:
                return account
    @classmethod
    def account_exist(cls,number):
        '''
        Method that checks if a account  exists from the account  list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the account  exists
        '''
        for account in cls.account_list:
            if account.phone_number == number:
                    return True

        return False
    @classmethod
    def display_accounts(cls):
        '''
        method that returns the account  list
        '''
        return cls.account_list
    # @classmethod
    # def copy_email(cls,number):
    #     account_found = cls.find_by_number(number)
    #     print(account_found)
    #     pyperclip.copy(account_found.email) 
    def create_account(aname,uname,phone,email):
        '''
        Function to create a new account 
        '''
        new_account = Account(aname,uname,phone,email)
        return new_account 
    def save_accounts(account):
    '''
    Function to save account 
    '''
    account.save_account()