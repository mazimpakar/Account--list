class Account:
    """
    Class that generates new instances of Account
    """

    pass

    def __init__(self,account_name,user_name,password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            account_name: New account account name.
            user_name : New account  user name.
            passwordr: New account password.
        

        '''
        self.account_name = account_name
        self.user_name = user_name
        self.password= password
        
