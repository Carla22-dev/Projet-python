import math
from datetime import datetime, timedelta, datetime

def converter_string_time(str_date):
    new_date=datetime.fromisoformat(str_date)
    return new_date

    
def delivery_date(start, description):
    date=converter_string_time(start)# convert the string time in real time
    print(date.day)
    day_of_week=date.weekday()
    print(day_of_week)
    match description:
        case "NOW":
            add_hours=date+timedelta(hours=2)
            return date.isoformat() # return to format
        case "ASAP":
           if  date.hour< 13:
                date.replace(hour=17)
                return date.isoformat()
                
           if date.hour>= 13: 
                date.replace(day=date.day+1)
                date.replace(hour=13)
                return date.isoformat()
        case "EOW":
            if day_of_week!=0 or day_of_week<5:
                if day_of_week in [0,1,2]:
                   day_to_friday=4-day_of_week
                   date=date + timedelta(days=day_to_friday)
                   date=date.replace(hour=17, minute=0, second=0)
                   return date.isoformat()
                #if day_of_week==0 or day_of_week==1 or day_of_week==2:
                    
                #if day






print( delivery_date("2025-02-03T16:00:00", "EOW"), "2025-02-07T17:00:00"
        )
#print(delivery_date("2008-12-21T13:00:00", "ASAP"), "2008-12-22T13:00:00")
#print( delivery_date("1999-06-03T09:45:00", "ASAP"), "1999-06-03T17:00:00")    
#print(delivery_date("2012-02-13T09:00:00", "NOW"), "2012-02-13T11:00:00")