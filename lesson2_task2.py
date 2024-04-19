# I have a static login and password user When entering, if both are entered correctly, it says that He entered, 
# if he entered incorrectly, he tells him that it is Tinki Winki And if one of them is entered correctly,
# he tells him to try it.
# Extra! Password checker: Enter the password and check the password if Exceeds 8 characters.


# TASK1

email = 'eduTech@mail.com'
password = 'EduTech'

userEmail = input('your email: ')
userPassword = input('your password: ')

if userEmail == email and userPassword == password:
  print('You signed in')
elif userEmail == email and userPassword != password:
  print('try again')  
elif userEmail != email and userPassword == password:
  print('try again')
else:
  print('tinki vinki')  


# TASK2

# check if password is at least 8 characters.

password = input('your password: ')

if len(password) >= 8:
  print('correct')
else:
  print('at least 8 chars')