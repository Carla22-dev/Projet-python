

data= "968-Maria,  (D@t@ Engineer  );;  27y"
data_update=data.replace("968-","")

# Extract the name 
parts_data=data_update.split(",")
data_name=parts_data[0].lower()

role_data=parts_data[1]
role_data=role_data.replace("(","")
role_data=role_data.replace(")","")
role_data=role_data.replace(";;",",")

# extract the role 
parts2_data=role_data.split(",")
role=parts2_data[0].strip().replace("@","a").lower()

#extract the age 

age_data=parts2_data[1].replace("y","")

print(f"name: {data_name} | role: {role} | age: {age_data}")




