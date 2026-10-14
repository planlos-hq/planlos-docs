# VueCal
verwendete Version: 5.0.1-rc.28

VueCal wird als zentrale Kalenderkomponente in unserem Vue-Frontend eingetzt, um übersichtlich und interaktiv Stundenpläne darzustellen und zu bearbeiten. Die Bibliothek ermöglicht die leichte integration eines modernen Kalenders, der sich einfach und individuell konfigurieren lässt.

In diesem Projekt wird VueCal hauptsächlich zur Planung von Stundenplänen verwendet. Es werden nur die dafür relevanten Aspekte betrachtet. Diese und zusätzliche Informationen sind in der offiziellen Dokumentation: <https://antoniandre.github.io/vue-cal/> zu finden.

## Vorteile & Features

- stark individuell konfigurierbar (Props, CSS und Slots)
- verschiedene Ansichten (Tag, Tage, Woche, Monat, Jahr, Jahre) verfügbar
- Anlegen von Schedules im Kalender möglich
  - Planung für mehrere Entitäten gleichzeitig
- Erstellung von Terminen (Events) und Hinzufügen zum Kalender (oder einzelnen Schedules)
- Interaktion mit Terminen (Events)
  - z.B. verschieben per Drag & Drop, Event-Größe ändern, löschen, usw.

## Nutzung der VueCal-Komponente

Um die VueCal-Komponente verwenden zu können, sind in der entsprechenden Vue-Komponente bzw. -View folgende Importe notwendig:

```TS
import { VueCal } from 'vue-cal'
import 'vue-cal/style'
```

Die Komponente kann dann im template folgendermaßen genutzt werden:

```HTML
<template>
    <div>
        <vue-cal ... />
    </div>
</template>
```

## Konfiguration von VueCal

Prinzipiell gibt es 3 Wege, über die VueCal konfiguriert werden kann: Props, CSS und Slots.

### Konfiguration über Props

Über Props kann die grundlegende Konfiguration der VueCal Komponente vorgenommen werden:

```HTML

<vue-cal  
  :dark="true"
  :timeFrom="8*60"
  :timeTo="22*60"
  :timeStep="30"
  :snapToInterval="15"
  ...
  />
```

Props des Typs boolean können dabei auch mit folgender schreibweise übergeben werden:

```HTML
<vue-cal dark/>
```

Alle Props für die Konfiguration des Kalenders auf diese Weise direkt zu übergeben, kann allerdings schnell zur Unübersichtlichkeit führen.

Aus diesem Grund sollen alle grundlegenden "Props"-Konfigurationen (in ein config-Objekt) in eine Config-Datei "timetableConfig.ts" ausgelagert werden:

```HTML
<vue-cal v-bind="timetableConfig" />
```

```TS
export const timetableConfig = {
  timeFrom: 8 * 60, // 8:00 Uhr
  timeTo: 22 * 60, // 22:00 Uhr
  timeStep: 30,
  snapToInterval: 15,
  ...
  }
```

Bei einigen VueCal-Props macht es zudem Sinn, den genauen Effekt durch z.B. einen Inline-Kommentar zu vermerken.

Alle möglichen Konfigurationsoptionen sind zu finden unter: <https://antoniandre.github.io/vue-cal/api> (unter Options)

### Konfiguration über CSS

#### CSS-Variablen

Bei Nutzung des "default Themes" ist es möglich den Kalender optisch über einige bereitsgestellte CSS-Variablen zu indiviualisieren.

```VUE
<style lang="css" scoped>
    .vuecal{
        --vuecal-primary-color: #1976d2;
        --vuecal-secondary-color: #ffffff;
        --vuecal-base-color: #000000;
    }
</style>
```

Die CSS-Variablen sind unter <https://antoniandre.github.io/vue-cal/examples/view> CSS-Control dokumentiert.

#### Styles überschreiben

Des Weiteren können auch die existierenden Styles der VueCal-Komponenten überschrieben werden. 
So kann man zum Beispiel die Linie, die den jetzigen Zeitpunkt hervorhebt, folgendermaßen entfernen:

```VUE
<style lang="css" scoped>
    :deep(.vuecal__now-line) {
        display: none !important;
    }
</style>
```

