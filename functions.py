import math


def make_coffee():

    print("Wake up ")
    print("Start Machine")
    print("add Milk")
    print("Enjoy it")


#functions from libraries
number=4.2
print(math.ceil(number))


# cause_rule="lower"#global variable

# def clean_name(name): # parameter name
#     cleaned=name.strip().lower()# local variable
#     if  cause_rule=="lower":
#         cleaned=cleaned.lower()
#     #print("Raw:",name)
#     print(cleaned)

# clean_name("MarRIA")
# print(f"The Rule is :{cause_rule} ")


# #######################################
# def clean_name(first_name,last_name, country):
#     first=first_name.strip().lower()
#     last=last_name.strip().lower()
#     full_name=first+ " " + last
#     print(f"The full name is :{full_name} from {country}")


# #positional Arguments 2-3 parameters
# clean_name("Carla","Fernandes","Cabo Verde")

# #keyword Arguments >3parameters
# clean_name(country="Cabo Verde",first_name="Carla",last_name="Fernandes")

# #Mix Arguments
# clean_name()

def clean_name(first_name,last_name, country="n/a"):
    first=first_name.strip().lower()
    last=last_name.strip().lower()
    full_name=first+ " " + last
    print(f"The full name is :{full_name} from {country}")

clean_name("Carla", "Fernandes")


#calculate the total of values

def total(*args):
    print((args))

total(1,2)

def create_user(**kwargs):
    print(kwargs)


create_user(first_name="Mo",last_name="Salah", age=33, country="Egypt")