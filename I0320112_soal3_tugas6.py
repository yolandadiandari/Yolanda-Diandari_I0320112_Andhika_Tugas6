for n in range(10, 25):
    if n == 1:
        print(n, "bukan prima")
    elif n == 2:
        print(n, "adalah bilangan prima")
    else:
        for i in range(2, n):
            if n % i == 0:
                print(n, "bukan prima")
                break
        else:
            print(n, "adalah bilangan prima")

