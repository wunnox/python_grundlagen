def fib(n):
    a=c=0
    b = 1
    while c < n:
        c = a + b
        print(b)
        a = b
        b = c
