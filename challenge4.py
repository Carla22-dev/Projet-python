
user_email="carlafernandesgmail.com"
user_name="carla fernan"
age=18
password="carlaggfhjjnnhggg "

is_admin=False
is_moderator=True
is_banned=True
is_verify_email=False

# # question 1 - Check if a user's name is not empty and the age is greater than or equal to 18 
# print(user_name !="" and age >=18)

# # question 2 - check if  the password is at least 8 characters long and does not contain spaces
# print(len(password)>=8 and not password.count(" "))

#question 3 - check if a user's email is not empty, contains '@' and ends with 'com'
#print(((user_email is not None and user_email is not "" ) and '@'in user_email) and user_email.endswith(".com"))

#question 4- Check if a username is a string, is not None and is longer than 5 charaters 
# print(user_name.isalpha() is not None and len(user_name)>5)

#question 5 - check if the user is either an admin or a moderator 
# and either they're not banned or they've verified their email 

print((is_admin or is_moderator)and (is_banned or is_verify_email) )