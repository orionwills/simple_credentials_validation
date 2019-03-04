# Python script to gather user credentials and evaluate the following:
# - is username 20 characters or less?
# - is password 5 or more characters?
# - are username and password the same?
# - are there any white spaces surrounding the username or password?
# - some simple timed things just for the fun of it


# import modules
import time, getpass, sys

# Gather username and password from user
def get_username_password():
    username = input('Enter Username: ')
    password = getpass.getpass(prompt='Enter Password: ')
    return username, password

#fucntion to gather credentials
def cred_validation():
    
    user_and_pass = get_username_password()
    username = user_and_pass[0]
    password = user_and_pass[1]

    
    if username == password:
        print('Username and Password cannot be the same; please try again')
        get_username_password()
    else:
        print('Checking credentials for validity...')
        time.sleep(1)
        print('Still checking')
        time.sleep(1)
    if username == username.strip():
        whitespace_username = False
    else:
            whitespace_username = True
    if password == password.strip:
        whispace_password = False
    else:
            whitespace_password = True
    if len(username) <= 20:
        time.sleep(.5)
        print('Username passes')
    else:
        time.sleep(.5)
        print('Username fails')
    if len(password) >= 5:
        time.sleep(.5)
        print('Password passes')
    else:
        time.sleep(.5)
        print('Password fails')
        time.sleep(1)
        print('Credentials check complete')
    show_check = input('Type 7 if you would like to see your credentials: ')
    if show_check == "7":
        time.sleep(.5)
        print('Fetching username...')
        time.sleep(.5)
        print('Fetching password')
        time.sleep(.5)
        print('Hooray!  They\'ve been located!')
        print('Your username is: ', username)
        print('Your password is: ', password)
        print('Thank you, ending routine.  Have a nice day.')
    else:
        print('Thank you, ending routine.  Have a nice day.')

cred_validation()