#print('Hi dad today is tuesday and tommorow will be wednsday')
#from datetime import date

#today = date.today()
#print("Today's date:", today)

#today = datetime.datetime(2020, 6, 30)
#today.get_weekday()


import datetime 
import calendar 

def findDay(date): 
	born = datetime.datetime.strptime(date, '%d %m %Y').weekday() 
	return (calendar.day_name[born]) 

# Driver program 
date = '06 30 2020'
print(findDay(date)) 