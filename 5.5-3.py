start = 1
numberofsteps = 16 
x = start 


for n in range(0, numberofsteps): 
  print(n, x) 
  g = (x ** 3) + (2 * x ** 2) + (10 * x) - 20
  gprime = (3 * x ** 2) + (4 * x) + 10
  x -= g/gprime
