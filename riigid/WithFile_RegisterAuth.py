## modul
import random
from email.message import EmailMessage
import smtplib, ssl
UsernamesList = []
PasswordsList = []
charsList = ['.',',',':',';','!','_','*','-','+','(',')','/','#','¤','%','&','@','$']
def read_users_pass():
    file=open(r'C:\Users\LP1\source\repos\Zhan-Gabriel-Gerke\project-test\Programmeerimise alused\Programmeerimise alused\def\Users.Pass.txt',"r",encoding="utf-8")
    for line in file:
        n = line.find(":")
        UsernamesList.append(line[0:n].strip())
        PasswordsList.append(line[n+1:len(line)].strip())
    file.close()
    return UsernamesList, PasswordsList
def write_to_single_file():
    with open(r'C:\Users\LP1\source\repos\Zhan-Gabriel-Gerke\project-test\Programmeerimise alused\Programmeerimise alused\def\Users.Pass.txt', "w", encoding="utf-8") as f:
        for x in range(len(UsernamesList)):
            TempVariable = f"{UsernamesList[x]}:{PasswordsList[x]}"
            f.write(TempVariable + "\n")
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
            write_to_single_file()
            answer = f'User has been created Username: {Username} Password: {Password}'
            email(answer)
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
        write_to_single_file()
        answer = f'Username has been changed New username: {UsernamesList[indexUsername]}'
        email(answer)
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
            write_to_single_file()
            answer = f'Password has been changed New Password: {PasswordsList[indexUsername]}'
            email(answer)
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
        write_to_single_file()
        answer = f"Password has been reset, Username: {Username} New Password: {NewPass}"
        email(answer)
    else:
        answer = "User doesn't exist"
    return answer
# answer = Password_Reset(Username)
# print(answer)
def write_to_file(fail:str, listt=[]):
    f=open(fail,'w',encoding="utf-8")
    for element in listt:
        f.write(element+"\n")
    f.close()
def email(letter):
    towho = input("Who do you want to send an email? ")
    smtp_server = 'smtp.gmail.com'
    port = 587
    sender_email = 'testmailfortthk@gmail.com'
    #####https://myaccount.google.com/apppasswords
    password = 'esmd plst aeln ydln'
    context = ssl.create_default_context()
    msg = EmailMessage()
    msg.set_content(letter)
    msg['Subject'] = 'e-mail sending'
    msg['From'] = sender_email
    msg['To'] = towho
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)
        server.login(sender_email, password)
        server.send_message(msg)
        server.quit()
        print('Sent')
    except Exception as e:
        print('Error:', e)