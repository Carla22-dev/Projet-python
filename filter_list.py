
letters=['a','','b',None,'c',False]
print(list(filter(None,letters)))

items=['sql','123','python','42']
print(list(filter(str.isalpha,items)))

