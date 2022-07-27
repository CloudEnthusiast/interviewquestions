# given an array A of N integers, returns the smallest 
# positive integer (greater than 0) that does not occur in A

# Testing for the presence of a number in a set is fast in Python.

def minpositive(a):
  A = set(a)
  ans = 1
  while ans in A:
    ans += 1
  return ans
