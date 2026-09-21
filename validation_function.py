#check if a password meets the minimum length of 8

def write_log(message):
     with open("dados.txt","a") as file:
    #with open(r"C:\Users\cf974\Desktop\PythonCodes","a") as file:
        file.write(message + "\n")


write_log("App started")

def clean_and_split_email(email):
    cl_email=email.strip().lower()
    #sara@gmail.com

    username,domain=cl_email.split("@")
    return {"username": username, "domain":domain}


#validate the password 

def is_valid_passwor(password):
   return  len(password)>=8

print(is_valid_passwor("12345"))


#check if email has a basic valid format 

def is_valid_email(email):
   return "@" in email and "." in email

print(is_valid_email("sara@gmail.com"))


#orcheter


#we reive an email from a user 
#we must check if is valid 
# if it is not valid, we log the problem 
# if it is valid, we clean it and store structured information 
#and we log what happened

def process_user_email(email):
    write_log("App Started")
   
    is_valid_email(email)
    if not is_valid_email(email):
        write_log(f"Invalid Email received: {email}")
    else:
        clean_email=clean_and_split_email(email)
        write_log(f"Processed Email: {clean_email}")
    write_log("App Stopped")


email=input("Please enter your email: ")
process_user_email(email)