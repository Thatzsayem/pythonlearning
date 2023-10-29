year = int(input("What is the year "))
print("Here is the number of year  " + str(year))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This is Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("This is Leap year. ")
else:
  print("This is not leap year.")
