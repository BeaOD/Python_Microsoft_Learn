# pi = 3.14159
# print(pi)

# first_num = input('enter a number')
# second_num = input('enter a number')
# print(int(first_num) + float(second_num))

# days_in_february = 28
# print(str(days_in_february) + "" + "total days in february")


# num = 45
# num_1 = 8
# print(num_1 ** 45)

from datetime import datetime, timedelta

currentDate = datetime.now()
# print('Today is: ' + str(currentDate))

# oneDay = timedelta(days=1)
# yesterday = currentDate - oneDay
# print('yesterday was ' + str(yesterday)) 

# lastWeek = timedelta(weeks=1)
# last_week = currentDate - lastWeek
# print('last week was' + str(last_week))

# print ('Day: ' + str(currentDate.day))
# print ('Month: ' + str(currentDate.month))
# print ('Year: ' + str(currentDate.year))

# NOTE: convert a date inputed as string to date time object
# birthday = input('when is your birthday (dd/mm/yyyy)?')
# birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
# print ("My birthday: " + str(birthday_date))
# print ("My birthday is on:" + str(birthday_date))

x=42
y=54
if x !=y:
    print("success")