
person=['Maria',29,'Data Engineer','Spain']

# name=person[0]
# age= person[1]
# role= person[2]
# country= person[3]

name,age,role,country=person
print(name)

# * details
name, *details,country=person

print(name)
print(details)
print(country)