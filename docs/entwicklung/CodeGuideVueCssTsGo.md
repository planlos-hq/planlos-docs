# Code Guide

## Übersicht

Dieser Code Guide legt die Regeln für Struktur, Stil und Qualität im Projekt fest.  
Er gilt für alle Komponenten in **Vue 3 (TypeScript, CSS)** und für den **Go-Backend-Teil**.  
Ziel: **einheitlicher, lesbarer und wartbarer Code**.

---

## 1. Allgemeine Prinzipien

- Schreibe **klaren, gut lesbaren Code** – Verständlichkeit über Kürze.
- **Konsistenz** ist wichtiger als persönliche Vorlieben.
- **Keine Logik duplizieren** – Wiederverwendung bevorzugen.
- Verwende **Linter** und **Autoformatter**, um konsistente Codequalität sicherzustellen.
- Verwendung der **englischen Sprache** in der Namensgebung.
- Verwende selbsterklärende Namen und vermeide kurze Bezeichner.
- "Magic Numbers" sollen vermieden werden und als Konstanten verwendet werden.
- Kommentare sollen immer einen Mehrwert bieten.
- Funktionen sollen nicht zu komplex und lang implementiert werden.
- Vermeidung von stark verschachteltem Code.
- Angezeigte Fehler müssen immer behoben werden.
- Warnungen sollten immer behoben werden, außer die Lesbarkeit des Codes wird schlechter.

---

## 2. Verwendung von Linter und Autoformatter

### Vue und TypeScript

- Nach `git clone` im Verzeichnis `npm install` ausführen, damit alle Dependencies in identischer Version vorliegen.
- Alles, was vom Autoformatter behoben wird, wird nicht als Fehler markiert.
- Linter: ESLint in Kombination mit Stylelint.
- Autoformatter: Prettier.
- TSDoc wird für Kommentare verwendet (siehe `https://tsdoc.org/`).
- Kommentare werden bei nicht selbsterklärenden oder komplexen Code-Abschnitten geschrieben.

**Dateien mit Regeln**

- `package.json/eslint.config.ts`
- `package.json/.prettierrc.json`
- `stylelint.config.mjs`

**Standardbefehle**

```bash
npm run lint
```

- prüft Vue-, TypeScript- und CSS-Dateien (kann mit VS Code Extensions direkt sichtbar gemacht werden).

```bash
npm run format
```

- formatiert den Code mit Prettier (wird bei Speichern der Datei ausgeführt).

**Empfohlene VS Code Extensions**

- ESLint
- Prettier – Code Formatter
- Stylelint

### Go

- Linter: **golangci-lint** (bündelt viele Linter).
- Autoformatter: **gofmt, goimports und golines**.
- Installation:

```bash
go install github.com/golangci/golangci-lint/v2/cmd/golangci-lint@v2.5.0
```

- (Installation von Go: `https://go.dev/doc/install`).

**Dateien mit Regeln**

- `.golangci.yml`

**Standardbefehle**

Zum Ausführen der Linter.
```bash
golangci-lint run
```

Zum Ausführen der Autoformatter.
```bash
golangci-lint fmt
```

Zum Ausführen der Linter und Autoformatter, sowie automatischer Änderungen durch [auto-fix]-Linter.
```bash
golangci-lint run --fix
```

---

## 4. Spezifikationen für Vue mit Typescript

- Semikolon ist Pflicht.
- Doppelte Anführungszeichen `"`.
- Strikter Vergleich mit `===` statt `==`.
- Kein `console.log()` mit sensiblen Daten.
- Verwendung von Vue 3 (Composition API)
- Maximal ein Prop pro Zeile.
- Props müssen Typen haben.
- Bevorzuge bei leeren Komponenten self-closing: `<user prop=prop/>` statt `<user prop=prop/></user>`.
- Bei `v-for` immer einen Key verwenden.
- Verwendung von `defineEmits` und `defineProps`.
- Keine ungenutzten Variablen, Funktionen oder Komponenten im Code behalten.
- Empfehlung für Reihenfolge in `.vue`-Dateien: `template`, `script`, `style`.
- Wenn Direktiven existieren, sollen sie verwendet werden.
- Nutzung von `<script setup lang="ts">`.
- Einheitliche Formatierung durch Autoformatter (Einrückungen, Klammern etc.).

### weitere TypeScript-Regeln

- `boolean` darf nicht `null` oder `undefined` sein.
- Keine Verwendung von `any`.
- Einheitliche Typdefinition mit `type` und ohne `interface`.

### Namensgebung in Vue und TypeScript

