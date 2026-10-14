# Vitest

Vitest wird als zentrales Testing Framework im Frontend verwendet, um die Funktionalität und Zuverlässigkeit der Software testen zu können. Aufgrund der nahtlosen Integration in Vite, bietet Vitest sich für dieses Projekt an.

Im folgenden wird auf die Einrichtung und Nutzung von Vitest eingegangen. Weitere Informationen sind in der offiziellen Dokumentation auffindbar https://vitest.dev/guide/ .

## Setup

### Einbindung ins Projekt

Installation von Vitest:

```
npm install -D vitest
```

Anschließend muss im package.json noch der Script-Teil erweitert werden:

```JSON
"scripts": {
    "test": "vitest"
  }
```

Da das Projekt Vite verwendet muss für Vitest keine extra Config Datei angelegt werden, sondern kann innerhalb der Vite Config Datei verwendet werden.

```TypeScript
/// <reference types="vitest/config" />
import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
  test: {
    includeSource: ['src/**/*.{js,ts}'],
  },
  define:{
    'import.meta.vitest': 'undefined',
  }
})
```

Innerhalb des Bereiches "test" können nun Änderungen für die Vitest Config angegeben werden. In diesem Fall wird das In-Source Testing hinzugefügt, womit in den ursprünglichen Dateien Code getestet werden kann, ohne extra Test-Dateien zu erstellen. Um im Build nicht den Testcode zu enthalten wird darunter ein define definiert, welches alles aus dem Build herausnimmt, was mit "import.meta.vitest" markiert ist.

Damit das In-Source Testing auch innerhalb von TypeScript funktioniert und keine Fehler auslöst, muss noch ein Type in der tsconfig.app.json definiert werden.

```JSON
"types": [
      "vitest/importMeta"
    ]
```

### Vitest VS-Code Extention

Es gibt eine VS-Code Extention, die man zusätzlich installieren kann. Die Extention heißt Vitest und wurde von vitest.dev gepublished.
Mithilfe der Extention kann man die Tests über einen grünen Pfeil starten, welcher neben den Test-Funktionen steht, anstatt über die Konsole die Tests zu starten.

## Testen mit Vitest

Tests werden entweder in einer seperaten Datei geschrieben oder mithilfe von In-Source Testing in der gleichen Datei, wie der restliche Code.

Dateien die Tests enthalten enden mit `.test.ts`

Um Vitest zu starten, muss folgender Command im Terminal eingegeben werden.

```
npm run test
```

### Mögliche Assertions

Vitest bietet eine Vielzahl von Assertions die für Tests verwendet werden können:

```TypeScript
expect(value).toBe(expected)           // Strikte Gleichheit (===)
expect(value).toEqual(expected)        // Deep equality (für Objects/Arrays)
expect(value).toBeTruthy()             // Truthy check
expect(value).toBeFalsy()              // Falsy check
expect(value).toBeNull()               // Null check
expect(value).toBeUndefined()          // Undefined check
expect(array).toContain(item)          // Array enthält Element
expect(fn).toThrow(error)              // Funktion wirft Error
expect(value).toBeGreaterThan(number)  // Größer als
expect(value).toBeLessThan(number)     // Kleiner als
```

### Beispiel Testdatei

Grundlegender Import, welcher immer benötigt wird, um tests zu schreiben.

```TypeScript
import { describe, test, expect } from 'vitest';
```

Das `describe` wird verwendet, um mehrere Tests zusasmmen zu gruppieren.

Das `test`definiert den eigentlichen Test und führt den nachfolgenden Code aus.

Die Assertions werden mit `expect`definiert. Diese vergleichen den eingegangenen Wert mit dem zu erwarteten Wert.

Das folgende Beispiel zeigt die Verwendung der drei Funktionen.

```TypeScript
describe('deleteColor', () => {
  beforeEach(() => {
    setActivePinia(createPinia());  //es muss eine Pinia Instanz vor dem Testen erstellt werden
  });
  test('sollte eine Farbe löschen', () => {
    const store = useColorStore();
    store.createColor('Schwarz', '#000000', true);
    const id = store.colorList[0]!.id;

    store.deleteColor(id);

    expect(store.colorList).toHaveLength(0);
  });

  test('sollte nichts tun wenn ID nicht existiert', () => {
    const store = useColorStore();
    store.createColor('Weiß', '#FFFFFF', true);

    store.deleteColor(999999);

    expect(store.colorList).toHaveLength(1);
    expect(store.colorList[0]!.name).toBe('Weiß');
  });
});
```

### In-Source Testing

In-Source Testing ermöglicht es, Tests direkt in derselben Datei, wo auch der zu testene Code ist, zu schreiben. Dies ist besonders nützlich für Unit-Tests von reinen Hilfsfunktionen oder isolierten Modulen, da der Testcode direkt beim dazugehörigen Code liegt.

Damit diese Tests nicht im Production-Build landen, werden sie in einen if-Block gekapselt. Durch die Konfiguration in der vite.config.ts (Abschnitt Setup) wird dieser Block beim Bauen der Anwendung komplett entfernt.

Beispiel für InSource-Testing:

```TypeScript
if (import.meta.vitest) {
  const { describe, it, expect, beforeEach } = import.meta.vitest;
  const { setActivePinia, createPinia } = await import("pinia");

  describe("Color Store In-Source Tests", () => {

    beforeEach(() => {
      setActivePinia(createPinia());
    });

    it("sollte eine neue Farbe erstellen", () => {
      const store = useColorStore();

      store.createColor("Blau", "#0000FF", true);

      expect(store.colorList).toHaveLength(1);
      expect(store.colorList[0]!.name).toBe("Blau");
      expect(store.colorList[0]!.hex).toBe("#0000FF");
    });

    it("sollte eine Farbe löschen können", () => {
      const store = useColorStore();
      store.createColor("Schwarz", "#000000", true);
      const idToDelete = store.colorList[0]!.id;

      store.deleteColor(idToDelete);

      expect(store.colorList).toHaveLength(0);
    });
  });
}

```
