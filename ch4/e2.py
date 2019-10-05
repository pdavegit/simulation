def e2(n):
    if n <= 0:
        return 3
    else:
        return (5*e2(n-1) + 7) % 200

for n in range(1, 11):
    print(n, e2(n))
