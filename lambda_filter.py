
prices=[120,30,300,80]
#print(list(filter(lambda p: p>=100,prices)))
students =[['Maria',85],['Kumar',90],['Max',60]]




print(list(filter(lambda row: row[1]>70,students)))
print("this is curiosity : ",students[1])


print(list(filter(lambda row: row[0].startswith('M'),students)))

#print(students[0][0].startswith('M'))