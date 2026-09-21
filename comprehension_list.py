
domains=['www.google.com','openai.com','localhost','WWW.DATAWITHBARAA.COM']

cleaned = [
    d.lower().replace('www.','') # o que quero fazer 
    for d in domains # for para cada elemento na lista 
    if '.' in d # para cada elemento dentro do domain que tem '.'
]
print(cleaned)