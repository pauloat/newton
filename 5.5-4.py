start = 1
numberofsteps = 16 
x = start 

for n in range(0, numberofsteps):   
  print(n, x)   
  g = (x ** 3) + (3 * x ** 2) - 5
  gprime = (3 * x ** 2) + (6 * x) 
  x -= g/gprime 
