# given an array A of N integers, returns the smallest 
# positive integer (greater than 0) that does not occur in A

# Testing for the presence of a number in a set is fast in Python.

# ex 1:
# A = [0, -1, 4, 5]
# output is 1

# ex 2:
# A = [3, 1, -1, -22.4, 3, 5]
# outpu is 2

def minpositive(a):
  A = set(a)
  ans = 1
  while ans in A:
    ans += 1
  return ans
