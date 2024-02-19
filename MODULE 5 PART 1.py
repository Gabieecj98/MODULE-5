Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:39) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#Step1
total_months = 24
total_rainfall = 24.45

num_years = int(input("Enter the number of years: "))
Enter the number of years: 2

for year in range(1, num_years + 1):
    for month in range (1, 13):
        rainfall = float(input(f"Enter rainfall for Year {year}, Month {month}: "))
        total_rainfall += rainfall
        total_months += 1

        
Enter rainfall for Year 1, Month 1: 0.78
Enter rainfall for Year 1, Month 2: 0.94
Enter rainfall for Year 1, Month 3: 1.17
Enter rainfall for Year 1, Month 4: 0.06
Enter rainfall for Year 1, Month 5: 2.59
Enter rainfall for Year 1, Month 6: 0.58
Enter rainfall for Year 1, Month 7: 0.99
Enter rainfall for Year 1, Month 8: 1.45
Enter rainfall for Year 1, Month 9: 1.25
Enter rainfall for Year 1, Month 10: 0.46
Enter rainfall for Year 1, Month 11: 0.47
Enter rainfall for Year 1, Month 12: 1.18
Enter rainfall for Year 2, Month 1: 0.22
Enter rainfall for Year 2, Month 2: 0.80
Enter rainfall for Year 2, Month 3: 3.80
Enter rainfall for Year 2, Month 4: 2.02
Enter rainfall for Year 2, Month 5: 3.65
Enter rainfall for Year 2, Month 6: 0.84
Enter rainfall for Year 2, Month 7: 0.34
Enter rainfall for Year 2, Month 8: 0.27
Enter rainfall for Year 2, Month 9: 0.28
Enter rainfall for Year 2, Month 10: 0.08
Enter rainfall for Year 2, Month 11: 0.07
Enter rainfall for Year 2, Month 12: 0.16

print(f"\nNumber of months: {total_months}")

Number of months: 48

num_years = int(input("Enter the number of years: "))
Enter the number of years: 2
Enter the number of years: 2
SyntaxError: invalid syntax

num_years = int(input("Enter the number of years: "))
Enter the number of years: 2

total_months = num_years * 12

for year in range(1, num_years + 1):
    for month in range(1, 13):
        rainfall = float(input(f"Enter rainfall for Year {year}, Month {month}: "))
        if 'total_rainfall' in locals():
            total_rainfall += rainfall
        else:
            total_rainfall = rainfall

            
Enter rainfall for Year 1, Month 1: 0.78
Enter rainfall for Year 1, Month 2: 0.94
Enter rainfall for Year 1, Month 3: 1.17
Enter rainfall for Year 1, Month 4: 0.06
Enter rainfall for Year 1, Month 5: 2.59
Enter rainfall for Year 1, Month 6: 0.58
Enter rainfall for Year 1, Month 7: 0.99
Enter rainfall for Year 1, Month 8: 1.45
Enter rainfall for Year 1, Month 9: 1.25
Enter rainfall for Year 1, Month 10: 0.46
Enter rainfall for Year 1, Month 11: 0.47
Enter rainfall for Year 1, Month 12: 1.18
Enter rainfall for Year 2, Month 1: 0.22
Enter rainfall for Year 2, Month 2: 0.80
Enter rainfall for Year 2, Month 3: 3.80
Enter rainfall for Year 2, Month 4: 2.02
Enter rainfall for Year 2, Month 5: 3.65
Enter rainfall for Year 2, Month 6: 0.84
Enter rainfall for Year 2, Month 7: 0.34
Enter rainfall for Year 2, Month 8: 0.27
Enter rainfall for Year 2, Month 9: 0.28
Enter rainfall for Year 2, Month 10: 0.08
Enter rainfall for Year 2, Month 11: 0.07
Enter rainfall for Year 2, Month 12: 0.16

average_rainfall = total_rainfall / total months
SyntaxError: invalid syntax
average_rainfall = total_rainfall / total_months
print(f"\nNumber of months: {total_months}")

Number of months: 24
print(f"Total inches of rainfall: {total_rainfall}")
Total inches of rainfall: 73.35

average_rainfall = total_rainfall / total_months
print(f"\nNumber of months: {total_months}")

