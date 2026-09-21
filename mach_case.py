
country="United States"

if country == "United States":
    print("US")
elif country == "India":
    print("IN")
elif country == "Egypt":
    print("EG")
elif country == "Germany":
    print("DE")
else:
     print("Unknown Country")

match country:
    case "United States":
        print("US")
    case "India":
        print("IN")
    case "Egypt":
        print("EG")
    case "Germany":
        print("DE") 
    case _:
        print("Unkwn Country")