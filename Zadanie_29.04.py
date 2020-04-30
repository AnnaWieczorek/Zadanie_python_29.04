n = int(input())
fib = [0, 1]
for i in range(n-2):
    new = fib[i] + fib[i+1]
    fib.append(new)
print(fib)
