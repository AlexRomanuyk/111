def is_prime(n):
  'Return True if n is a prime number otherwise return False'
  if n <= 1:
      return False
  else:
      for num in range(2, n-1):
          if n % num == 0:
              return False
      return True
