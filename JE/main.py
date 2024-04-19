def baseDeux(n):
    m = n
    sortie = ""
    while m >= 1:
        print(m)
        print(m % 2)
        if m % 2 == 1:
            sortie += "1"
        else:
            sortie += "0"
        m = m / 2
    print(sortie)

baseDeux(42)