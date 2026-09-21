
prices= ['$12.50', '$9.99','$100.00']
print(list(map(lambda p : float(p.replace('$','')),prices)))

p= '$12.50'
print(p.replace('$',''))