Number of months: 24
print(f"Total inches of rainfall: {total_rainfall}")
Total inches of rainfall: 73.35
Total inches of rainfall: 73.35
SyntaxError: invalid syntax

num_years = int(input("Enter the number of years: "))
Enter the number of years: 2

for year in range(1, num_years + 1):
    for month in range(1, 13):
        total_rainfall += float(input(f"Enter rainfall for Year {year}, Month {month}: "))
        total_months += 1

        
Enter rainfall for Year 1, Month 1: 0.78
Enter rainfall for Year 1, Month 2: 0.94
Enter rainfall for Year 1, Month 3: 1.17
Enter rainfall for Year 1, Month 4: 0.06
Enter rainfall for Year 1, Month 5: 2.59
Enter rainfall for Year 1, Month 6: 0.58
Enter rainfall for Year 1, Month 7: 0.99
Enter rainfall for Year 1, Month 8: 1.45
Enter rainfall for Year 1, Month 9: 1.25
Enter rainfall for Year 1, Month 10: 0.46
Enter rainfall for Year 1, Month 11: 0.47
Enter rainfall for Year 1, Month 12: 1.18
Enter rainfall for Year 2, Month 1: 0.22
Enter rainfall for Year 2, Month 2: 0.80
Enter rainfall for Year 2, Month 3: 3.80
Enter rainfall for Year 2, Month 4: 2.02
Enter rainfall for Year 2, Month 5: 3.65
Enter rainfall for Year 2, Month 6: 0.84
Enter rainfall for Year 2, Month 7: 0.34
Enter rainfall for Year 2, Month 8: 0.27
Enter rainfall for Year 2, Month 9: 0.28
Enter rainfall for Year 2, Month 10: 0.08
Enter rainfall for Year 2, Month 11: 0.07
Enter rainfall for Year 2, Month 12: 0.16

average_rainfall = total_rainfall / total_months
print(f"\nNumber of months: {total_months}")

Number of months: 48

num_years = int(input("Enter the number of years: "))
Enter the number of years: 2

for year in range(1, num_years + 1):
    for month in range(1, 13):
        total_rainfall += float(input(f"Enter rainfall for Year {year}, Month{month}: "))
        total_month += 1

        
Enter rainfall for Year 1, Month1: 0.78
Traceback (most recent call last):
  File "<pyshell#58>", line 4, in <module>
    total_month += 1
NameError: name 'total_month' is not defined. Did you mean: 'total_months'?


#Part1
num_years = int(input("Enter the number of years: "))
Enter the number of years: 2

for year in range(1, num_years + 1):
    for month in range(1, 13):
        total_rainfall += float(input(f"Enter rainfall for Year {year}, Month {months}: "))
        total_months += 1

        
Traceback (most recent call last):
  File "<pyshell#68>", line 3, in <module>
    total_rainfall += float(input(f"Enter rainfall for Year {year}, Month {months}: "))
NameError: name 'months' is not defined. Did you mean: 'month'?
NameError: name 'months' is not defined. Did you mean: 'month'?
SyntaxError: invalid syntax


num_years = int(input("Enter the number of years: "))
Enter the number of years: 2

for year in range(1, num_years +1):
    for month in range(1, 13):
        total_rainfall += float(input(f"Enter rainfall for Year {year}, Month {month}: "))
        total_months += 1

        
Enter rainfall for Year 1, Month 1: 0.78
Enter rainfall for Year 1, Month 2: 0.94
Enter rainfall for Year 1, Month 3: 1.17
Enter rainfall for Year 1, Month 4: 0.06
Enter rainfall for Year 1, Month 5: 2.59
Enter rainfall for Year 1, Month 6: 0.58
Enter rainfall for Year 1, Month 7: 0.99
Enter rainfall for Year 1, Month 8: 1.45
Enter rainfall for Year 1, Month 9: 1.25
Enter rainfall for Year 1, Month 10: 0.46
Enter rainfall for Year 1, Month 11: 0.47
Enter rainfall for Year 1, Month 12: 1.18
Enter rainfall for Year 2, Month 1: 0.22
Enter rainfall for Year 2, Month 2: 0.80
Enter rainfall for Year 2, Month 3: 3.80
Enter rainfall for Year 2, Month 4: 2.02
Enter rainfall for Year 2, Month 5: 3.65
Enter rainfall for Year 2, Month 6: 0.84
Enter rainfall for Year 2, Month 7: 0.34
Enter rainfall for Year 2, Month 8: 0.27
Enter rainfall for Year 2, Month 9: 0.28
Enter rainfall for Year 2, Month 10: 0.08
Enter rainfall for Year 2, Month 11: 0.07
Enter rainfall for Year 2, Month 12: 0.16

