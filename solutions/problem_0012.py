def solution():
    number = 0
    i = 1
    while(True):
        number += i
        divisors = 0
        m = int(number ** 0.5)
        for j in range(1, m):
            if(number % j == 0):
                divisors += 2
            if(m*m == number):
                divisors -= 1
        if(divisors > 500):
            print 'Answer: %i' % number
            break
        i += 1

if __name__ == '__main__':
    solution()