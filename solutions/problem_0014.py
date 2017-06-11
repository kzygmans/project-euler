def solution():
    longest_chain = 0
    number = 0

    for i in range(2, 1000001):
        term = i
        chain_length = 1

        while(term != 1):
            if(term % 2 == 0):
                term = term/2
            else:
                term = term * 3 + 1
            chain_length += 1

        if(longest_chain < chain_length):
            longest_chain = chain_length
            number = i

    print 'Answer: %i' % number

if __name__ == '__main__':
    solution()