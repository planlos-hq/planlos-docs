# Pinia
## 1. Einleitung
**Pinia** ist das offizielle State-Management-Tool für Vue 3. Es ist der Nachfolger von Vuex und bietet eine einfachere, modulare und typsichere Möglichkeit, den Zustand (State) in Vue-Anwendungen zu verwalten.

### 1.1 Vorteile von Pinia
- **Modularität**: Jeder Store ist unabhängig und kann einfach importiert werden.
- **Typsicherheit**: Vollständige TypeScript-Unterstützung ohne komplizierte Typdefinitionen.
- **Devtools-Integration**: Unterstützt Vue Devtools direkt, inklusive Time-Travel Debugging.
- **Reaktive Stores**: Stores sind vollständig reaktiv und arbeiten nahtlos mit der Composition API zusammen.

## 2. Installation
Pinia kann mit npm, yarn, pnpm oder bun installiert werden.

Beispiel mit npm:
```bash 
npm install pinia
```
 
 Anschließend muss der Root Store noch in die App eingebunden werden:
```typescript
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'

const pinia = createPinia()
const app = createApp(App)

app.use(pinia)
app.mount('#app')
``` 

## 3. Grundkonzepte
Ein Store ist ein zentrales Objekt, welches aus einem Zustand (State), berechneten Werten (Getters) und Methoden (Actions) besteht.

### 3.1 State
Der State enthält die Daten, die global in der Anwendung geteilt werden.

Beispiel:
```TypeScript
import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useCounterStore = defineStore('counter', () => {
  //State
  const count = ref<number>(0)

  return { count }
})
```

Verwendung:
```Vue
<script setup lang="ts">
import { useCounterStore } from '@/stores/counter'

const counter = useCounterStore()
</script>

<template>
  <p>Zähler: {{ counter.count }}</p>
</template>
```

**Typisierung komplexer Objekte**

Für Objekte im State empfiehlt es sich, Interfaces zu definieren. Diese Interfaces können auch in seperaten Dateien geschrieben werden.

```TypeScript
interface User {
  id: number;
  name: string;
}

export const useUserStore = defineStore('user', () => {
  const user = ref<User | null>(null) // Typ explizit angeben
  return { user }
})
```

**Private State (Information Hiding)**
Variablen, die definiert, aber **nicht** im return-Statement zurückgegeben werden, sind von außen nicht sichtbar.

```TypeScript
export const useCounterStore = defineStore('counter', () => {
  const secretNumber = ref(42) // Diese Variable bleibt privat
  const publicNumber = ref(10)

  return { publicNumber } // Nur publicNumber ist öffentlich
})
```

Pinia State Dokumentation: https://pinia.vuejs.org/core-concepts/state.html
### 3.2 Getters
Getters sind berechnete Werte basierend auf dem State. 

Beispiel:
```TypeScript
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useCounterStore = defineStore('counter', () => {
  //State
  const count = ref<number>(0)

  //Getter
  const doubleCount = computed(() => count.value * 2)

  return { count, doubleCount }
})
```

Verwendung:
```Vue
<script setup lang="ts">
import { useCounterStore } from '@/stores/counter'

const counter = useCounterStore()
</script>

<template>
  <p>Verdoppelt: {{ counter.doubleCount }}</p>
</template>
```

**Zugriff auf andere Stores**

Der Counter könnte von globalen Einstellungen (z.B. einem Multiplikator) abhängen.

```TypeScript
import { useSettingsStore } from './settings'

export const useCounterStore = defineStore('counter', () => {
  const count = ref(10)
  const settings = useSettingsStore() // Anderen Store nutzen

  // Berechnet den Wert basierend auf dem Multiplikator im SettingsStore
  const multipliedCount = computed(() => count.value * settings.globalMultiplier)

  return { count, multipliedCount }
})
```

**Getter mit Argumenten**

Wir wollen prüfen, ob der Zählerstand durch eine bestimmte Zahl teilbar ist.

```TypeScript
export const useCounterStore = defineStore('counter', () => {
  const count = ref(10)

  // Gibt eine Funktion zurück, die Parameter akzeptiert
  const isDivisibleBy = computed(() => {
    return (divisor: number) => count.value % divisor === 0
  })

  return { count, isDivisibleBy }
})
```

Verwendung im Template: 
```HTML 
<p>Durch 5 teilbar? {{ counter.isDivisibleBy(5) }}</p>
```

Pinia Getters Dokumentation: https://pinia.vuejs.org/core-concepts/getters.html
### 3.3 Actions
Actions sind Funktionen, die den Zustand ändern oder asynchron sein können.

Beispiel:
```TypeScript
import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useCounterStore = defineStore('counter', () => {
  const count = ref<number>(0)

  function increment(): void {
    count.value++
  }
  
  async function incrementAsync() {
	await delay(500)
	count.value++
  }
  
  return { count, increment, incrementAsync }
})
```

Verwendung:
```Vue
<script setup lang="ts">
import { useCounterStore } from '@/stores/counter'
const counter = useCounterStore()
</script>

<template>
  <button @click="counter.increment">+1</button>
</template>
```

Pinia Actions Dokumentation: https://pinia.vuejs.org/core-concepts/actions.

### 3.4 Reaktivität und Destructuring 
Destructuring ist eine andere Art die Store Variablen in den Components zu nutzen. Vorher sah die Nutzung der Store variablen in der Template zum Beispiel so aus:
```HTML
<template>
  <div>
    <p>{{ userStore.firstName }}</p>
    <p>{{ userStore.lastName }}</p>
    <p>{{ userStore.email }}</p>
    <p>{{ userStore.role }}</p>
  </div>
</template>
```

Mithilfe von Destructuring können wir uns das "userStore." sparen und somit einfacher drauf zugreifen.
Im script Teil der Component:
```TypeScript
<script setup lang="ts">
import { storeToRefs } from 'pinia' 
import { useUserStore } from '@/stores/userStore'

const userStore = useUserStore()

const { firstName, lastName, email, role } = storeToRefs(userStore)

</script>
```
Die Verwendung von ```storeToRefs``` ist essenziell, damit die Reaktivität beibehalten wird.

Anschließend können im Template die Variablen folgendermaßen angesprochen werden:
```HTML
<template>
  <div>
    <p>{{ firstName }}</p>
    <p>{{ lastName }}</p>
    <p>{{ email }}</p>
    <p>{{ role }}</p>
  </div>
</template>
```

Dies funktioniert genauso mit Funktionen die im Store festgelegt sind. Angenommen wir haben eine ```changeName``` Funktion im Store definiert, dann können wir im Script Teil der Component die Funktion einfügen:
```TypeScript
const { changeName } = userStore 
//die Verwendung von storeToRefs ist hier nicht nötig
```
 Anschließend im Template:
 ```HTML
 <button @click="changeName"> 
	Klick mich: Ändere Namen zu "Anna" 
 </button>
 ```

## 4. Best Practices
- Information Hiding
	- Variablen und Funktionen die nur innerhalb des Stores genutzt werden
	- nicht im Return-Statement angeben
- Komplexe Logik im Store und nicht in Components
- kleine, modulare Stores
- Tief verschachtelte Objekte im State vermeiden
