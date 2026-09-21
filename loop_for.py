
# items=(1,2,3,4,5)#tuple 

# for i in items :
#     print(f"Round:{i}")

# print("Round: 1 ")
# print("Round: 2 ")
# print("Round: 3 ")
# print("Round: 4 ")
# print("Round: 5 ")

# items=[1,2,3,4,5]#list
# for i in items :
#     print(f"Round:{i}")


# items="Python"
# for item in items :
#     print(f"Round:{item}")


# for item in range (10):
#     print(f"Round: {item}")


scores =[80,50,60,75]

total=0
for score in scores :
    total +=score
    print("Current Total:", total)
print("Final scores is ", total)

files=['Report.csv','DATA.csv', 'fianl.TXT']
for file in files:
    file =file.strip().lower().replace('.txt','.csv')
    print(f"Processing {file}")
