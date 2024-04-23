Pattern-One solution
n = int(input())
for row in range(1, n + 1):
   for star in range(row):
       print("*", end = "")
   print()
Pattern-Two solution
n = int(input())
for row in range(1, n + 1):
   for col in range(1, row + 1):
       print(col, end = "")
   print()
Pattern-Three solution
n = int(input())
for row in range(n):
   for col in range(n):
       print("*", end = "")
   print()
Pattern-Four solution
n = int(input())
spaces = 0
for row in range(n):
   for space in range(spaces):
       print(" ", end = "")
   for star in range(n):
       print("*", end = "")
   spaces += 1
   print()
Pattern-Five solution
n = int(input())
for row in range(n, 0, -1):
   for star in range(row):
       print("*", end = "")
   print()

Pattern-Six solution
n = int(input())
spaces = n - 1
stars = 1
for row in range(1, n + 1):
   for space in range(spaces):
       print(" ", end = "")
     
   spaces -= 1
 
   for star in range(stars):
       print("*", end = "")
   stars += 1
   print()
Pattern-Seven solution
n = int(input())
spaces = n - 1
for row in range(1, n + 1):
     
   for space in range(spaces):
       print(" ", end = "")
   spaces -= 1
 
   for col in range(1, row + 1):
       print(col, end = "")
   print()
Pattern-Eight solution
n = int(input())
stars = n
spaces = 0
for row in range(n):
   for space in range(spaces):
       print(" ", end = "")
     
   spaces += 1
 
   for star in range(stars):
       print("*", end = "")
   stars -= 1
 
   print()
Pattern-Nine solution
n = int(input())
spaces = n - 1
stars = 1
for row in range(n):
   for space in range(spaces):
       print(" ", end = "")
   spaces -= 1
 
   for star in range(stars):
       print("*", end = "")
   stars += 2
   print()
Pattern-Ten solution
n = int(input())
spaces = 0
for row in range(n, 0, -1):
   for space in range(spaces):
       print(" ", end = "")
     
   spaces += 1
 
   for star in range(2 * row - 1):
       print("*", end = "")
   print()