average_rainfall = total_rainfall / total_months
print(f"\nNumber of months: {total_months}")

Number of months: 72
Number of months: 72
SyntaxError: invalid syntax

num_years = int(input("Enter the number of years: "))
Enter the number of years: 2

total_rainfall = 24.45
total_months = 24

for year in range(1, num_years + 1):
    for month in range(1, 13):
        total_rainfall += float(input(f"Enter rainfall for Year {year}, Month {month}: "))
        total_months += 1

        
Enter rainfall for Year 1, Month 1: 0.78
Enter rainfall for Year 1, Month 2: 0.94
Enter rainfall for Year 1, Month 3: 1.17
Enter rainfall for Year 1, Month 4: 0.06
Enter rainfall for Year 1, Month 5: 2.59
Enter rainfall for Year 1, Month 6: 0.58
Enter rainfall for Year 1, Month 7: 0.99
Enter rainfall for Year 1, Month 8: 1.45
Enter rainfall for Year 1, Month 9: 1.25
Enter rainfall for Year 1, Month 10: 0.46
Enter rainfall for Year 1, Month 11: 0.47
Enter rainfall for Year 1, Month 12: 1.18
Enter rainfall for Year 2, Month 1: 0.22
Enter rainfall for Year 2, Month 2: 0.80
Enter rainfall for Year 2, Month 3: 3.80
Enter rainfall for Year 2, Month 4: 2.02
Enter rainfall for Year 2, Month 5: 3.65
Enter rainfall for Year 2, Month 6: 0.84
Enter rainfall for Year 2, Month 7: 0.34
Enter rainfall for Year 2, Month 8: 0.27
Enter rainfall for Year 2, Month 9: 0.28
Enter rainfall for Year 2, Month 10: 0.08
Enter rainfall for Year 2, Month 11: 0.07
Enter rainfall for Year 2, Month 12: 0.16

average_rainfall = total_rainfall / total_months
print(f"\nNumber of months: {total_months}")

Number of months: 48
Number of months: 48
SyntaxError: invalid syntax

num_years = int(input("Enter the number of years: "))
Enter the number of years: 2

for year in range(1, num_years + 1):
    for month in range(1, 13):
       total_rainfall += float(input(f"Enter rainfall for Year {year}, Month {month}: "))

       
Enter rainfall for Year 1, Month 1: 0.78
Enter rainfall for Year 1, Month 2: 0.94
Enter rainfall for Year 1, Month 3: 1.17
Enter rainfall for Year 1, Month 4: 0.06
Enter rainfall for Year 1, Month 5: 2.59
Enter rainfall for Year 1, Month 6: 0.58
Enter rainfall for Year 1, Month 7: 0.99
Enter rainfall for Year 1, Month 8: 1.45
Enter rainfall for Year 1, Month 9: 1.25
Enter rainfall for Year 1, Month 10: 0.46
Enter rainfall for Year 1, Month 11: 0.47
Enter rainfall for Year 1, Month 12: 1.18
Enter rainfall for Year 2, Month 1: 0.22
Enter rainfall for Year 2, Month 2: 0.80
Enter rainfall for Year 2, Month 3: 3.80
Enter rainfall for Year 2, Month 4: 2.02
Enter rainfall for Year 2, Month 5: 3.65
Enter rainfall for Year 2, Month 6: 0.84
Enter rainfall for Year 2, Month 7: 0.34
Enter rainfall for Year 2, Month 8: 0.27
Enter rainfall for Year 2, Month 9: 0.28
Enter rainfall for Year 2, Month 10: 0.08
Enter rainfall for Year 2, Month 11: 0.07
Enter rainfall for Year 2, Month 12: 0.16

total_months = 12 * num_years
average_rainfall = total_rainfall / total_months
print(f"\nNumber of months: {total_months}")

Number of months: 24
print(f"Total inches of rainfall: {total_rainfall}")
Total inches of rainfall: 73.35
print(f"average rainfall per month: {average_rainfall:.2f}")
average rainfall per month: 3.06
average rainfall per month: 3.06
SyntaxError: invalid syntax