| Element                                 | Stil             | Beispiel                                 |
| --------------------------------------- | ---------------- | ---------------------------------------- |
| **Komponenten- und Dateiname**          | PascalCase       | `UserProfile`, `LoginForm`               |
| **Komponentennamen (im Script)**        | PascalCase       | `UserProfile.vue`, `LoginForm.vue`       |
| **Komponentennamen (im Template)**      | kebab-case       | `<user-profile/>`, `<login-form.vue/>`   |
| **Funktionen / Methoden**               | camelCase        | `fetchUserData()`, `handleSubmit()`      |
| **Variablen**                           | camelCase        | `userName`, `isActive`                   |
| **Props (im Script)**                   | camelCase        | `userId`, `isVisible`                    |
| **Props (im Template)**                 | kebab-case       | `user-id`, `is-visible`                  |
| **Konstanten**                          | camelCase        | `userName`, `isActive`                   |
| **CSS-Klassen und CSS-IDs im Template** | kebab-case       | `user-card`, `user-card-header`          |
| **Enums / Interfaces / Typen**          | PascalCase       | `UserRole`, `UserProfile`, `ApiResponse` |

### Regeln

- Komponentenname muss **aus mehreren Wörtern** bestehen (z. B. `UserCard`, nicht `Card`).
- **Komponentenname = Dateiname**.
- Verwende **eindeutige und beschreibende Namen** – vermeide Abkürzungen.
- Verwende **Verb + Objekt** für Funktionen (z. B. `loadUser()`, `updateProfile()`).

### Lint-Meldungen ausschalten
- Sollte nur bei falsch-positiven Meldungen eingesetzt werden.

HTML:
`<!-- eslint-disable-next-line rule-name-from-eslint-config -->`
oder
```html
<!-- eslint-disable rule-name-from-eslint-config -->
        <div>content</div>
<!-- eslint-enable rule-name-from-eslint-config -->
```

TS:
`/* eslint-disable-next-line rule-name-from-eslint-config */`
oder
```TS
/* eslint-disable rule-name-from-eslint-config */
        //falsch-positiver Code
/* eslint-enable rule-name-from-eslint-config */
```

CSS:
`/* stylelint-disable-next-line rule-name-from-stylelint-config */`
oder
```CSS
/* stylelint-disable rule-name-from-stylelint-config */
        /*falsch-positiver Code*/
/* stylelint-enable rule-name-from-stylelint-config */
```
---

## 5. Spezifikationen für CSS

- Doppelte Anführungszeichen `"`.
- Duplikate vermeiden.
- Leere Blöcke vermeiden.
- Farbvariablen werden in `main.css` definiert.
- Möglichst nur Farben aus der `main.css` werden verwendet.
- So oft wie möglich `<style scoped>` nutzen.
- 0-Werte: ohne Einheit (`margin: 0;`).
- Einheitliche Formatierung durch Autoformatter(Einrückung, Klammern, Leerzeichen).
- Bilder und Icons nur über `assets` einbinden.
- Verwendung von relativen Einheiten z.B. `%`, `vh`, `vw` statt `px`.
- Maximale Verschachtelung: 3.

### Namensgebung in CSS

| Element          | Stil                  | Beispiel                          |
| ---------------- | --------------------- | --------------------------------- |
| **Klassennamen** | kebab-case            | `.my-button`, `.user-card`        |
| **Variablen**    | kebab-case mit Präfix | `--primary-color`, `--text-light` |
| **IDs**          | kebab-case            | `#main-header`, `#my-button`      |

- Verwende **eindeutige und beschreibende Namen** – vermeide Abkürzungen.

---

## 6. Dokumentation in Vue

Grundlegend erfolgt die Dokumentation auf deutsch.

### Inline

#### Html-Template

- Inline-Kommentare im Template sollten sparsam, aber gezielt eingesetzt werden.
  Sie sind sinnvoll, wenn sie die Verständlichkeit erhöhen oder besondere Entscheidungen erklären.
- Kommentare schreiben bei:
    - verschachteltem Layout
    - komplexer Kombination von Direktiven
    - ungewöhnlichen Entscheidungen

Gutes Beispiel:
```html
<template>
  <ul class="notifications">
    <!--
      Es werden nur die letzten 5 Nachrichten angezeigt. Für alle Nachrichten siehe allNotifications.
    -->
    <li v-for="note in recentNotifications" :key="note.id">
      {{ note.message }}
    </li>
  </ul>
</template>
``` 
Schlechtes Beispiel:
```html
<template>
  <!-- Schleife -->
  <div v-for="item in items" :key="item.id">
    <!-- Anzeige des Namens -->
    <p>{{ item.name }}</p>
  </div>
</template>
```
#### Script
- Inline-Kommentare im Script-Teil werden im TSDoc-Stil verfasst. Mehr Informationen dazu findet man unter https://tsdoc.org/.
- Kommentare bei exportierten Komponenten sind Pflicht. Dazu zählen unter anderem:
    - props
    - emits
    - exportierte Funktionen
    - exportierte Variablen
- Zusätzlich wird auch jede interne Funktion dokumentiert.
- Für Variablen ist kein Kommentar notwendig. Außnahme:
     - Für Variablen ist ein Kommentar Pflicht, falls sich diese aus z.B. `computed` berechnen lässt.

wichtige Tags:
```TS
/**
 * @remarks - für längere Erklärungen
 * @param - Parameter 1 
 * @param - Parameter 2  
 * @returns - Rückgabewert
 */
```

    

