start = #numer closest to the root we want
numberofsteps = 8
x = start

for n in range(1, numberofsteps):
  print(n, x) 
  g = # g(x), the polynomial we are seaching the roots
  gprime = # g'(x), derivative of g(x)
  x -= g/gprime
