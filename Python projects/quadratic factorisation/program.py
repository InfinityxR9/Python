# to generate a program to factorise a given quadratic equation

def factorise(a, b, c):
    print(a, b, c)

    product = a*c
    sum = b

    absProduct = abs(product)
    factors = []

    for r1 in range(1, absProduct+1):
        for r2 in range(1, r1+1):
            if r1*r2 == absProduct:
                if product <= 0:
                    factors.append((-r1, r2))
                    factors.append((r1, -r2))
                else:
                    factors.append((r1, r2))
                    factors.append((-r1, -r2))

    rFactors = ()

    for (r1, r2) in factors:
        if r1 + r2 == sum:
            rFactors = (r1, r2)

    print(factors, '\n', rFactors)
    
    r1 = rFactors[0]
    r2 = rFactors[1]

    if a == 1:
        if r1 != 0 and r2 != 0:        
            if r1 > 0 and r2 > 0: print(f"The factorisation of given Qudratic equation is (x + {r1})(x + {r2})")
            if r1 < 0 and r2 < 0: print(f"The factorisation of given Qudratic equation is (x  {r1})(x  {r2})")
            if r1 > 0 and r2 < 0: print(f"The factorisation of given Qudratic equation is (x + {r1})(x  {r2})")
            if r1 < 0 and r2 > 0: print(f"The factorisation of given Qudratic equation is (x  {r1})(x + {r2})")

factorise(1, 5, 6)
