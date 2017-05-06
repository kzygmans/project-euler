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
    number = 600851475143
    i = 3
    primeFactors = []
    while(i <= number):
        if(number % i == 0 and isPrime(i)):
            primeFactors.append(i)
            number /= i
        i += 2

    print primeFactors[-1]

if __name__ == '__main__':
    solution()