def nextPrime(n):
    while True:
        n = n + 1
        if isPrime(n):
            return n
    
def isPrime(n):
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime = int(raw_input("Enter number: "))
prime = nextPrime(prime)
print "Next prime: " + str(prime)

while 1:
    choice = raw_input("Compute next prime? (y/n): ")
    if choice == "y":
        prime = nextPrime(prime)
        print "Next prime: " + str(prime)
    elif choice == "n":
        break
    else:
        print "Improper input."