# SQL Style Guide
- SQL-Schlüsselwörter werden komplett klein geschreiben
- Namen (Tabellen, Spalten, etc.) sind Englisch werden in kleinem Snakecase geschrieben (z. B. `hello_world`).
- Tabellennamen sind Singular (z.B. `room` statt `rooms`). N-N Verbindungstabellen werden `name1_name2` gennant (z. B. `studi_roboter` ;-)) sofern dies konfliktfrei möglich ist.
- Entitätstabellen werden über `id int generated always as identity primary key` identifiziert und referenziert.
- Spalten werden immer `not null` oder `null` markiert. Spalten werden nicht implizit nullable. Spalten die im Primärschlüssel verwendentet werden und damit automatisch `not null` sind werden trotzdem als solches markiert.
- Fremdschlüssel die andere ids referenzieren nennen die referenzierende Spalte wie die Tabelle (z. B. `room int not null references room(id)` nicht `room_id`).
- Constraints werden nicht benannt und wenn möglich inline deklariert (z. B. foreign key direkt hinter referenzierende Spalte).
- Textspalten werden durch den `text`-Datentypen dargestellt (kein `char(n)`, `varchar(n)` oder `varchar`). Sollte Bedarf für eine Längenbegrenzung bestehen wird diese mit einem Check-constraint gelöst.
- Alle SQL-Befehle und Queries müssen sich .sql Dateien befinden (keine String Literals oder anderweitige inline Verwendung)
- SQL-Dateien müssen mit `pg_format` formatiert sein (`format_sql.sh` im Root-Verzeichnis jedes Projekts).
Zu diesem Zweck befindet sich eine `.pg_format`-Datei mit folgendem Inhalt im Projekthauptverzeichnis:
```
keyword-case=1
function-case=1
type-case=1
wrap-limit=80
```

