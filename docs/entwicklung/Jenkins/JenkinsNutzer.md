# Nutzersicht

Jenkins ist unser CI/CD System.

- Es baut automatisiert unsere Projekte (deckt dabei eventuelle Compiler-Fehler auf)
- Kompiliert und führt unsere Testsuites aus (deckt dabei eventuelle Logic-Fehler auf)
- Deployt unsere Projekte automatisch (durch push auf den `main` oder `release` branch)

Ausgelöst werden diese Mechanismen automatisch durch push neuer Commits auf entsprechende Branches der GitHub Repositories.

In der GitHub-UI könnt ihr den Status eures Commits rechts neben der Commit-Zeit sehen:

- Orangener Kreis bedeutet Prozess noch im Gang
- Rotes Kreuz bedeutet Fehler
- Grüner Haken bedeutet alles in Ordnung

Details lassen sich durch Klicken auf diese Zeichen und anschließendes Klicken auf "Details" betrachten.

Mit "View more details on ..." könnt ihr auf den Jenkins-Server wechseln und euch die Logs im Detail anzeigen lassen.
