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

# x=42
# y=0
# if x !=y:
#     print("success")
# try:
#     print(x/y)
# except ZeroDivisionError as e:
#     print("you can't divide by zero")
# else:
#     print("something else went wrong")
# finally:
#     print("the try except is finished")

#NOTE: CONDITIONAL STATEMENTS
# price = 4
# if price >= 2.00:
#     tax = 0.8
# else:
#     tax = 0.1
# print(tax)


# country = "CANADA"
# if country.lower() == "canada":
#     print("ooh a canadian")
# else:
#     print("sorry to bother you, you're not canadian")

#NOTE: CONDITIONAL LOGIC
# price = input("how much is the donught")
# price = float(price)
# if price >= 1.00:
#     tax = 0.7
    # print('tax rate is:' + str(tax))
#     print(tax)
# else:
#     print ('we dont know what you are saying but that is outrageous')

# country = input('where are you from')
# if country.lower() == 'canada':
#     print('that is cool')
# else:
#     print('still dont know where you from')

# country = input("your country is: ")
# tax = 0

# if  country.lower() == "canada":
#     province = input("what is your province?")
#     if province in ('alberta', 'nunavut','saskachtuan'):
#         tax = 0.05
#     elif province == "ontario":
#         tax = 0.13
# else:
#     tax = 0.15
# print (tax)

gpa = input("what's your gpa?")
gpa = float(gpa)
lowest_grade = input("your grade")
lowest_grade = float(gpa)
if gpa >= .85 and lowest_grade >= .70:
    honour_roll = True
else:
    honour_roll = False
    if honour_roll:
        print("we got it ")