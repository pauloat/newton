#start = 1
start = 0
numberofsteps = 16
x = start for n in range(0, numberofsteps):
  print(n, x)
  g = (x ** 5) - (3 * x) + 1
  gprime = (5 * x ** 4) - 3
  x -= g/gprime 
