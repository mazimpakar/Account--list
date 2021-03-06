
# import pyperclip
from user import Account
from Credentials import Credentials

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
    print(' ')
    print('Hello! Welcome to Password Locker.')
    while True:
        print(' ')
        print("-"*100)
        print("Use these short codes : ca - create a new account, da - display accounts, fa -find a account, ex -exit the account list ")
        short_code = input('Enter a choice: ').lower().strip()
        if short_code == 'ex':
            break

        elif short_code == 'ca':
            print("-"*100)
            print(' ')
            print('To create a new account:')
            account_name = input('Enter your account name - ').strip()
            user_name = input('Enter your user name - ').strip()
            phone_number= input('Enter your phone number - ').strip()
            email= input('Enter your email - ').strip()
            Account(account_name, user_name, phone_number,email)
            print(" ")
            print(
                f'New Account Created for: {account_name} {user_name} using phone-number: {phone_number}')
        elif short_code == 'da':
            print("-"*100)
            print(' ')
            print('To create, enter your account details:')
            user_name = input('Enter your account name - ').strip()
            phone_number = str(input('Enter your phone_number- '))
            user_exists = verify_user(user_name, phone_number)
            if user_exists == user_name:
                print(" ")
                print(
                    f'Welcome {user_name}. Please choose an option to continue.')
                print(' ')
                while True:

                    print("-"*100)
                    print("Use these short codes : cc - create a new Credentials, dc - display Credentials, fc -find a Credentials, ex -exit the Credentials list")
                        
                    short_code = input('Enter a choice: ').lower().strip()
                    print("-"*100)
                    if short_code == 'ex':
                        print(" ")
                        print(f'Goodbye {user_name}')
                        break
                    elif short_code == 'cc':
                        print(' ')
                        print('Enter your Credentials details:')
                        site_name = input('Enter the site\'s name- ').strip()
                        account_name = input(
                            'Enter your account\'s name - ').strip()
                        while True:
                            print(' ')
                            print("-"*100)
                            print(
                                'Please choose an option for entering a phone_number: \n ep-enter existing phone_number \n gp-generate a phone_number \n ex-exit')
                            phon_number_choice = input(
                                'Enter an option: ').lower().strip()
                            print("-"*100)
                            if phn_choice == 'ep':
                                print(" ")
                                phone_number= input(
                                    'Enter your phone_number: ').strip()
                                break
                            elif phn_choice == 'gp':
                                phone_number = generate_phone_number()
                                break
                            elif psw_choice == 'ex':
                                break
                            else:
                                print('Oops! Wrong option entered. Try again.')
                        save_credential(create_credential(
                            user_name, site_name, account_name, phone_number))
                        print(' ')
                        print(
                            f'Credential Created: Site Name: {site_name} - Account Name: {account_name} - Phone_number: {phone_number}')
                        print(' ')
                    elif short_code == 'dc':
                        print(' ')
                        if display_credentials(user_name):

                            print('Here is a list of all your credentials')
                            print(' ')
                            for credential in display_credentials(user_name):
                                print(
                                    f'Site Name: {credential.site_name} - Account Name: {credential.account_name} - Phone_number: {credential.phone_number}')
                            print(' ')
                        else:
                            print(' ')
                            print("You don't seem to have any credentials saved yet")
                            print(' ')
                    elif short_code == 'copy':
                        print(' ')
                        chosen_site = input(
                            'Enter the site name for the credential phone_number to copy: ')
                        copy_credential(chosen_site)
                        print('')
                    else:
                        print('Try again.')

            else:
                print(' ')
                print('Oops!Try again or Create an Account.')

        else:
            print("-"*100)
            print(' ')
            print('Oops!Try again.')


if __name__ == '__main__':
    main()














