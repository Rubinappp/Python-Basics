#without using recursion
def factorial(n):
  fact=1
  for i in range(n):
    fact=fact*(i+1)
  return fact
print(factorial(5))

# using recursion
# n! =   1 * 2 * 3 * 4*...... * n 
# n! =   [1 * 2 * 3 * 4 *......*n-1 ]* n 
# n! =   n * (n-1)! 
def factorial_iter(n):
  fact=1
  if ( n==1 or n==0):
   return 1
  else:
    return(fact*fact(n-1))
    
print(factorial(5))

