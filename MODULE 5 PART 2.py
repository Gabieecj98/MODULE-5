Python 3.12.1 (v3.12.1:2305ca5144, Dec  7 2023, 17:23:39) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> num_books = int(input("Enter the number of books purchased this month: "))
Enter the number of books purchased this month: 15
>>> 
>>> if num_books == 0:
...     points = 0
... 
...     
>>> elif num_books == 2:
...     
SyntaxError: invalid syntax
>>> elif num_books == 2:
...     
SyntaxError: invalid syntax
>>> 
>>> num_books = int(input("Enter the number of books purchased this month: "))
Enter the number of books purchased this month: 10
>>> 
>>> if num_books == 0:
...     points = 0
... 
...     
>>> elif num_books == 2:
...     
SyntaxError: invalid syntax
>>> num_books = int(input("Enter the number of books purchased this month: "))
Enter the number of books purchased this month: 12
>>> if num_books == 0:
...     points = 0
... elif num_books == 2:
...     points = 5
... elif num_books == 4:
...     points = 15
... elif num_books == 6:
...     points = 30
... elif num_books >= 8:
...     points = 60
... else:
    points = 0

    
print(f"You earned {points} points for pruchasing {num_books} books for this month.")
You earned 60 points for pruchasing 12 books for this month.
