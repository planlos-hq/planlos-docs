# Bootstrap

Bootstrap ist ein weit verbreitetes CSS-Framework, dass die Entwicklung moderner und responsiver Benutzeroberflächen erleichtert. Es bietet zahlreiche vorgefertigte Komponenten und Klassen, die die Erstellung komplexer Layouts stark vereinfacht. In diesem Projekt wird BootstrapVueNext verwendet, das Vue-Komponenten für Bootstrap bereitstellt.

## Setup

Die Installation erfolgt über folgenden Befehl:
```bash
npm i bootstrap bootstrap-vue-next
```
Es gibt verschiedene Einbindungsmöglichkeiten. In diesem Projekt wird Bootstrap über die `<BApp>`-Komponenten-Variante eingebunden.


Einbindung in `App.vue`:
```vue
<template>
  <BApp>
    <!-- Your application content -->
    <router-view />
  </BApp>
</template>

<script setup lang="ts">
    import {BApp} from 'bootstrap-vue-next'
</script>
```
Einbindung in `main.ts`
```ts
import {createApp} from 'vue'
import App from './App.vue'

// Add the necessary CSS
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-next/dist/bootstrap-vue-next.css'

const app = createApp(App)
app.mount('#app')
```

## Komponenten
Bootstrap stellt verschiedene Komponenten bereit. Eine Übersicht und die jeweiligen Details über alle Komponenten findet man hier: https://bootstrap-vue-next.github.io/bootstrap-vue-next/docs.html. 

### Verwendung
Jede Komponente die eingebunden werden kann beginnt mit einem `B`, z.B. `<BApp>`.

Damit diese im Template verwendet werden können, müssen sie im `script` importiert werden.
```ts
import {BApp} from 'bootstrap-vue-next'
```
Der Stil ist mit eigenen CSS-Klassen überschreibbar. In diesem Projekt wird empfohlen, die Standarddesigns aufgrund der Einheitlichkeit beizubehalten.

Einige Komponenten, z.B. Buttons, haben verschiedene Varianten. Bevor ein eigenes Design ausgearbeitet wird, sollte nachgeschaut werden, ob nicht eine Standardkomponente für den Anwendungsfall bereits existiert. Beispielhaft kann man Buttons, die eine "gefährliche" Funktion mit folgender Variante anpassen. Dadurch ändert sich die Hintergrundfarbe auf rot und die Schrift zu weiß. Auch die jeweiligen Styles beim Hovern usw. verändern sich mit den Varianten. Alle Varianten findet man hier: https://bootstrap-vue-next.github.io/bootstrap-vue-next/docs/reference/color-variants.html 

```html
<BButton variant="danger">Button</BButton>
```

## Klassen
Bootstrap stellt viele Klassen zur Verfügung. Diese können direkt an der Komponente mit `class="bootstrap-class"` eingebunden werden und sind nicht auf Bootstrap-Komponenten beschränkt. Bietet sich die Verwendung einer Bootstrap-Klasse an, so sollte diese auch genutzt werden.

```html
<div class="d-flex gap-2">
    <BButton
    id="show-btn"
    @click="show"
    >Open Modal</BButton
    >
    <BButton
    id="toggle-btn"
    @click="toggle"
    >Toggle Modal</BButton
    >
</div>
```

Bei den Klassen kommen häufig Abkürzungen vor, wie z.B. `class="pb-2"` oder `class="mb-2"`. Dabei bedeutet pb und mb jeweils padding-bottom und margin-bottom. Die Zahl dahinter beschreibt eine vordefinierte Stärke der Eigenschaft. Mit 0 wird das Attribut entfernt, auch wenn es standardmäßig gesetzt ist, und mit 5 wird der höchste vordefinierte Wert gesetzt. 
Häufige Beispiele sind z.B.:
- `d-flex` - display:flex
- `flex-column`
- `justify-content-center`
- `align-items-center`
- `gap-3` - mittlerer Abstand
- `p-0` - kein Padding
- `m-0` - kein Margin 

```html
<div class="d-flex justify-content-between align-items-start mb-3">
  <BButton>Left</BButton>
  <BButton>Right</BButton>
</div>
```

# Weiteres
Neben eigenen Komponenten und CSS-Klassen können auch Composables und Direktiven verwendet werden.

## Composable:
Composables ermöglichen den Einsatz von Komponenten im Script und kapseln wiederverwendbare Logik.
```vue
<template>
  <ClientOnly>
    <BCard ref="target">
      <BButton @click="changeColor"> Current color: {{ mode }} </BButton>
    </BCard>
  </ClientOnly>
</template>

<script setup lang="ts">
import {ref} from 'vue'
import {useColorMode} from 'bootstrap-vue-next'
import {type BCard} from 'bootstrap-vue-next/components/BCard'

const target = ref<InstanceType<typeof BCard> | null>(null)

const mode = useColorMode({
  selector: target,
})

const changeColor = () => {
  mode.value = mode.value === 'dark' ? 'light' : 'dark'
}
</script>
```
Mehr Infos zu Composables unter https://bootstrap-vue-next.github.io/bootstrap-vue-next/docs/composables.html.

## Direktiven:
Direktiven binden Verhalten an Komponenten.
```vue
<template>
  <BCard v-b-color-mode="currentColor">
    <BButton @click="changeColor"> Current color: {{ currentColor }} </BButton>
  </BCard>
</template>

<script setup lang="ts">
import {vBColorMode} from 'bootstrap-vue-next/directives/BColorMode'

// Unlike the composable variant, this is not strongly typed by default!
const currentColor = ref<'light' | 'dark'>('dark')

const changeColor = () => {
  currentColor.value = currentColor.value === 'dark' ? 'light' : 'dark'
}
</script>
```
Mehr Infos zu Direktiven unter https://bootstrap-vue-next.github.io/bootstrap-vue-next/docs/directives.html.