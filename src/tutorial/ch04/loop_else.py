for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "は", x, "*", n//x, "と等しい")
            break
    else:
        print(n, "は素数です")
