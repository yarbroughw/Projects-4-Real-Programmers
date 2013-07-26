
n = int(raw_input("Enter index of desired number in fibo sequence: "))

fibo = []

for i in range(0,n):
    if i < 2:
        fibo.append(1)
    else:
        fibo.append(fibo[i-1] + fibo[i-2])
        
print fibo[-1]