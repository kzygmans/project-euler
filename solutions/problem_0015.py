def solution():
    m = 20
    n = 20

    grid = [[1 for x in range(m+1)] for y in range(n+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]

    print 'Answer: %i' % grid[20][20]

if __name__ == '__main__':
    solution()