Da wir mit `<style scoped>` arbeiten, ist es nötig, `:deep` zu verwenden, damit die Style-Änderung auch in der Kindkomponente VueCal übernommen wird. Zudem ist `!important` nötig, um default oder inline Style zu überschreiben, welche eigentlich eine höhere Priorität besitzen.

##### Hinweis

Das direkte Überschreiben von bestimmten VueCal-CSS-Klassen z.B. mit `display: none !important;` o.ä. kann durchaus die Funktionalität der VueCal-Komponente beeinträchtigen. Es sollte entsprechend nur mit Bedacht geschehen und nur wenn wirklich notwendig. Wenn die Möglichkeit existiert, sollten stets die zur Verfügung gestellten Props, CSS-Variablen oder Slots verwendet werden.

### Konfiguration über Slots

VueCal stellt zudem eine Reihe von Slots zur Verfügung, die es ermöglichen, den Kalendar optisch anzupassen, z.B.:

```HTML
<vue-cal>
  <template #time-cell="{ format24 }">
    <strong>{{ format24 }}</strong>
  </template>
</vue-cal>
```

Alle verfügbaren Slots sind zu finden unter <https://antoniandre.github.io/vue-cal/examples/customization> oder unter <https://antoniandre.github.io/vue-cal/api>.

## Stundenplanung mit Vue Cal

### Termine (Events)

Termine werden in VueCal als "Events" bezeichnet. Alle Events, welche im Kalendar angezeigt werden, sind als Prop an die VueCal-Komponente gebunden:

```HTML
<vue-cal :events="events" />
```

Ein Event muss dabei mindestens ein Start- und ein Enddatum besitzen. Zusätzlich können einige weitere Attribute, wie z.B. `title`, `content` und `class` (CSS-Klasse), sowie eigene Custom-Attribute hinzugefügt werden.

Beispiel für ein Event:

```TS
const events = [
    {
    id: 1,
    start: new Date(new Date().setHours(11, 30)),
    end: new Date(new Date().setHours(12, 30)),    title: "Mathe 2",
    },
    ...
]
```

### Schedules

<https://antoniandre.github.io/vue-cal/examples/schedules>

Die Nutzung von Schedules erlaubt es, für mehrere Entitäten gleichzeitig zu planen. Äquivalent zu den Events werden auch Schedules als Prop an die VueCal-Komponente gebunden:

```HTML
<vue-cal :events="events" :schedules="schedules" />
```

Grundsätzlich sind für ein Schedule ein `label` zur Benennung und Anzeige, sowie eine `id` nötig. Über eine CSS-`class` lässt sich zudem ein Style festlegen:

```TS
const schedules: [
    { 
        id: 1,
        label: 'Inf23W',
        class: 'schedule-1'
    },
    ...
]
```

Wenn man selbst keine `id` vergibt, macht VueCal dies auch automatisch (id aufsteigend von 1 - n). Die `id` ist notwendig, um Events spezifischen Schedules zuzuordnen. Dafür erhält ein Event das Attribut `schedule`, welches die `id` des Schedules enthält:

```TS
const schedules: [
    { id: 1, label: 'Inf23W', class: 'schedule-1'},
    ...
]
const events = [
    {
    id: 1,
    start: new Date(new Date().setHours(11, 30)),
    end: new Date(new Date().setHours(12, 30)),    title: "Mathe 2",
    schedule: 1
    },
    ...
]
```

### Emitted Events

VueCal stellt eine Reihe von Emits zur Verfügung, die es erlauben, auf bestimmte VueCal-Events zu reagieren:

Alle nutzbaren emitted Events sind unter <https://antoniandre.github.io/vue-cal/api> zu finden.

## Besonderheiten bei der Verwendung im Projekt

### Verwendung als Stundenplan

Im Projekt wird der Kalendar als Stundenplan genutzt. Termine lassen sich in VueCal allerdings nur mit Start- und Enddatum erstellen. Entsprechend ist folgendes notwendig:

- ausschließliche Nutzung der Wochenansicht
- Termine werden ausschließlich in einer einzigen repräsentativen Woche geseichert
  - Woche festlegen mit Prop `:viewDate="..."` 
  - Mapping zwischen Wochentag und Datum innerhalb der Woche notwendig

### Wochenansicht

- Sonntag deaktivieren
- Eventuell Tage auswählbar machen: 

```HTML
<vue-cal :hide-weekdays="['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']" />
```
