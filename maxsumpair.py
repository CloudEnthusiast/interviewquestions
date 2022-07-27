# python 3.6
# 1. given an array of numbers.
# 2. Find a pair with maximum sum and having the same sum of digits. 
# 3. Print the sum of that pair, if it exists. Otherwise, print -1.

def sum_of_digits(num):
    tot = 0
    while (num):
        tot += num % 10 # remainder
        num = num // 10 # quotient
    return tot

def solution(A):
    n = len(A)
    # k:v = sumofdigits_of_num : max_num_with_same_sumofdigits
    mp = {}
    ans = -1
    # pair of numbers
    numi = 0
    numj = 0

    for i in range(n):
        ds = sum_of_digits(A[i])

        if ds not in mp:
            mp[ds] = 0

        if (mp[ds] != 0):
            if (A[i] + mp[ds] > ans):
                numi = A[i]
                numj = mp.get(ds)
                ans = numi + numj

        # update value in map
        mp[ds] = max(A[i], mp[ds])
    
    # print(f"{numi} {numj} {ans}")
    return ans