Beispiel für props:

```TS
const props = defineProps<{
  /** Text innerhalb des Buttons */
  title: string;

  /** Farbe des Buttons */
  color?: string;
}>();
```

Beispiel für emits:

```TS
const emit = defineEmits<{
  /** Wird bei Klicken des Senden-Buttons ausgelöst */
  clicked: [MouseEvent];
}>();
```

Beispiel für Funktionen:

```TS
 /**
   * Sucht eine Farbe anhand ihrer ID
   *
   * @param id - Die eindeutige ID der Farbe
   * @returns Die gefundene Farbe oder undefined, falls nicht vorhanden
   */
  function readColor(id: number): Color | undefined {
    return colorList.value.find(color => color.id === id);
  }
```

#### CSS
Kommentare im Style-Teil sind bei regulärem Einsatz keine Pflicht, da die Bedeutung aus dem Code klar wird. Überall wo nicht direkt ersichtlich ist, was bestimmter Code macht, sollte ein Kommentar mit kurzer Beschreibung erstellt werden. Beispielhaft ist hier der Umgang mit externen Bibliotheken, z.B. VueCal, zu nennen. 

Beispiel:
```css
  /* to change cell color without affecting the horizontal lines of the time grip  */
  :deep(.vuecal__cell::before) {
    background-color: #ffffff;
    border-left: 1px solid black !important;
  }
```

### Ordnerstruktur

```plaintext
src/
├───assets              # statistische Dateien, z.B. CSS, Bilder, ...
├───components          # wiederverwendbare Komponenten
│   ├───IconButtons     # Buttons, die mit Template IconButton erstellt wurden
│   └───SideBars        # Seitenleisten des BaseLayouts
├───dummyData           # Testdaten
├───enums               # feste Werte, z.B. Studiengangskürzel
├───models              # Wiederverwendbare TypeScript-Typen
├───router              # Navigation mit vue-router
├───stores              # Pinia Stores, Datenverwaltung
├───template            # Komponenten, die als Vorlage dienen
├───types               # Types von Bibliotheken, damit TS keinen Fehler anzeigt (bisher nur VueCal)
└───views               # Ansichten der Anwendungen
```

---

## 7. Spezifikationen für Go

- Alle verwendeten Linter von `golangci-lint` lassen sich mit einer Kurzbeschreibung in `.golangci.yml` finden.

- Es dürfen nur ACII-Zeichen im Code verwendet werden.
- Alle öffentlichen Typen, Variablen und Funktionen müssen eine Kommentar aufweisen.
- Globale Variablen sollen möglichst vermieden werden.
- Entweder wird ein gültiger Fehler und ein ungültiger/nil-Wert, oder ein nil-Fehler und ein gültiger Wert zurückgegeben. Die gleichzeitige Rückgabe von nil für Fehler und einem ungültigen Wert ist zu vermeiden.
- Zurückgegebene Fehler müssen immer behandelt werden.
- Fehler von externen Funktionen müssen immer mit Kontext verpackt werden, damit die Herkunft des Problems klar bleibt. (Nutzung von `%w`).
- Für Tests muss das separate Testpaket-Format `package paketname_test` verwendet werden. 
- Tests sollten die Möglichkeit parallel zu laufen ausnutzen.
- Kein `SELECT *` in SQL-Anfragen aus Performance-Gründen. 
- Keine Init-Funktionen, um Seiteeffekte zu vermeiden.
- Funktionen, die Ähnlichkeit mit `printf` haben, sollen mit einem `f` am Ende benannt werden.

### Lint-Meldungen ausschalten

- Mit `//nolint:all` lassen sich alle Lint-Meldungen für einen spezifischen Codebereich, z.B. für eine Funktion, oder in der gleichen Zeile Inline deaktivieren.
- Mit `//nolint:lintername` lassen sich spezifische Lint-Meldungen deaktivieren.
- Die Deaktivierung von Lint-Meldungen sollte nur bei falsch-positiven Ergebnissen verwendet werden. 
- Wenn eine Meldung deaktiviert wird, muss dies immer begründet werden. `//nolint:all // This is is the reason ...` 


### Namensgebung in Go

| Element                                  | Stil             | Beispiel                            |
| ---------------------------------------- | ---------------- | ----------------------------------- |
| Paketname                                | klein            | `user`, `database`                  |
| Variablen                                | camelCase        | `userName`, `isActive`              |
| Konstanten                               | UPPER_SNAKE_CASE | `MAX_RETRIES`, `DEFAULT_TIMEOUT`    |
| Funktionen / Methoden (exportiert)       | PascalCase       | `AddUser()`, `GetProfile()`         |
| Funktionen / Methoden (nicht exportiert) | camelCase        | `calculateSum()`, `handleRequest()` |
| Structs & Interfaces                     | PascalCase       | `UserProfile`, `UserService`        |
| Exportierte Felder                       | PascalCase       | `UserName`, `Email`                 |
| Private Felder                           | camelCase        | `userName`, `email`                 |

---