num = int(input("Digite um número: "))
fib = [0,1]

if num > 6:
    for i in range(2,num):
        fib.append((fib[i-2]+fib[i-1]))
else: 
    for i in range(2,6):
        fib.append((fib[i-2]+fib[i-1]))

if num in fib:
    print("o numero existe na série de Fibonacci")
else:
    print("o numero não existe na série de Fibonacci")

print(fib)
