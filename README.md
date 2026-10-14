# Stundenplan Docs

Nutzer- und Entwicklerdokumentation des Stundenplan-Assistenzsystems (PlanLos),
gebaut mit [Zensical](https://zensical.org).

- `docs/benutzerhandbuch/`: Benutzerhandbuch
- `docs/entwicklung/`: Entwicklerdokumentation

```bash
zensical serve   # lokale Vorschau auf http://127.0.0.1:8000
zensical build   # baut nach site/
```

Mit Nix: `direnv allow` bzw. `nix develop`.

**Keine Passwörter, Schlüssel, echten Namen, Benutzernamen, Hostnamen oder
Serverkonfigurationen committen.**

## Docker

```bash
docker compose up -d --build   # http://127.0.0.1:8001
```

## Einstellungen

Alles in [`settings.yml`](settings.yml):

- **`abschnitte`:** Benutzerhandbuch bzw. Entwicklung mit `false` komplett
  aus dem Build nehmen.
- **`impressum`:** Angaben für das Impressum. Leere Werte (`""`) blenden die
  Zeile bzw. den Abschnitt aus.

`python build.py` baut nach `site/` und berücksichtigt die Abschnitte
(der Docker-Build nutzt das ebenfalls). `zensical serve` zeigt immer alles.
