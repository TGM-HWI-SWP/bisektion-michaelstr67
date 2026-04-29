import matplotlib.pyplot as plt
from Aufgabe5 import funktion_aus_text_erstellen

#Bisektions-Verfahren mit Grafik
def bisektion_grafik(f, a, b, epsilon)-> float:
    """f: Funktion, deren Nullstelle gefunden werden soll
    a: Anfang des Intervalls
    b: Ende des Intervalls
    epsilon: gewünschte Genauigkeit
    Rückgabe: Nullstelle von f im Intervall [a, b] oder None, wenn kein Vorzeichenwechsel vorliegt
    """
    if f(a) * f(b) >= 0: # Kein Vorzeichenwechsel
        print("Kein Vorzeichenwechsel.")
        return None

    loesungen = [] #Liste zur Speicherung der Lösungen für die Grafik
    genauigkeiten = [] #Liste zur Speicherung der Genauigkeiten für die Grafik
    iterationen = [] #Liste zur Speicherung der Iterationen für die Grafik

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1) #Erstellung von drei Subplots für die Funktion, die Genauigkeit und die Lösungen

    iteration = 0 # Zähler für die Iterationen

    while (b - a) / 2 > epsilon: # Solange die Genauigkeit nicht erreicht ist
        c = (a + b) / 2 # Mitte des Intervalls

        iteration += 1
        iterationen.append(iteration)
        loesungen.append(c)
        genauigkeiten.append(abs(f(c)))

        x = [] #Liste zur Speicherung der x-Werte für die Grafik
        y = [] #Liste zur Speicherung der y-Werte für die Grafik

        i = a - 2 # Startpunkt für die x-Werte, etwas kleiner als a, um die Funktion vor dem Intervall zu zeigen
        while i <= b + 2: # Endpunkt für die x-Werte, etwas größer als b, um die Funktion nach dem Intervall zu zeigen
            x.append(i) #Hinzufügen des aktuellen x-Werts zur Liste
            y.append(f(i)) #Hinzufügen des Funktionswerts für den aktuellen x-Wert zur Liste
            i += 0.1

        ax1.clear() #Clearing der Subplots, um die neuen Werte zu plotten
        ax2.clear() #Clearing der Subplots, um die neuen Werte zu plotten
        ax3.clear() #Clearing der Subplots, um die neuen Werte zu plotten

        ax1.plot(x, y) #Grafik der Funktion f(x) über das Intervall [a-2, b+2]
        ax1.axhline(0) #Horizontale Linie bei y=0, um die Nullstelle besser sichtbar zu machen
        ax1.axvline(c) #Vertikale Linie bei x=c, um die aktuelle Näherung besser sichtbar zu machen
        ax1.set_title("Bisektion") #Titel für die Funktionengrafik

        ax2.plot(iterationen, genauigkeiten) #Grafik der Genauigkeit über die Iterationen
        ax2.set_title("Aktuelle Genauigkeit |f(c)|") #Titel für die Genauigkeitsgrafik

        ax3.plot(iterationen, loesungen) #Grafik der Lösungen über die Iterationen
        ax3.set_title("Aktuelle Lösung c") #Titel für die Lösungsgrafik

        plt.tight_layout() #Anpassung des Layouts, damit die Subplots nicht überlappen
        plt.pause(0.5) #Pause, um die Grafik zu aktualisieren und die Iterationen sichtbar zu machen

        if f(a) * f(c) < 0: # Vorzeichenwechsel zwischen a und c
            b = c
        else:
            a = c

    plt.show() 
    return (a + b) / 2 # Rückgabe der gefundenen Nullstelle

# Printer für die Aufgabe 7
def plotter():
    print("=== Aufgabe 7 ===")

    f = funktion_aus_text_erstellen("x**2 - 25")
    x = bisektion_grafik(f, 0, 25, 0.00001)

    print("Nullstelle:", x)


if __name__ == "__main__":
    plotter()