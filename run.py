def create_account(aname,uname,phone,email):
        '''
        Function to create a new contact
        '''
        new_account = Account(aname,uname,phone,email)
        return new_account 

def save_accounts(account):
    '''
    Function to save contact
    '''
    account.save_account()
def del_account(account):
    '''
    Function to delete a contact
    '''
    account.delete_account()   
def find_account(number):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return Account.find_by_number(number)

def check_existing_accounts(number):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return Account.account_exist(number)

    def display_accounts():
    '''
    Function that returns all the saved contacts
    '''
    return Account.display_accounts()
    #......credentials....

def create_Credentials(credentials_name,user_name,phone_number,email):
        '''
        Function to create a new Credentials
        '''
        new_Credentials= Credentials(credentials_name,user_name,phone-number,email)
        return new_Credentials

def save_Credentials(Credentials):
        '''
        Function to save Credentials
        '''
        Credentials.save_Credentials()

def del_Credentials(Credentials):
    '''
    Function to delete a Credentials
    '''
    Credentials.delete_Credentials()      

    

def find_Credentials(Credentials_name):
        '''
        Function that finds a Credentials by Credentials_name and returns the Credentials
        '''
        return Credentials.find_by_Credentials_name(Credentials_name)

def check_existing_Credentials(Credentials_name):
        '''
        Function that check if a Credentials exists with that Credentials_name and return a Boolean
        '''
        return Credentials.Credentials_exist(Credentials_name)

def display_Credentials():
        '''
        Function that returns all the saved Credentials
        '''
        return Credentials.display_Credentials()






def main():
    print("Hello Welcome to password Locker. What is your name?")
            user_name = input()

            print(f"Hello {user_name}. what would you like to do?")
            print('\n')

            while True:
                    print("Use these short codes : ca - create a new account, da - display accounts, fa -find a account, ex -exit the account list ")

                    short_code = input().lower()

                    if short_code == 'ca':
                            print("New Account")
                            print("-"*10)

                            print ("Acount name ....")
                            a_name = input()

                            print("User name ...")
                            u_name = input()

                            print("Phone number ...")
                            p_number = input()

                            print("Email address ...")
                            e_address = input()


                            save_accounts(create_account(a_name,u_name,p_number,e_address)) # create and save new account.
                            print ('\n')
                            print(f"New Account {a_name} {u_name} created")
                            print ('\n')

                    elif short_code == 'da':

                            if display_accounts():
                                    print("Here is a list of all your accounts")
                                    print('\n')

                                    for contact in display_accounts():
                                            print(f"{account.account_name} {account.user_name} .....{account.phone_number}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any accounts saved yet")
                                    print('\n')

                    elif short_code == 'fa':

                            print("Enter the number you want to search for")

                            search_number = input()
                            if check_existing_accounts(search_number):
                                    search_account= find_account(search_number)
                                    print(f"{search_account.account_name} {search_account.user_name}")
                                    print('-' * 20)

                                    print(f"Phone number.......{search_account.phone_number}")
                                    print(f"Email address.......{search_account.email}")
                            else:
                                    print("That account does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")


                    if __name__ == '__main__':

                             main()           
