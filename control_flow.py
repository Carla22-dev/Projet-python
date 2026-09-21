
email=""
phone=""
username=""


#allows registration 
#if any field is filled 

# print(any([email,phone, username]))


# #allows registration 
# #only of all fields is filled 

# print(all([email,phone,username]))


# print(3>1 and 5 < 1)
# print(3>1 and 5 < 1)

# print(3>1 and 5 < 1)
# print(3>1 and 5 < 1)

# cpu_usage=70
# memory_usage=95

# print(cpu_usage>90 or memory_usage>90)


# email=True
# password=False

# print(email and password)


#allow the user access only if the user is logged in 
#or they are a guest 
# but they must not be banned 

is_logged_in=True
is_guest=False
is_banned=True

print((is_logged_in or is_guest) and not is_banned)