# R1.1:
def is_multiple(n, m):
    return (n % m) is 0


# R1.2
def is_even(k):
    return (k % 2) is 0


# R1.3
def minmax(data):
    if type(data) is list:
        data = sorted(data)
        return data[0], data[-1]
    else:
        print('Please enter data as list!')


# R1.4
def sumofsq(n):
    return n*n + sumofsq(n-1) if (n > 0) else n


# R1.5
def comp_sumofsq(n):
    return sum(n*n for n in range(n+1) if n > 0)


# R1.6 !! Its NOT correct!!
def sumofoddsq(n):
    while n > 0:
        if (n % 2 is not 0):
            return n * n + sumofoddsq(n - 1)
        else:
            print('Not a valid number')


# R1.7
def comp_sumofoddsq(n):
    return sum(n*n for n in range(n+1) if n % 2 is not 0)


# R1.8: s[j] = s[k+len(s)]
# R1.9: (k*10 for k in range(5,9))
# R1.10: (k*2 for k in range(4,-5,-1))
# R1.11 [2**k for k in range(0,9)]
