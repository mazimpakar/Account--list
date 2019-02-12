class _account:
    """
    Class that generates new instances of contacts.
    """

    _account_list = [] # Empty contact list

    def __init__(self,account_name,user_name,number,email):

      # docstring removed for simplicity

        self.account_name = account_name
        self.user_name = user_name
        self.phone_number = number
        self.email = email
    _account_list = [] # Empty contact list
 # Init method up here
    def save__account(self):

        '''
        save_contact method saves contact objects into contact_list
        '''

        _account._account_list.append(self)
    def delete__account(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        account.account_list.remove(self)    

    @classmethod
    def display_accounts(cls):
        '''
        method that returns the contact list
        '''
        return cls.account_lis
    @classmethod
    def find_by_number(cls,number):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        for account in cls.account_list:
            if account.phone_number == number:
                return account
    @classmethod
    def account_exist(cls,number):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for account in cls.account_list:
            if account.phone_number == number:
                    return True

        return False
    @classmethod
    def display_accounts(cls):
        '''
        method that returns the contact list
        '''
        return cls.account_list