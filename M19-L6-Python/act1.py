#display current date and time


from datetime import date , time ,datetime
today = date.today()
now = datetime.now()
print("Today's date-", today)
print("Date components are", today.year,today.month, today.day)
print("Current Date and time-",now)

