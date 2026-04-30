import math
from Aufgabe5 import funktion_aus_text_erstellen

#Regula Falsi Verfahren
def regula_falsi(f, a, b, epsilon)-> float:
    while True:
        """f: Funktion, deren Nullstelle gefunden werden soll
    a: Anfang des Intervalls
    b: Ende des Intervalls
    epsilon: gewünschte Genauigkeit
    Rückgabe: Nullstelle von f im Intervall [a, b] oder None, wenn kein Vorzeichenwechsel vorliegt
    """
        c = b - f(b) * (b - a) / (f(b) - f(a))# Berechnung der neuen Näherung c

        if abs(f(c)) < epsilon:# Überprüfung der Genauigkeit
            return c

        if f(a) * f(c) < 0:#Vorzeichenwechsel zwischen a und c
            a = c
        else:
            b = c

# Printer für die Aufgabe 6
def solver2():
    print("=== Aufgabe 6 ===")
    print("1 - Eigene Funktion")
    print("2 - Testfälle")

    wahl = input("Auswahl: ")

    if wahl == "1": #Eingabe der Funktion und des Intervalls sowie der gewünschten Genauigkeit
        formel = input("Funktion: ") #Eingabe der Funktion als String
        a = float(input("a: ")) #Eingabe des Intervallanfangs
        b = float(input("b: ")) #Eingabe des Intervallendes
        epsilon = float(input("epsilon: ")) #Eingabe der gewünschten Genauigkeit

        f = funktion_aus_text_erstellen(formel) #Erstellung der Funktion aus dem eingegebenen String
        x = regula_falsi(f, a, b, epsilon) #Berechnung der Nullstelle mit dem regula falsi Verfahren

        print("Nullstelle:", x)

    elif wahl == "2": #Testfälle für die Funktion x^2 - n, um die Quadratwurzel von n zu finden
        for n in [25, 81, 144]:
            f = funktion_aus_text_erstellen(f"x**2 - {n}")
            x = regula_falsi(f, 0, n, 0.00001)

            print("n =", n, "| numerisch:", x, "| exakt:", math.sqrt(n))

    else:
        print("Ungültige Auswahl.") #Ausgabe bei ungültiger Auswahl

if __name__ == "__main__":
    solver2()