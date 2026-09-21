
items =[1,25,3,43,7]

for i in items:
    if i% 2 ==0:
        print("Even Nr.Found", i)
        break
else:
    print("All numbers are odd")

## check missing values 


names=['Kamara','Tuba',None, 'Mounika']


for name in names :
    if name is None:
        print('Found a missing name')
        break
else:
    print("All names are available")


files=['data1.csv','report.pdf','report2.csv']

for file in files :
    if not file.endswith('.csv'):
        print(f'{file} is not a csv')
        break
else :
    print('All files are csv')