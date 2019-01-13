#Given: Positive integers n<=40 and k<=5.

#Return: The total number of rabbit pairs that will be present after n months,
#if we begin with 1 pair and in each generation, every pair of reproduction-age
#rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

#Sample 1
#Input: 5 3
#Output: 19
#Sample 2
#Input: 29 2
#Output: 178956971

#1  2  3  4  5
#1  1  4  7  19

#f1 = 1
#f2 = 1
#fn = f(n-1) + k*f(n-2)

def rabbitmaker(n, k):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return rabbitmaker(n - 1, k) + rabbitmaker(n - 2, k) * k

x = rabbitmaker(29, 2)
print(x)
