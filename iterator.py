 
letters=['a','b','c']
numbers=[1,2,3]
new_list=[]
for l in letters:
    new_list.append(l.upper())
    print(new_list)


# #enumerate 
# print(list(enumerate(letters)))
# #print(list(enumerate(letters, start=1)))
# for index,value in enumerate (letters):
#     print(index,value)


for l in reversed(letters):
    print(l)
#print(list(reversed(letters)))

for l,n in zip(letters,numbers):
    print(l,n)



#print(list(zip(letters,numbers)))