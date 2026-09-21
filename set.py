
# unordered 

my_set={10,30,20}
print(my_set)

a={10,20,30,40}
b={30,40,50,60}
print(a.union(b))
print(a.issuperset(b))
print(a.intersection(b))
print(a.symmetric_difference(b))
a.add(50)
a.update({1,2})
a.discard(100)
print(a)
