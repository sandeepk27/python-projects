# Python program to check if year is a leap year or not

n = int(input())

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (n % 400 == 0) and (n % 100 == 0):
    print("{0} is a leap year".format(n))

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (n % 4 == 0) and (n % 100 != 0):
    print("{0} is a leap year".format(n))

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(n))
