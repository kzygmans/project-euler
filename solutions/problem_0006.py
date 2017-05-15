def solution():
    sumOfSquares = 0
    squareOfSum = 0
    for i in range(1, 101):
        sumOfSquares += i ** 2
        squareOfSum += i
    squareOfSum *= squareOfSum

    print 'Answer: %i' % (squareOfSum - sumOfSquares)

if __name__ == '__main__':
    solution()