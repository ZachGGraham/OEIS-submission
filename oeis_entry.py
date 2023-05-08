ints = []


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
integers = [1,2,3,4,5,6,7,8,9,10]

def hamming_distance(x,y):
    return bin(x ^ y).count('1')

def next_number(a,h):
    x = a
    while hamming_distance(a,x) < h:
        x += 1
    else:
        return x

def hamming_primes(n):
    a = 0
    for i in range(0,n):
        b = next_number(a,primes[i])
        ints.append(b)
        a = b

hamming_primes(10)
print(ints)
