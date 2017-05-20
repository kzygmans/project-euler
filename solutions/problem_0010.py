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
    sum = 0
    for i in range(2000000):
        if(isPrime(i)):
            sum += i
    print 'Answer: %i' % sum

if __name__ == '__main__':
    solution()