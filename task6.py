login = 'hello'
password = 123
i = 1
while i <= 3:
    user_login = input('Enter your login:')
    user_password = int(input('Enter numbers of your password:'))
    if login == user_login and password == user_password:
        print('Authorization is successful, attempt «{}» '.format(i))
        break
    i += 1
else:
    print('Sorry you had too many attempts to login. Try again later')
