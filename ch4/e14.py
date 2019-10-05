def x(n):
    if n == 1:
        return 23
    if n == 2:
        return 66
    return (3*x(n-1) + 5*x(n-2)) % 100

def u(n):
    return x(n)/100

for n in range(1, 15):
    print(n, u(n))

    
