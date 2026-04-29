import math
from Aufgabe5 import funktion_aus_text_erstellen


def regula_falsi(f, a, b, epsilon):
    while True:
        c = b - f(b) * (b - a) / (f(b) - f(a))

        if abs(f(c)) < epsilon:
            return c

        if f(a) * f(c) < 0:
            a = c
        else:
            b = c





def solver2():
    print("=== Aufgabe 6 ===")
    print("1 - Eigene Funktion")
    print("2 - Testfälle")

    wahl = input("Auswahl: ")

    if wahl == "1":
        formel = input("Funktion: ")
        a = float(input("a: "))
        b = float(input("b: "))
        epsilon = float(input("epsilon: "))

        f = funktion_aus_text_erstellen(formel)
        x = regula_falsi(f, a, b, epsilon)

        print("Nullstelle:", x)

    elif wahl == "2":
        for n in [25, 81, 144]:
            f = funktion_aus_text_erstellen(f"x**2 - {n}")
            x = regula_falsi(f, 0, n, 0.00001)

            print("n =", n, "| numerisch:", x, "| exakt:", math.sqrt(n))


if __name__ == "__main__":
    
    solver2()