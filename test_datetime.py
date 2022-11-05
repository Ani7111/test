import datetime
from datetime import *

r = date.today()
print(r)
'''
6 Class - 1.date 2.time 3.datetime 4.tzinfo 5.timezone 6.timedelta 
'''

# dt = datetime.now()
# print('current datetime :',dt) #YYYY-MM-DD HH:MM:SS


# d = datetime.today()
# print('Today`s date     :',d)
# print('Today`s year     :',d.year)
# print('Today`s month    :',d.month)
# print('Today`s day      :',d.day)
# print('Today`s hour     :',d.hour)

# dob = datetime.datetime(1995,10,13,6,30,00)
# print(dob)

# from datetime import *

# now = datetime.now()
# print(now.strftime('Sumit:%D Time:%H:%M:%S' ))
# s = (dob.strftime('Sumit DOB :%d-%B-%Y Time:%H:%M:%S' ))
# print(type(s))
# print(s)
#
# from datetime import *
# strng = '11 sep 1995 8:52:11'
# s = datetime.strptime(strng,'%d %b %Y %H:%M:%S')
# print(type(s))
# print(s)




# from datetime import datetime
# import pytz
# ind = datetime.now()
# ind_tz = ind.strftime('%m-%d-%Y %H:%M:%S')
# print('Indian Time:',ind_tz)
#
#
# print('===========')
# place1 = pytz.timezone('America/New_york')
# ny_tz = datetime.now(place1)
# ny = ny_tz.strftime('%m-%d-%Y %H:%M:%S')
# print('New York Time:',ny)
#
#
# place2 = pytz.timezone('Europe/London')
# uk_tz = datetime.now(place2)
# uk = uk_tz.strftime('%d-%m-%Y %H:%M:%S')
# print('London timezone:',uk)


# from datetime import date
# from datetime import timedelta
#
# # Get today's date
# today = date.today()
# print("Today is: ", today)
#
# # Yesterday date
# yesterday = today - timedelta(days=1)
# print("Yesterday was: ", yesterday)

# import pytz
# place = datetime.now()
# print('Indian datetime  :',place)
#
# place = pytz.timezone('America/New_york')
# ny_tz = datetime.now(place)
# print('American Datetime:',ny_tz.strftime('%d-%b-%Y %I:%M:%S %p'))
#
# place = pytz.timezone('Japan')
# ny_tz = datetime.now(place)
# print('Japan Datetime   :',ny_tz.strftime('%d-%b-%Y %I:%M:%S %p'))

# start_date = "2021-08-18"
# end_date = "2021-08-28"
# start = datetime.strptime(start_date, "%Y-%m-%d")
# print((start))
# print('====')
# end = datetime.strptime(end_date, "%Y-%m-%d")
# print(end)
# print('====')
# a = (end-start)
# print(a)
# print('====')
# date_array = (start + timedelta(days=x) for x in range((end - start).days))
# # print(list(date_array))
# for date in date_array:
#     print(date)



