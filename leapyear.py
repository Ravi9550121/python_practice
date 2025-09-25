num=int(input("enter a year"))

if (num%4==0 or num%100==0 or num%400==0):
    print(num," is a leap year")
else:
    print(num, "not a leap year")