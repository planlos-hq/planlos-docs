# Lokales Setup

Anlegen des Doker Netzwerks mit `docker network create stundenplan` Pullen aller
applikationsrelevanten Repositories mit `git pull --recurse-submodules`

## Anlegen der Env-Dateien

In den Repos eine Datei mit dem Namen `.env` anlegen und mit den benötigten
Variablen befüllen. Diese werden dank `.gitignore` nicht committed.

**1. planlos-db**

```
STUNDENPLAN_PG_PASSWD=<db-passwort>
```

**2. planlos-server**

```
STUNDENPLAN_PG_PASSWD=<db-passwort>
NO_AUTH=true
```

`STUNDENPLAN_PG_PASSWD` legt dabei das Datenbankpasswort fest und muss in beiden
Repos identisch sein. `NO_AUTH` legt fest, ob die API-Sperre für Unbefugte
temporär aufgehoben werden soll.

**3. planlos-web**

```
VITE_API_BASE_URL=/stundenplan/backend/api/v1
VITE_SHIB_USERNAME=uXXXXX
```

`VITE_API_BASE_URL` legt die Basis-URL fest, über die das Frontend die API des Backends anspricht.
`VITE_SHIB_USERNAME` legt den Shibboleth-Benutzernamen (U-Nummer) fest, der für die Authentifizierung benötigt wird.

## Starten der Docker-Compose-Container

Mit `docker compose up` in folgender Reihenfolge starten:

1. planlos-db
2. planlos-server

## Starten des Frontends

Die Dependencies im `planlos-web` mit `npm install` installieren und anschließend den Dev-Server mit `npm run dev` starten.
Der Dev-Server läuft anschließend auf dem Port 8005. In diesem Fall muss der `planlos-web` Docker-Container **nicht** gestartet werden.
