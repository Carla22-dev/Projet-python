
#allow up to 3 attemps 
#if the user types "yes", print "Glad we are the same page"
#otherwise, print "3 Strikes, You are Out"

attempts=0
while attempts<3:
    answer=input("Do you agree? (yes/no):")
    if answer=='yes':
        print("Glad we are on the same page")
        break
    attempts+=1
else:
    print("3 Strikes, You are Out!")
        


       
