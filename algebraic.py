def is_group(numbers, op):
    #closure
    for a in numbers:
        for b in numbers:
            if op(a, b) not in numbers:
                return False

    # Associativity
    for a in numbers:
        for b in numbers:
            for c in numbers:
                if op(op(a, b), c) != op(a, op(b, c)):
                    return False

    # Identity element
    identity = None
    for e in numbers:
        if all(op(e, x) == x and op(x, e) == x for x in numbers):
            identity = e
            break
    if identity is None:
        return False

    # Inverse elements
    for a in numbers:
        found_inverse = False
        for b in numbers:
            if op(a, b) == identity:
                found_inverse = True
                break
        if not found_inverse:
            return False

    return True

def is_ring(numbers, add, mul):
    if not is_group(numbers, add):
        return False

    # Commutativity of addition
    for a in numbers:
        if any(add(a, b) != add(b, a) for b in numbers):
            return False

    # Closure under multiplication
    for a in numbers:
        for b in numbers:
            if mul(a, b) not in numbers:
                return False

    # Associativity of multiplication
    for a in numbers:
        for b in numbers:
            for c in numbers:
                if mul(a, mul(b, c)) != mul(mul(a, b), c):
                    return False

    # Distributive property
    for a in numbers:
        for b in numbers:
            for c in numbers:
                if mul(a, add(b, c)) != add(mul(a, b), mul(a, c)):
                    return False
                
    return True

numbers = {0, 1, 2, 3}

add = lambda x, y: (x + y) % 4
mul = lambda x, y: (x * y) % 4

if is_group(numbers, add):
    print("The set forms a group under addition modulo 4")

    if is_ring(numbers, add, mul):
        print("The set is a ring under addition and multiplication modulo 4")
