import math


def funktion_aus_text_erstellen(formel: str):
    erlaubte_werte = {
        "x": 0,
        "math": math,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "sqrt": math.sqrt,
        "sinh": math.sinh,
        "cosh": math.cosh,
        "pi": math.pi,
        "e": math.e,
    }

    def f(x: float) -> float:
        erlaubte_werte["x"] = x
        return eval(formel, {"__builtins__": {}}, erlaubte_werte)

    return f


def bisektion(f,a ,b , epsilon):
    try:
        if f(a) * f(b) >= 0:
            print("Kein Vorzeichenwechsel")
            return None

        while (b - a) / 2 > epsilon:
            c = (a + b) / 2

            if f(a) * f(c) < 0:
                b = c
            else:
                a = c

        return (a + b) / 2

    except:
        print("Fehler")
        return None


def solver():
   print("=== Aufgabe 5 ===")
   print("1 - Eigene Funktion")
   print("2 - Testfälle")

   wahl = input("Auswahl: ")

   if wahl == "1":
    formel = input("Funktion: ")
    a = float(input("a: "))
    b = float(input("b: "))
    epsilon = float(input("epsilon: "))

    f = funktion_aus_text_erstellen(formel)
    x = bisektion(f, a, b, epsilon)

    print("Nullstelle:", x)

   elif wahl == "2":
    for n in [25, 81, 144]:
        f = funktion_aus_text_erstellen(f"x**2 - {n}")
        x = bisektion(f, 0, n, 0.00001)

        print("n =", n, "| numerisch:", x, "| exakt:", math.sqrt(n)) 

if __name__ == "__main__":
    
    solver()