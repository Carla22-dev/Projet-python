#validate the quality and correctness of Email Values 
# - must not be empty 

verify_email="carlafernandes@gamil.com"
#Clean the string
verify_email=verify_email.strip()

if verify_email =="":
    print("Email can not be empty")
    # must contain '.' and @
elif not ('.' in verify_email and '@' in verify_email):
    print("Email must contain . and @")
#- must contain exactly one '@' symbol
elif verify_email.count('@')!=1:
    print("Email must contain 1 @")
# - must end with '.com' , '.org ', or '.net 
elif not verify_email.endswith(('.com','.org','.net')):
    print("Email must end with  .com .org .net")
# - must not be longer than 254 charaters 
elif len(verify_email) >254:
    print("Email must not be longer than 254 charaters")
# - Must start and end with a letter or digit 
elif not(verify_email[0].isalnum() and verify_email[-1].isalnum()):
    print("The email must start and end a letter or digit ")
else:
    print("Email is valid")
