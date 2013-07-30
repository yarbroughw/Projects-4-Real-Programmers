from collections import deque
    
divisors = deque()
primefactors = []

inputNum = input("Enter number to factor: ")
divisors.append(inputNum)

while len(divisors) > 0:
    div = divisors.popleft()
    for n in range(2, int(div**0.5) + 1):
        if div % n == 0:
            divisors.extend([n, div/n])
            break
    else:
        primefactors.append(div)

print "Prime factors of " + str(inputNum) + ": " + str(primefactors)