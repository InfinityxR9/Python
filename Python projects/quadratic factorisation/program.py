# to generate a program to factorise a given quadratic equation for integral coefficients
import math

def factorise(a, b, c):
    if a == 0: print("Don't fuck with quadratics...")
    else:
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
        

        if not not rFactors:
            r1 = rFactors[0]
            r2 = rFactors[1]
            if a == 1:
                if r1 != 0 and r2 != 0:        
                    if r1 > 0 and r2 > 0: print(f"The factorisation of given Qudratic equation is (x + {r1})(x + {r2})")
                    if r1 < 0 and r2 < 0: print(f"The factorisation of given Qudratic equation is (x  {r1})(x  {r2})")
                    if r1 > 0 and r2 < 0: print(f"The factorisation of given Qudratic equation is (x + {r1})(x  {r2})")
                    if r1 < 0 and r2 > 0: print(f"The factorisation of given Qudratic equation is (x  {r1})(x + {r2})")

        else:
            print("Factorisation doesn't exist")

# factorise(1, 2*math.sqrt(3), 3)
