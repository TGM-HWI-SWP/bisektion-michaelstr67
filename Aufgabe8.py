def polynom(x):
    return 2 * x + x**2 + 3 * x**3 - x**4


def bisektion_iter(f, a, b, epsilon):
    if f(a) * f(b) >= 0:
        print("Kein Vorzeichenwechsel.")
        return None, 0

    iteration = 0

    while (b - a) / 2 > epsilon:
        c = (a + b) / 2

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        iteration += 1

    return (a + b) / 2, iteration


def solver3():
    print("=== Aufgabe 8 ===")

    x1, i1 = bisektion_iter(polynom, 3, 4, 0.01)
    x2, i2 = bisektion_iter(polynom, 3, 4, 0.00000001)

    print("Intervall: [3, 4]")
    print("epsilon 10^-2:")
    print("Nullstelle:", x1)
    print("Iterationen:", i1)

    print("epsilon 10^-8:")
    print("Nullstelle:", x2)
    print("Iterationen:", i2)


if __name__ == "__main__":
    solver3()