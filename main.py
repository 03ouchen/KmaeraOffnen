import cv2

# Kamera öffnen (die Standardkamera verwenden, normalerweise 0)
cap = cv2.VideoCapture(0)

# Überprüfen, ob die Kamera erfolgreich geöffnet wurde
if not cap.isOpened():
    print("Fehler beim Öffnen der Kamera.")
    exit()

# Schleife zum Lesen und Anzeigen des Video-Streams
while True:
    # Einzelbild von der Kamera lesen
    ret, frame = cap.read()

    # Überprüfen, ob das Bild erfolgreich gelesen wurde
    if not ret:
        print("Fehler beim Lesen des Bildes.")
        break

    # Das Bild anzeigen
    cv2.imshow('Kamera', frame)

    # Warte auf eine Taste zum Beenden (hier 'q' für Quit)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera freigeben und alle Fenster schließen
cap.release()
cv2.destroyAllWindows()
