start = 0
numberofsteps = 128 
x = start 

for n in range(0, numberofsteps):   
  print(n, x)   
  g = (x ** 3) - (2 * x) - 5
  gprime = (3 * x ** 2) - 2
  x -= g/gprime 
