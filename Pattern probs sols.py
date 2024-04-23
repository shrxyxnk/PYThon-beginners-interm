Pattern-Eleven solution
n = int(input())
spaces = n - 1
for row in range(1, n + 1):
     
   for space in range(spaces):
       print(" ", end = "")
   spaces -= 1
 
   val = 1
   for num in range(2 * row - 1):
       print(val, end = "")
       val += 1
   print()
Pattern-Twelve solution
n = int(input())
spaces = 0
for row in range(n, 0, -1):
   val = 1
   for space in range(spaces):
       print(" ", end = " ")
   spaces += 1
 
   for num in range(2 * row - 1):
       print(val, end = " ")
       val += 1
   print()
Pattern-Thirteen solution
n = int(input())
val = 10
for i in range(1, n + 1):
   for j in range(i):
       print(val, end = " ")
       val += 10
   print()
Pattern-Fourteen solution
n = int(input())
for i in range(1, n + 1):
   for j in range(i):
       if i % 2 == 0:
           print("#", end = "")
       else:
           print("*", end = "")
   print()
Pattern-Fifteen solution:
n = int(input())
for i in range(1, n + 1):
   val1 = i
   val2 = 1
   for j in range(i):
       if i % 2 == 0:
           print(val1, end = " ")
           val1 -= 1
       else:
           print(val2, end = " ")
           val2 += 1
   print()
Pattern-Sixteen solution:
        
n = int(input())
for i in range(1, n + 1):
   for j in range(i):
       if i % 2 == 0:
           print("@", end = "")
       else:
           print(i, end = "")
   print()
Pattern-Seventeen solution:
n = int(input())
spaces = 0
for i in range(n, 0, -1):
  for j in range(spaces):
      print(" ",  end = " ")
  spaces += 1
   letter = 65
  for j in range(i):
      print(chr(letter), end = " ")
      letter += 1
  print()
Pattern-Eighteen solution
n = int(input())
spaces = 0
for i in range(n, 0, -1):
   for j in range(spaces):
       print(" ", end = " ")
   spaces += 1
   for j in range(2 * i - 1):
       print("*", end = " ")
   print()
Pattern-Nineteen solution
n = int(input())
spaces = n - 1
stars = 1
for row in range(1, n + 1):
  for space in range(spaces):
      print(" ", end = " ")
  spaces -= 1
   for star in range(stars):
      print("*", end = " ")
  stars += 2
  print()
 stars -= 4
spaces = 1
for row in range(1, n):
  for space in range(spaces):
      print(" ", end = " ")
  spaces += 1
   for star in range(stars):
      print("*", end = " ")
  stars -= 2
  print()
Pattern-Twenty solution
n = int(input())
stars = 2 * n - 1
spaces = 0
for row in range(n):
   for space in range(spaces):
       print(" ", end = " ")
   spaces += 1
 
   for star in range(stars):
       print("*", end = " ")
   stars -= 2
   print()
 
stars += 4
spaces -= 2
for row in range(1, n):
   for space in range(spaces):
       print(" ", end = " ")
   spaces -= 1
 
   for star in range(stars):
       print("*", end = " ")
   stars += 2
   print()
