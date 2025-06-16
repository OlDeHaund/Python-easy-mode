## modul
import random
UsernamesList = ['Test1','Test2', 'Test3']
PasswordsList = ['1234', '123456', '12345678']
charsList = ['.',',',':',';','!','_','*','-','+','(',')','/','#','¤','%','&','@','$']
print(charsList)
def RandomPass():
    """Function creates Strong Password
   
    rtype:str
    """
    str0=".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0+str1+str2+str3
    ls = list(str4)
    random.shuffle(ls)
    # Извлекаем из списка 12 произвольных значений
    psword = ''.join([random.choice(ls) for x in range(12)])
    # Пароль готов
    return psword

def CheckPass(psword:str):
    """Function checks the complexity of the password
    
    :param str paword: Password
    :rtype bool
    """
    for x in range(len(psword)):
        if psword[x].isdigit() == True:
            for x in range(len(psword)):
                if psword[x].isupper() == True:
                    for x in range(len(psword)):
                        if psword[x].islower() == True:
                            for y in range(len(psword)):
                                if psword[y] in charsList:
                                    return True
    return False
def check_user_in_list(User:str):
    """Function checks if the user in list

    :param str: Username
    :trype bool
    """
    if User in UsernamesList:
        return True
    else:
        return False
def Log_in(Username:str, Password:str):
    """Function checks if user in list and if password is correct
    If everнthing is correct return the bool data for authorization in the system
    :param str Username: Username
    :param str Password: Password for user
    :rtype: bool
    """
    unicCheck = check_user_in_list(Username)
    if unicCheck == True:
        indexUsername = UsernamesList.index(Username)
        Passfromlist = PasswordsList[indexUsername]
        if Password == Passfromlist:
            return True
    return False
def Sign_in(Username:str, Password:str):
    """ Function checks if user in list and if password is correct
    If everнthing is correct the function 
    will add Username and Passwort to the list
    :param str Username
    :param str Password
    :rtype: str
    """
    unicCheck = check_user_in_list(Username)
    if unicCheck == False:
        passw = CheckPass(Password)
        if passw == True:
            UsernamesList.append(Username), PasswordsList.append(Password)
            answer = 'User has been created'
        else:
            answer = 'Error'
    else:
        answer = 'Erorr'
    return answer
def Change_Username(Username:str, NewUsername:str):
    """Function checks if user in the list
    If fuction will find Username in the list
    It'll change Old username to New username
    :param str Username
    :param str Password
    :rtype: str
    """
    unicCheck = check_user_in_list(Username)
    if unicCheck == True:
        indexUsername = UsernamesList.index(Username)
        UsernamesList.pop(indexUsername)
        UsernamesList.insert(indexUsername, NewUsername)
        answer = 'Username has been changed'
    else:
        answer = "User doesn't exist"
    return answer
#Username, OldPass, NewPass = input('Username: '), input('Old Password: '), input('New Password')
def Change_Password(Username:str, OldPass:str, NewPass:str):
    """Funtion checks if user in the list

    If function will find Username in the list
    It'll change OldPassword to NewPassword
    :param str Username
    :param str OldPass
    :param str NewPass
    """
    unicCheck = check_user_in_list(Username)
    if unicCheck == True:
        indexUsername = UsernamesList.index(Username)
        if OldPass == PasswordsList[indexUsername]:
            PasswordsList.pop(indexUsername)
            PasswordsList.insert(indexUsername, NewPass)
            answer = 'Password has been changed', PasswordsList
        else:
            answer = 'Wrong Password'
    else:
        answer = "User doesn't exist"
    return answer
# answer = Change_Password(Username, OldPass, NewPass)
# print(answer)

# Username = input('Username: ')
def Password_Reset(Username:str):
    """Function reset password
    Funtion will request username. If function will find username in the list
    It'll delete old password and create new password
    :param str Username
    :trype: str
    """
    unicCheck = check_user_in_list(Username)
    if unicCheck == True:
        indexUsername = UsernamesList.index(Username)
        PasswordsList.pop(indexUsername)
        NewPass = RandomPass()
        PasswordsList.insert(indexUsername, NewPass)
        answer = "Password has been reset, New Password: ", NewPass
    else:
        answer = "User doesn't exist"
    return answer
# answer = Password_Reset(Username)
# print(answer)