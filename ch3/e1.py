def e1(n):
   if n <= 0:
      return 5
   else:
      return (3*e1(n-1)) % 150

for n in range(1, 11):
   print(n, e1(n))