num_years = int(input("Enter the number of years: "))
Enter the number of years: 2

total_rainfall = 24.45

or year in range(1, num_years + 1):
    
SyntaxError: invalid syntax
for year in range(1, num_years + 1):
    for month in range(1, 13):
        total_rainfall += float(input(f"Enter rainfall for Year {year}, Month {month}: "))

        
Enter rainfall for Year 1, Month 1: 0.78
Enter rainfall for Year 1, Month 2: 0.94
Enter rainfall for Year 1, Month 3: 1.17
Enter rainfall for Year 1, Month 4: 0.06
Enter rainfall for Year 1, Month 5: 2.59
Enter rainfall for Year 1, Month 6: 0.58
Enter rainfall for Year 1, Month 7: 0.99
Enter rainfall for Year 1, Month 8: 1.45
Enter rainfall for Year 1, Month 9: 1.25
Enter rainfall for Year 1, Month 10: 0.46
Enter rainfall for Year 1, Month 11: 0.47
Enter rainfall for Year 1, Month 12: 1.18
Enter rainfall for Year 2, Month 1: 0.22
Enter rainfall for Year 2, Month 2: 0.80
Enter rainfall for Year 2, Month 3: 3.80
Enter rainfall for Year 2, Month 4: 2.02
Enter rainfall for Year 2, Month 5: 3.65
Enter rainfall for Year 2, Month 6: 0.84
Enter rainfall for Year 2, Month 7: 0.34
Enter rainfall for Year 2, Month 8: 0.27
Enter rainfall for Year 2, Month 9: 0.28
Enter rainfall for Year 2, Month 10: 0.08
Enter rainfall for Year 2, Month 11: 0.07
Enter rainfall for Year 2, Month 12: 0.16
>>> 
>>> total_months = 12 * num_years
>>> average_rainfall = total_rainfall / total_months
>>> print(f"\nNumber of months: {total_months}")

Number of months: 24
>>> print(f"Total inches of rainfall: {total_rainfall:.2f}")
Total inches of rainfall: 48.90
>>> 
>>> 
>>> num_years = int(input("Enter the number of years: "))
Enter the number of years: 2
>>> total_rainfall = 0
>>> total_months = 12 * num_years
>>> 
>>> for year in range(1, num_years + 1):
...     for month in range(1, 13):
...        total_rainfall += float(input(f"Enter rainfall for Year {year}, Month {month}: "))
... 
...        
Enter rainfall for Year 1, Month 1: 0.78
Enter rainfall for Year 1, Month 2: 0.94
Enter rainfall for Year 1, Month 3: 1.17
Enter rainfall for Year 1, Month 4: 0.06
Enter rainfall for Year 1, Month 5: 2.59
Enter rainfall for Year 1, Month 6: 0.58
Enter rainfall for Year 1, Month 7: 0.99
Enter rainfall for Year 1, Month 8: 1.45
Enter rainfall for Year 1, Month 9: 1.25
Enter rainfall for Year 1, Month 10: 0.46
Enter rainfall for Year 1, Month 11: 0.47
Enter rainfall for Year 1, Month 12: 1.18
Enter rainfall for Year 2, Month 1: 0.22
Enter rainfall for Year 2, Month 2: 0.80
Enter rainfall for Year 2, Month 3: 2.80
Enter rainfall for Year 2, Month 4: 2.02
Enter rainfall for Year 2, Month 5: 3.65
Enter rainfall for Year 2, Month 6: 0.84
Enter rainfall for Year 2, Month 7: 0.34
Enter rainfall for Year 2, Month 8: 0.27
Enter rainfall for Year 2, Month 9: 0.28
Enter rainfall for Year 2, Month 10: 0.08
Enter rainfall for Year 2, Month 11: 0.07
Enter rainfall for Year 2, Month 12: 0.16
>>> 
>>> average_rainfall = total_rainfall / total_months
>>> print(f"\nNumber of months: {total_months}")

Number of months: 24
>>> print(f"Total inches of rainfall: {total_rainfall:.2f}")
Total inches of rainfall: 23.45
>>> print(f"Average rainfall per month: {average_rainfall:.2f}")
Average rainfall per month: 0.98
