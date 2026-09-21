
person=['Maria',29,'Data Engineer','Spain']


name,_,role,_=person

# combine * and _

name,*_,country=person

print(name)
print(country)
