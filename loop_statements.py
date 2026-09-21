
#break, continue, pass
names=['john', 'maria', '','Kumar']

#CONTINUE 
# for name in names:
#     if name=='':
#         print('Empty value detected')
#         continue
#     print(f"Name= {name}")


# with break stop the loop 
# for name in names:
#     if name=='':
#         print('Empty value detected')
#         break
#     print(f"Name= {name}")

# PASS STATEMENT 

# for name in names:
#     if name=='':
#         print('Empty value detected')
#         pass
#     print(f"Name= {name}")

# days =['Mon','Sun','Wed','Tue']

# for day in days:
#     if day in ['Sat','Sun']:
#         continue
#     print(f"Worday: {day}")

#Another way 
# days =['Mon','Sun','Wed','Tue']
# weekends=['Sat','Sun']
# for day in days:
#     if day in weekends:
#         continue
#     print(f"Worday: {day}")

emails=['data@gmail','baraa@outlook.de','DROP TABLE USERS;','maria@gmail.com']

for email in emails:
    if ';' in email:
        print('SQL Injection :m Hacker Attack')
        break
    print (f'Processing email : {email}')

