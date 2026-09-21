
#task store application log messages in a file 


def write_log(message):
    with open(r"C:\Main\Python\app.log","a") as file:
        file.write(message + "\n")


write_log("App started")
