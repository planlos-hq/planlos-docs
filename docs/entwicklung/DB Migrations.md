# DB Migrationen

Um Änderungen am Datenbankschema vorzunehmen werden Datenbankmigrationen verwendet.

Im planlos-db Repository liegen unter migrations/ durchnummerierte Ordner, die die Migrationen enthalten.

## Migration

Jede Migration bezieht sich auf eine Schemaversion und enthält zwei Dateien:

- `schema.sql`: Enthält das komplette Schema der Tabelle, um eine Datenbank auf diese Schemaversion zu initialisieren. Es handelt sich um eine Kopie der vorherigen `schema.sql`, die die veränderten `create`-Statements enthält. Außerdem enthält sie ein Insert, das diese Schemaversion in die `schema_version_history` einträgt.
- `up.sql`: Enthält die SQL-Statements, die nötig sind um die vorherige Schemaversion auf diese Schemaversion zu upgraden. Außerdem ein insert, das diese Schemaversion in die `schema_version_history` einträgt.

## planlos-db `Dockerfile`

Wenn eine neue Schemaversion erstellt wird, muss der COPY-Befehl aktualisiert, damit die aktuellste `schema.sql` Datei zum initialisieren neuer Datenbanken verwendet wird.

```Dockerfile
COPY migrations/001/schema.sql /docker-entrypoint-initdb.d/01_schema.sql
```

muss also zu

```Dockerfile
COPY migrations/002/schema.sql /docker-entrypoint-initdb.d/01_schema.sql
```

verändert werden.

# Funktionsweise

Das Backend ist verantwotlich, beim Start die aktuelle Schemaversion auszulesen und alle `up.sql` Dateien in einer Transaktion auszuführen, um die aktuelle Schemaversion auf die neueste Schemaversion zu upgraden.

Hierfür enthält das `planlos-server`-Repository das `planlos-db`-Repository als Git-Submodule, um den `migrations`-Ordner als `embed.FS` einzubinden.
