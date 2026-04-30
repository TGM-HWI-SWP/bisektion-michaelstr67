def polynom(x):
    return 2 * x + x**2 + 3 * x**3 - x**4

# Aufgabe 8: Iterative Version der Bisektion
def bisektion_iter(f, a, b, epsilon):
    """ Iterative Version der Bisektion, die die Anzahl der Iterationen zurückgibt
    Args:
        f (function): Funktion, für die die Nullstelle gefunden werden soll
        a (float): Untere Grenze des Intervalls
        b (float): Obere Grenze des Intervalls
        epsilon (float): Gewünschte Genauigkeit"""
    if f(a) * f(b) >= 0:
        print("Kein Vorzeichenwechsel.")
        return None, 0

    iteration = 0 # Zähler für die Iterationen

    while (b - a) / 2 > epsilon: # Solange die Genauigkeit nicht erreicht ist
        c = (a + b) / 2

        if f(a) * f(c) < 0: # Vorzeichenwechsel zwischen a und c
            b = c
        else:
            a = c

        iteration += 1 # Erhöhung der Iterationszähler

    return (a + b) / 2, iteration # Rückgabe der gefundenen Nullstelle und der Anzahl der Iterationen

# Printer für die Aufgabe 8
def solver3():
    print("=== Aufgabe 8 ===")

    x1, i1 = bisektion_iter(polynom, 3, 4, 0.01)
    x2, i2 = bisektion_iter(polynom, 3, 4, 0.00000001)

    print("Intervall: [3, 4]") #Ausgabe des Intervalls, in dem die Nullstelle gesucht wurde
    print("epsilon 10^-2:") #Ausgabe der Genauigkeit, mit der die Nullstelle gefunden wurde
    print("Nullstelle:", x1) #Ausgabe der gefundenen Nullstelle für epsilon 10^-2
    print("Iterationen:", i1) #Ausgabe der Anzahl der Iterationen, die für die Berechnung der Nullstelle mit epsilon 10^-2 benötigt wurden

    print("epsilon 10^-8:") #Ausgabe der Genauigkeit, mit der die Nullstelle gefunden wurde
    print("Nullstelle:", x2) #Ausgabe der gefundenen Nullstelle für epsilon 10^-8
    print("Iterationen:", i2) #Ausgabe der Anzahl der Iterationen, die für die Berechnung der Nullstelle mit epsilon 10^-8 benötigt wurden


if __name__ == "__main__":
    solver3()