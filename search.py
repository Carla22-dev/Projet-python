#search  (starswith)

phone="+49-176-12345"
print(phone.startswith("+49"))


email="baraa@gmail.com"
print(email.endswith("gmail.com"))

file="data_backup.csv"
print(file.endswith(".csv"))

print("@" in email)

url= "https://api.company.com/v1/data"
print("/api" in url)