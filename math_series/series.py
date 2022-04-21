import math

def fibonacci(n):
  '''This function takes the nth position in the Fibonacci Series and returns
  the value for that position. The Fibonacci Series starting integers are 0 and 1.'''
  if n == 0:
    return 0
  elif n <= 2:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)
      
  

def lucas(n):
  '''This function takes in the nth position in the Lucas Series and returns the
  value for that postion. The Lucas Series starting integers are 2 and 1.'''
  if n == 0:
    return 2
  elif n == 1:
    return 1
  else:
    return lucas(n-1) + lucas(n-2)

def sum_series(n, n1=0, n2=1):
  '''This function takes in a number (n) that determines the nth position value to return. The 2 optional parameters (n1 and n2)
  are not required for returning the position within the Fibonacci Series. However, n1 and n2 should be set to 2 and 1, respectively
  to receive values from the Lucas Series.'''
  if n == 0:
    return n
  elif n == 1:
    return n
  elif n1 == 2 and n2 == 1:
    return lucas(n)
  else:
    return sum_series(n - 1, n1, n2) + sum_series(n - 2, n1, n2)