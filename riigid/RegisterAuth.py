from ModulRegistreerimineJaAutoriseerimine import *
aaa = None
while aaa is None:
    a = input('Sign in - 1, Log in - 2, Change Password or Username - 3, Forgot password - 4: If you want quit - q')
    if a == '1':
        Username, Password = input('Username'), input('Password')
        answer = Sign_in(Username, Password)
    elif a == '2':
        Username, Password = input('Username'), input('Password')
        answer = Log_in(Username, Password)
    elif a == '3':
        b = input('Change username == 1, Change Password == 2')
        if b == '1':
            Username, NewUsername = input('Username'), input('New Username')
            answer = Change_Username(Username, NewUsername)
        elif b == '2':
            Username, OldPass, NewPass = input('Username'), input('Old password'), input('New password')
            answer = Change_Password(Username, OldPass, NewPass)
        else:
            print('You wrote wrong number')
    elif a == '4':
        Username = input('Username')
        answer = Password_Reset(Username)
    elif a == 'q'.islower():
        aaa = 1
    else:
        print('You wrote wrong number or letter')
    print(answer) 