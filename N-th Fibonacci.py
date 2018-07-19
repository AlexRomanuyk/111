def nth_fib(n):
  
  a, b = 0, 1
  iterable = 2
  
  if n == 1:
      return 0
  elif n == 2:
      return 1
  else: 
      while iterable < n:
          a, b = b, a + b
          iterable += 1
      return b
