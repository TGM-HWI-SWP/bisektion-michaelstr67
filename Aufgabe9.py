import math
from Aufgabe5 import bisektion
from Aufgabe6 import regula_falsi
from Aufgabe7 import bisektion_grafik


def funktion(a):
    return a * math.cosh(50 / a) - a - 10


def laenge(a):
    return 2 * a * math.sinh(50 / a)


def ausgabe(name, a):
    if a is not None:
        print(name)
        print("Krümmungsradius a:", a)
        print("Länge der Leitung:", laenge(a), "m")
    else:
        print(name, ": Keine Lösung gefunden.")


def solver4():
    print("=== Aufgabe 9 ===")

    a_bisektion = bisektion(funktion, 120, 130, 0.00001)
    a_regula = regula_falsi(funktion, 120, 130, 0.00001)

    ausgabe("Bisektion:", a_bisektion)
    ausgabe("Regula Falsi:", a_regula)

    print("Visualisierung wird gestartet...")
    a_grafik = bisektion_grafik(funktion, 120, 130, 0.00001)

    print("Grafische Lösung:", a_grafik)


if __name__ == "__main__":
    solver4()