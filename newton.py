start = -1
numberofsteps = 8
x = start

for n in range(1, numberofsteps):
  print(n, x)
  g = (4 * x ** 3) + (3 * x ** 2) + (2 * x) + 2
  gprime = (12 * x ** 2) + (6 * x) + 2
  x -= g/gprime
