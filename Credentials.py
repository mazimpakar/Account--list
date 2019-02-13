class Credentials:
    """
    Class that generates new instances of credential.
    """

    credentials_list = [] # Empty contact list

    def __init__(self,credentials_name,user_name,number,email):

      # docstring removed for simplicity

        self.credential_name = credential_name
        self.user_name = user_name
        self.phone_number = number
        self.email = email
     # Empty contact list
 # Init method up here
    def save__credentials(self):

        '''
        save_credentials method saves credentials objects into credentials_list
        '''

        Credentials.credentials_list.append(self)
    def delete__credentials(self):

        '''
        delete_credentials method deletes a saved credentials from the credentials_list
        '''

        Credentials.credentials_list.remove(self)    

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials_ list
        '''
        return cls.credentials_list
    
    @classmethod
    def credentials_exist(cls,number):
        '''
        Method that checks if a credentials exists from the credentials list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the credentials exists
        '''
        for credentials in cls.credentials_list:
            if credentials.phone_number == number:
                    return True

        return False
    
    
    def create_credentials(aname,uname,phone,email):
        '''
        Function to create a new credentials
        '''
        new_credentials = Credentials(aname,uname,phone,email)
        return new_credentials 
    def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()