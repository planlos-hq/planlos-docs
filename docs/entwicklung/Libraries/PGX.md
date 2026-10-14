# PGX
Für das Go-Backend wird der PGX PostgreSQL Treiber und Verbindungspool eingesetzt:
https://github.com/jackc/pgx
PGX kann einerseits über die eigenen Datenstrukturen verwendet werden, oder als Adapter für die Standardbibliothek eingesetzt werden. Aktuell werden die PGX Datenstrukturen verwendet.

## Vorteile
- Signifikant schneller
    - Keine abstrakte Zwischenrepräsentation, direkte Nutzung des PSQL Protokolls
- Support für alle Postgres Features
- Besseres Go <-> Postgres Mapping
- Gute Tracing / Logging Unterstützung
- Syntax größtenteils gleich / ähnlich zur Standardbibliothek

## Verwendung (Limitiert auf relevante Funktionalitäten)

### Erstellung eines Kontexts
In PGX werden im Vergleich zur Standardbibliothek verstärkt Kontexte eingesetzt. Diese definieren Laufzeitgrenzen, wie Timeouts oder Deadlines, und sorgen dafür, dass Operationen bei Verletzungen abgebrochen werden.

Leerer / default Kontext:
```
ctx := context.Background()
```

Mit Timeout:
```
ctx, cancel := context.WithTimeout(r.Context(), timeout)
```

`cancel()` bricht hierbei den Kontext ab, auch wenn der Timeout noch nicht abgelaufen ist. Typischerweise wird `cancel()` am Ende der Funktion aufgerufen: `defer cancel()`


### Erstellung Datenbankpool
Die Erstellung eines DB Pools erfolgt mittels PGX Typen `pgxpool`.

Komplett neuer Pool:
```
dbpool, err := pgxpool.New(ctx, dbURL)
```

Alternativ kann auch ein Pool aus einer Config erstellt werden. Somit können Parameter, wie zum Beispiel die maximale Verbindungsanzahl auch über die URL vergeben werden:
```
cfg, err := pgxpool.ParseConfig(dbURL)
...
// Optionale Anpassung weiterer Parameter
cfg.MinConns = 2
cfg.MaxConns = 20
...
dbpool, err := pgxpool.NewWithConfig(ctx, cfg)
...
defer dbpool.Close()
```

### Durchführung von Anfragen
Die Durchführung von Anfragen funktioniert quasi identisch zur Standardbibliothek, mit der Änderung, das immer ein Kontext übergeben werden muss. Die Parameterbenennung erfolgt Postgres-typisch nummeriert über `$1`, `$2`, ...

Allgemeine Benutzung mit Prepared Parametern und max. 1 Row Rückgabe:
```
type Example struct {
    a string
    b string
    c int
}

row := dbpool.QueryRow(
    ctx,
    "SELECT a, b, c from abc where d = $1 and e = $2"
    paramFuerD, paramFuerE
    )

// Ergebnis zum Beispiel direkt in struct Example mappen
var ex Example
// Wichtig: Bei QueryRow werden erst hier Fehler zurückgegeben
err := row.Scan(&ex.a, &ex.b, &ex.c)
```

Bei mehr als einer Row Rückgabe wird `Query` verwendet, welches `Rows` zurückgibt, durch welche mit `Next()` iteriert werden kann:
```
rows, err := dbpool.Query(ctx, query)
defer rows.Close()
for rows.Next() {
    err := rows.Scan(...)
    ...
}
```

Erwartet man keine Rückgabe kann `Exec` verwendet werden, welches nur einen `CommandTag`, aus welchem man beispielsweise auslesen kann, wie viele Zeilen betroffen sind, und einen Fehler zurückgibt.

## In unserem Projekt
Im Backend des Stundenplanes wird ein `pgxpool.Pool` bei Programmstart aus einer Konfiguration erstellt und in das State Objekt basierend auf dem Server struct gespeichert. Da alle Handler auf dem Server struct definiert werden, hat man stets Zugriff auf den Datenbankpool.