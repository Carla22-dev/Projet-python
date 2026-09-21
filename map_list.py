
letters=['a','b','c']
print(list(map(str.upper,letters)))


numbers=['1','2','3']
print(list(map(int,numbers)))

names=[' Maria','John',' Kumar']
for n in map(str.strip, names):
    print(n)
#print(list(map(str.strip,names)))
