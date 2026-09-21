

# user={"id":1,"age":30,"city":"Berlim"}

# #access 
# #print(use8r"name"])

# #checks 
# print("age" in user)
# print("name" not in user )

# #view Objets 

# print(user.keys())
# print(user.values())
# print(user.items())

# for u in user:
#     print(u, user[u])


# for key, value in user.items():
#     print(key,value)

# #add, Remove, Update

# user["name"]="John"
# user["age"]=35
# user.update({"age" : 40, "city":"Paris"})

# print(user)

# #Remove 

# age=user.pop("age")
# print(user)
# print("Removed Item: ",age )

# user.popitem()
# print(user)

#creation 

user={"id":None,
      "name":None,
      "age":None,
      "city":None
}

user=dict.fromkeys(["id","name","age","city"],None)
print(user)

