

#challenge: keep only string value and convert them to uppercase

user={"id":1,"name":"john","age":30,"city":"Brlim"}
user_str={
    #expression 
    k:v.upper()
    for k, v in user.items()#loop
    if isinstance(v,str) #filter

}
print(user_str)
