import math
from Aufgabe5 import bisektion
from Aufgabe6 import regula_falsi

# Aufgabe 9: Krümmungsradius und Länge einer Leitung
def funktion(a):
    return a * math.cosh(50 / a) - a - 10 # Funktion, die den Krümmungsradius a mit der Länge der Leitung in Beziehung setzt

# Berechnung der Länge der Leitung basierend auf dem Krümmungsradius a
def laenge(a):
    return 2 * a * math.sinh(50 / a) #Länge der Leitung basierend auf dem Krümmungsradius a

# Ausgabe der Ergebnisse
def ausgabe(name, a):
    """ Ausgabe der Ergebnisse für die Krümmungsradius a und die Länge der Leitung 
    Args:
        name (str): Name der Methode (z.B. "Bisektion" oder "Regula Falsi")
        a (float): Gefundener Krümmungsradius a
    """
    if a is not None:
        print(name) #Ausgabe des Namens der Methode
        print("Krümmungsradius a:", a) #Ausgabe des gefundenen Krümmungsradius a
        print("Länge der Leitung:", laenge(a), "m") #Ausgabe der Länge der Leitung basierend auf dem gefundenen Krümmungsradius a
    else:
        print(name, ": Keine Lösung gefunden.")

#solver4() führt die Berechnung der Krümmungsradius a und der Länge der Leitung durch, 
#indem es die Funktionen bisektion und regula_falsi verwendet, um die Nullstelle der Funktion zu finden,
#die den Krümmungsradius a mit der Länge der Leitung in Beziehung setzt. Die Ergebnisse werden dann mit der Funktion ausgabe ausgegeben.
def solver4():
    print("=== Aufgabe 9 ===")

    a_bisektion = bisektion(funktion, 50, 150, 0.00001)
    a_regula = regula_falsi(funktion, 50, 150, 0.00001)

    ausgabe("Bisektion:", a_bisektion)
    ausgabe("Regula Falsi:", a_regula)



if __name__ == "__main__":
    solver4()