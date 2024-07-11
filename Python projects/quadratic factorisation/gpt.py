def factorize_quadratic(a, b, c):
    # Step 1: Input the coefficients
    print(f"Quadratic equation: {a}x^2 + {b}x + {c}")

    # Step 2: Compute the product ac
    ac = a * c
    print(f"Step 2: Compute the product ac = {a} * {c} = {ac}")

    # Step 3: Find the factors of ac that add up to b
    factors = []
    for i in range(1, abs(ac) + 1):
        if ac % i == 0:
            factors.append((i, ac // i))
            factors.append((-i, -ac // i))
    
    factor_pair = None
    for f1, f2 in factors:
        if f1 + f2 == b:
            factor_pair = (f1, f2)
            break
    
    if factor_pair is None:
        print("The quadratic equation cannot be factorized by middle term splitting.")
        return

    print(f"Step 3: Factors of {ac} that add up to {b} are {factor_pair[0]} and {factor_pair[1]}")

    # Step 4: Split the middle term
    middle_term_1, middle_term_2 = factor_pair
    print(f"Step 4: Split the middle term {b}x into {middle_term_1}x and {middle_term_2}x")
    print(f"{a}x^2 + {b}x + {c} = {a}x^2 + {middle_term_1}x + {middle_term_2}x + {c}")

    # Step 5: Factor by grouping
    if a != 1:
        # If a is not 1, it must be included in the factoring
        print(f"Step 5: Group the terms: {a}x^2 + {middle_term_1}x and {middle_term_2}x + {c}")
        print(f"Factor out the common terms:")
        print(f"{a}x^2 + {middle_term_1}x = {a}x(x + {middle_term_1//a})")
        print(f"{middle_term_2}x + {c} = {middle_term_2}(x + {c//middle_term_2})")
        print(f"Combining: {a}x(x + {middle_term_1//a}) + {middle_term_2}(x + {c//middle_term_2})")
    else:
        print(f"Step 5: Group the terms: x^2 + {middle_term_1}x and {middle_term_2}x + {c}")
        print(f"Factor out the common terms:")
        print(f"x^2 + {middle_term_1}x = x(x + {middle_term_1})")
        print(f"{middle_term_2}x + {c} = {middle_term_2}(x + {c//middle_term_2})")
        print(f"Combining: x(x + {middle_term_1}) + {middle_term_2}(x + {c//middle_term_2})")
        
    # Final result
    print(f"The factorized form of the quadratic equation is: ({a}x + {middle_term_1})(x + {c//middle_term_2})")

# Example usage:
factorize_quadratic(1, -5, 6)
