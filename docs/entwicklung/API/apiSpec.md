# OpenAPI Spec

Für die Dokumentation der API wird die **OpenAPI Spezifikation** (ehem. Swagger)
verwendet: https://www.openapis.org/

OpenAPI beschreibt HTTP-APIs in einem menschen- und maschinenlesbaren Format,
namentlich JSON oder YAML, wobei YAML aufgrund der besseren Lesbarkeit oftmals
bevorzugt wird. Es folgt eine unvollständige Liste an Eigenschaften der API, die
per OpenAPI spezifiziert werden können:

- API-Routen und Endpunkte
  - Methode
  - Div. Beschreibungen und Tags
  - Verschiedene Parametertypen
    - Path, Query, Header, Cookie, ...
  - Request Bodies
    - Zusammensetzbare Schemata mit Datentypen
  - Responses
- Informationen zum Server
- Authentifizierung
- Beispielwerte
- ...

## Dokumentationsworkflow

### OpenAPI Version und Format

Für unsere API Dokumentation wird OpenAPI Version `3.1` (aktuellste Version)
eingesetzt. Als Dateiformat verwenden wir `YAML`, welches hier folgende Vorteile
über `JSON` hat:

- Bessere Lesbarkeit
- Kompakter (keine Klammern, etc.)
- Kommentare sind möglich (mit #)

### Verwendung

#### Anzeigen der API Dokumentation

##### Über interne Dokumentation

Die aktuellste Version der API-Dokumentation wird automatisch (per Jenkins) als
`openapi.yaml` in dieses Repository übernommen und unter
[API-Dokumentation](Api-Dokumentation.md) mit Swagger UI angezeigt.

##### Lokal bauen

1. Repository `planlos-openapi` klonen
2. `npm install`
3. `npm run build` zum Bauen (landet in `dist`)

##### OpenAPI Syntax validieren

Mittels `npm run validate`

#### Ändern der API Dokumentation

1. Repository `planlos-openapi` klonen
2. Änderungen an `openapi.yaml` vornehmen
3. `npm install`
4. Mit `npm run validate` Syntax validieren
5. Optional: Mit `npm run build` bauen und lokal testen
6. Auf `main` pushen (Wird automatisch gebaut)

## OpenAPI Basics

Die vollständige OpenAPI Dokumentation, inklusive Beispiele, ist hier zu finden:
https://swagger.io/specification/

Es folgen einige grundlegende Erklärungen:

### Grundstruktur

Auf höchster Ebene ist die OpenAPI YAML Datei in vier Bereiche aufgeteilt:

- Metadaten
  - Keywords: `openapi`, `info`
- Server
  - Definition von Hosts
  - Keyword: `servers`
- Pfade / Endpunkte
  - Definition von Endpunkten
  - Keyword: `paths`
- Schemas
  - Wiederverwendbare Schemata / eigene Datenstrukturen
  - Keyword: `components`

Ein Minimalbeispiel könnte so aussehen:

```
openapi: 3.1.0
info:
  title: Beispiel API
  version: 1.0.0

servers:
  - url: https://api.example.com

paths:
  /users:
    get:
      summary: Liste aller Nutzer
      responses:
        '200':
          description: OK
```

### Pfade

Jeder API-Endpunkt wird unter `paths` definiert. Für jeden Pfad können alle
unterstützten HTTP Methoden angegeben werden, welche Parameter (und ggf. Request
Body) diese akzeptieren und was mögliche Antworten sind.

Beispiel:

```
paths:
  /users/{userid}:
    get:
      summary: Hole einen Nutzer
      parameters:
        - name: userid
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Nutzer erfolgreich abgerufen
```

### Spezifizierung vom HTTP Body

Der Inhalt vom HTTP Body kann ebenfalls genau spezifiziert werden. Dazu werden
Schemata eingesetzt, welche entweder direkt angegeben oder wiederverwendbar
unter `components` gespeichert werden:

Beispiel für spezifizierten Request Body:

```
...
post:
    requestBody:
            required: true
            content:
                application/json:
                    schema:
                        # Verweis auf Schema in components
                        $ref: "#/components/schemas/PutMatchRequest"
...
```

Beispiel für spezifizierte Antwort:

```
...
responses:
  '200':
    description: OK
    content:
      application/json:
        schema:
            type: string
            format: uuid
...
```

### Schemata

Unter `components` lassen sich wiederverwendbare Schemata für JSON Objekte
anlegen, welche zum beispiel Parameter oder den HTTP Body spezifizieren:

Beispiel:

```
components:
  schemas:
    User:
      # Object -> JSON Objekt
      type: object
      required: [id, name]
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
```

Als Datentyp unter type werden die normalen JSON Datentypen verwendet. Mit
`format` können einige dieser Datentypen weiter eingeschränkt werden, zum
Beispiel: `format: uuid` bei `type: string`.

Diese Schemata lassen sich folgendermaßen referenzieren:

```
schema:
    $ref: "#/components/schemas/User"
```
