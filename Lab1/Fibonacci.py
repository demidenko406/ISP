def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-1) + fibonacci(n-2))

amount_of_numbers = 7

if amount_of_numbers > 0:
   for i in range(amount_of_numbers):
       print(fibonacci(i))
else:
   print("Wrong Input.")
    
