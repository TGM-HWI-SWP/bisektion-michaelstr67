import math

# Aufgabe 5: Nullstellenbestimmung mit Bisektions-Verfahren
def funktion_aus_text_erstellen(formel: str):
    """Erstellt eine Funktion aus einem gegebenen String.
    formel: Ein String, der eine mathematische Funktion beschreibt, z.B. "x**2 - 25"
    Rückgabe: Eine Funktion, die die gegebene Formel auswertet.
    """
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

# Bisektions-Verfahren
def bisektion(f,a ,b , epsilon)-> float:
    """f: Funktion, deren Nullstelle gefunden werden soll
    a: Anfang des Intervalls
    b: Ende des Intervalls
    epsilon: gewünschte Genauigkeit
    Rückgabe: Nullstelle von f im Intervall [a, b] oder None, wenn kein Vorzeichenwechsel vorliegt
    """
    try:
        if f(a) * f(b) >= 0: # Kein Vorzeichenwechsel
            print("Kein Vorzeichenwechsel")
            return None

        while (b - a) / 2 > epsilon: # Solange die Genauigkeit nicht erreicht ist
            c = (a + b) / 2 # Mitte des Intervalls

            if f(a) * f(c) < 0: # Vorzeichenwechsel zwischen a und c
                b = c
            else:
                a = c

        return (a + b) / 2

    except:
        print("Fehler")
        return None

#Printer für Eigene Funktion oder Testfälle
def solver():
    print("=== Aufgabe 5 ===")
    print("1 - Eigene Funktion")
    print("2 - Testfälle")

    wahl = input("Auswahl: ")

    if wahl == "1": #Eingabe der Funktion und des Intervalls sowie der gewünschten Genauigkeit
        formel = input("Funktion: ") #Eingabe der Funktion als String
        a = float(input("a: ")) #Eingabe des Intervallanfangs
        b = float(input("b: ")) #Eingabe des Intervallendes
        epsilon = float(input("epsilon: ")) #Eingabe der gewünschten Genauigkeit

        f = funktion_aus_text_erstellen(formel) #Erstellung der Funktion aus dem eingegebenen String
        x = bisektion(f, a, b, epsilon) #Berechnung der Nullstelle mit dem Bisektions-Verfahren

        print("Nullstelle:", x)

    elif wahl == "2": #Testfälle für die Funktion x^2 - n, um die Quadratwurzel von n zu finden
        for n in [25, 81, 144]:
            f = funktion_aus_text_erstellen(f"x**2 - {n}")
            x = bisektion(f, 0, n, 0.00001)

            print("n =", n, "| numerisch:", x, "| exakt:", math.sqrt(n))


if __name__ == "__main__":
    solver()