# Go Tests

Diese Dokumentation beschreibt das Vorgehen zum Ausführen der Integrationstests für die Stundenplan-API.

## Voraussetzungen

Die Tests erfordern eine aktive PostgreSQL-Datenbank. Diese wird über Docker im entsprechenden Repository verwaltet.

### Datenbank starten
Stellen Sie sicher, dass die Datenbank-Container laufen:

```bash
cd ~/planlos-db
docker compose up -d
```

## Ausführung der Tests

Die Tests nutzen die Umgebungsvariable `DATABASE_URL`, um sich mit der laufenden Datenbank zu verbinden.

### Alle Tests im Projekt ausführen
Wechseln Sie in das Verzeichnis `planlos-server` und führen Sie folgenden Befehl aus:

```bash
DATABASE_URL="postgres://stundenplan:<db-passwort>@localhost:8003/stundenplan?sslmode=disable" go test ./apiserver -v
```

### Einzelne Test-Suiten ausführen (z.B. Rooms)
Um nur die Tests für die Raum-Verwaltung mit detaillierter Ausgabe anzuzeigen:

```bash
DATABASE_URL="postgres://stundenplan:<db-passwort>@localhost:8003/stundenplan?sslmode=disable" go test -v ./apiserver -v -run TestRoomEndpoints
```

## Funktionsweise der Tests

1. **Datenbank-Cleanup**: Die Tests führen vor jedem Durchlauf ein `TRUNCATE` auf alle relevanten Tabellen aus, um Seiteneffekte zwischen Testläufen zu vermeiden.
2. **Authentifizierung**: Der Test-Server wird standardmäßig mit deaktivierter Authentifizierung gestartet (`noAuth=true`), um die Geschäftslogik der Endpunkte isoliert prüfen zu können.
3. **Integration**: Es werden echte HTTP-Anfragen gegen einen `httptest.Server` gesendet, um das Zusammenspiel von Routing, Handlern und Datenbank zu validieren.

## Fehlerbehebung

*   **Verbindungsfehler**: Prüfen Sie mit `docker ps`, ob der Container `stundenplan_pg` den Status "healthy" hat und der Port `8003` korrekt gemappt ist.
*   **Schema-Konflikte**: Falls die Tabellenstruktur nicht mit dem Code übereinstimmt, stellen Sie sicher, dass die Migrationen im `planlos-db` Repository aktuell sind.
