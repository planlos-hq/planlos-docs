# Zensical

## Was ist Zensical?

[Zensical](https://zensical.org) ist ein Static Site Generator, der aus Markdown-Dateien eine Dokumentationswebseite erzeugt. Er stammt von den Machern von Material for MkDocs und ersetzt MkDocs, das nicht mehr gepflegt wird. Konfiguriert wird über die Datei `zensical.toml`.

## Erste Schritte

Repository klonen und in das Verzeichnis wechseln:

```bash
git clone <repo-url>
cd planlos-docs
```

Mit Nix reicht `direnv allow` (bzw. `nix develop`), sonst:

```bash
pip install zensical
```

## Neue Dokumentation erstellen

### 1. Neue Markdown-Datei anlegen

Nutzerdokumentation gehört nach `docs/benutzerhandbuch/`, Entwicklerdokumentation nach `docs/entwicklung/`:

```
docs/
  ├── index.md
  ├── benutzerhandbuch/
  └── entwicklung/
        └── NeueSeite.md  ← Deine neue Datei
```

### 2. Navigation

Die Navigation wird automatisch aus der Ordnerstruktur erzeugt, ein Eintrag in `zensical.toml` ist nicht nötig:

- **Reihenfolge:** alphabetisch nach Datei- bzw. Ordnernamen, Dateien vor Ordnern. Eine `index.md` steht immer zuerst und ist die Startseite des Ordners.
- **Seitentitel im Menü:** die erste `#`-Überschrift der Seite, daher kurz halten.
- **Abschnittstitel:** der Ordnername.

### 3. Inhalte schreiben

Schreibe deine Dokumentation mit [Markdown-Syntax](https://www.markdownguide.org/basic-syntax/):

```markdown
# Überschrift

Dies ist ein Absatz mit **fettem Text** und _kursivem Text_.

## Unterüberschrift

- Liste mit Punkten
- Noch ein Punkt

![Bildbeschreibung](assets/bild.png)
```

Bilder liegen im `assets/`-Ordner des jeweiligen Bereichs.

### 4. Änderungen hochladen

```bash
git add .
git commit -m "Dokumentation hinzugefügt"
git push
```

Die Webseite wird automatisch durch Jenkins neu gebaut und deployed.

## Wichtige Befehle

| Befehl            | Beschreibung                                       |
| ----------------- | -------------------------------------------------- |
| `zensical serve`  | Startet lokalen Entwicklungsserver mit Live-Reload |
| `zensical build`  | Baut die statische Webseite im `site/`-Ordner      |
| `zensical --help` | Zeigt Hilfe mit allen Befehlen                     |

Nach `zensical serve` ist die Vorschau unter `http://127.0.0.1:8000` erreichbar.

## Docker

```bash
# Bauen und starten (http://127.0.0.1:8001)
docker compose up -d --build

# Stoppen und entfernen
docker compose down
```

## Einstellungen

Alle Einstellungen stehen in `settings.yml` im Projektverzeichnis.

### Abschnitte ein-/ausblenden

```yaml
abschnitte:
  benutzerhandbuch: true
  entwicklung: false   # Entwicklerdoku wird nicht gebaut
```

Ausgeschaltete Abschnitte fehlen komplett in der gebauten Seite (nicht nur im
Menü), ebenso ihre Verweise auf der Startseite. Das übernimmt `build.py`, das
auch der Docker-Build verwendet:

```bash
python build.py
```

`zensical serve` zeigt zum Schreiben immer alle Abschnitte. Der Build läuft
mit `--strict`: Verlinkt eine Seite in einen abgeschalteten Abschnitt, schlägt
er fehl. Abschnittsübergreifende Links daher vermeiden.

### Impressum

Die Angaben im [Impressum](../../rechtliches/Impressum.md) (Anschrift, Kontakt,
Verantwortliche usw.) stehen unter `impressum:`. Ein leerer Wert (`""`) blendet
die Zeile bzw. den ganzen Abschnitt aus.

Die Werte werden über die Jinja-Variablen der Zensical-Erweiterung `macros`
eingesetzt. Diese ist nur auf Seiten mit `render_macros: true` im Kopfbereich
aktiv, damit `{{ ... }}` in Codebeispielen (z. B. Vue-Templates) unverändert
bleibt.

## Keine sensiblen Daten

Die Dokumentation darf **keine** Passwörter, Schlüssel, echten Namen, Benutzernamen, Hostnamen oder Serverkonfigurationen enthalten. Auch Screenshots vor dem Einchecken auf echte Namen prüfen und ggf. durch Platzhalter (z. B. „Max Mustermann") ersetzen.

## Tipps

- Nutze aussagekräftige Dateinamen (z. B. `Installation.md` statt `seite1.md`)
- Benenne Dateien im CamelCase-Format
- Strukturiere längere Texte mit Überschriften
- Teste deine Änderungen lokal mit `zensical serve` vor dem Push

## Weitere Ressourcen

- **Zensical Dokumentation:** [zensical.org/docs](https://zensical.org/docs/)
- **Markdown-Guide:** [markdownguide.org](https://www.markdownguide.org)
