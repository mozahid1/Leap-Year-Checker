

year = int(input("Enter a Year: "))

if year % 400 == 0:
    y = "{} is not a Leap Year."
    print(y.format(year))
elif year % 100 == 0:
    y = "{} is not a Leap Year."
    print(y.format(year))
elif year % 4 == 0:
    y = "{} is a Leap Year."
    print(y.format(year))
else:
    y = "{} is not a Leap Year."
    print(y.format(year))        


    