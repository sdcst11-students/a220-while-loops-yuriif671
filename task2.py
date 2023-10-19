#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
Remember to use input().strip() to input str type variables
username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied

example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 12345
Access granted


"""

while True:
    username = str(input("Gimme ur name: "))
    password = str(input("Gimme ur password: "))

    if username == 'admin' and password == '12345':
        print("Ur in!")
        break

    print("Ur not in!")