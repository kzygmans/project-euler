def isPrime(n):
    """Checking if number is prime number"""
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True

def solution():
    a_max = 0
    b_max = 0
    max_number = 0

    for a in range(-1000, 1001):
        for b in range(-1000, 1001):
            max_tmp = 0
            n = 0
            while(True):
                f = n*n + a*n + b
                if(isPrime(f)):
                    max_tmp += 1
                    n += 1
                else:
                    break
            if(max_tmp > max_number):
                a_max = a
                b_max = b
                max_number = max_tmp

    print 'Answer: %i' % (a_max * b_max)

if __name__ == '__main__':
    solution()