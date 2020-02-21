from datetime import date
curr=date.today()
year=int(input("Enter a year: "))
month=int(input("Enter a month: "))
day=int(input("Enter a day: "))
given=date(year,month,day)
diff=given-curr
hours=diff*24
sec=hours*3600
if (month==1) or (month==3) or (month==5) or (month==7) or (month==8) or (month==10) or (month==12):
    print("31 days")
elif (month==4) or (month==6) or (month==9) or (month==11):
    print("30 days")
else:
    if (year % 4==0) and not(year % 100==0) and not(year % 400==0):
       print ("29 days")
    else:
       print ("28 days")
print (diff,hours,sec)       