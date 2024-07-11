# to generate a program to factorise a given quadratic equation for integral coefficients
import math

def factorise(a, b, c):
    if a == 0: print("Don't fuck with quadratics...")
    else:
        if c != 0:
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

            print(rFactors)

            if not not rFactors:
                r1 = rFactors[0]
                r2 = rFactors[1]
                if a > 0: f1 = math.gcd(a, r1)
                else: f1 = -math.gcd(a, r1)
                

                if r2 >= 0: f2 = math.gcd(r2, c)
                else: f2 = -math.gcd(r2, c)

                # Linear factor 1
                xCoeff1 = f1
                const1 = f2


                # Linear factor 2
                xCoeff2 = a/f1
                const2 = r1/f1

                if const1 > 0 and const2 > 0: print(f"The factorisation of given Qudratic equation is ({xCoeff1}x + {const1})({xCoeff2}x + {const2})")
                elif const1 < 0 and const2 < 0: print(f"The factorisation of given Qudratic equation is ({xCoeff1}x  {const1})({xCoeff2}x  {const2})")
                elif const1 > 0 and const2 < 0: print(f"The factorisation of given Qudratic equation is ({xCoeff1}x + {const1})({xCoeff2}x  {const2})")
                elif const1 < 0 and const2 > 0: print(f"The factorisation of given Qudratic equation is ({xCoeff1}x  {const1})({xCoeff2}x + {const2})")

            else:
                print("Factorisation doesn't exist")

        else:
            if b != 0:
                divFactor = math.gcd(a, b)

                fac1 = a/divFactor
                fac2 = b/divFactor

                if fac2 > 0: print(f"The factorisation of given Qudratic equation is ({divFactor}x)({fac1}x + {fac2})")
                elif fac2 < 0: print(f"The factorisation of given Qudratic equation is ({divFactor}x)({fac1}x {fac2})")

            else: print(f"The factorisation of given Qudratic equation is {a}(x)(x)")

# factorise(14, -41, 15)
# factorise(-1, 5, -6)
# factorise(-14, 41, -15)
# factorise(-1, -5, -6)
# factorise(1, 5, -6)
# factorise(1, 5, 6)
# factorise(1, -5, 6)
# factorise(25, 34, 9)
# factorise(25, -34, 9)
# factorise(-25, 34, -9)
# factorise(-1, 1, -1)
# factorise(0, 1, -1)
# factorise(1, 0, -1)
# factorise(1, 1, 0)
# factorise(5, 2, 0)
# factorise(-5, 3, 0)
# factorise(-7, -4, 0)
# factorise(-7, 14, 0)
# factorise(4,0,-16)
factorise(0,0,-16)
factorise(0,0,0)
factorise(4,0,0)
