


# for x in range (3):
#     for y in range (2):
#         print(f'({x},{y})')



# colors=['red','blue','green']
# sizes=['L','M','S']

# for color in colors:
#     for size in sizes:
#         print(f'{color}-Size {size}') 


# years=[2026,2027]
# month=['Jan','Feb']
# days=range(1,29)


# for y in years:
#     for m in month:
#         for d in days :
#             print(f'report_{y}_{m}_{d}.csv')

#SELECT count (*) FROM customers where id IS NULL 

tables =['customers','orders','products','prices']
columns=['id','create_date']


for t in tables:
    for c in columns :
        print(f'SELECT count(*) FROM {t} WHERE {c} IS NULL;')