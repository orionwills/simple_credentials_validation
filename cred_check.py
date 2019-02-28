def cred_validation():
    import time
    import getpass
    import sys
    username = input('Enter Username: ')
    password = getpass.getpass(prompt='Enter Password: ')
    print('Checking credentials for validity...')
    time.sleep(1.5)
    print('Still checking')
    time.sleep(1.5)
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