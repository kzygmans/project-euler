def isPalindrome(n):
    for i in range(0, len(n)/2):
        if(n[i] != n[len(n)-i-1]):
            return False
    return True

def solution():
    palindromes = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            if(isPalindrome(str(i * j))):
                palindromes.append(i * j)
                break

    print 'Answer: %s' % max(palindromes)

if __name__ == '__main__':
    solution()