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
    count = 0
    i = 2
    while True:
        if(isPrime(i)):
            count += 1
            if(count == 10001):
                print 'Answer: %i' % i
                break
        i += 1

if __name__ == '__main__':
    solution()