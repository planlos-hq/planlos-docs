# Vue Icons

Für die Verwendung von Icons wird die Bibliothek "lucide-vue-next" verwendet. 
Icons können über folgenden Link gefunden werden.

https://lucide.dev/icons/

1. Gewünschtes Icon anklicken 
2. "See in action" auswählen
3. auf "Vue" umschalten.

## Verwendung

```vue
<template>
  <div>
    <info />
  </div>
</template>

<script setup lang="ts">
import { Info } from 'lucide-vue-next';
</script>
```

Jedes Icon ist eine eigene Vue-Komponente und kann direkt aus `lucide-vue-next` importiert werden.

---


## Styling und Props

Lucide Icons akzeptieren alle SVG(Scalable Vector Graphics)-Attribute als Props.

```vue
<template>
  <info :size="40" color="red" stroke-width="2" />
</template>

<script setup lang="ts">
import { Info } from 'lucide-vue-next';
</script>
```
### Wichtigste Props

| Prop           | Beschreibung                          | Typ / Beispiel         |
|----------------|---------------------------------------|------------------------|
| `color`        | Strichfarbe des Icons                 | `"black"`, `"red"`     |
| `size`         | Größe des Icons in Pixeln             | `24`, `32`, `48`       |
| `stroke-width` | Stärke der Linien                     | `1`, `2`, `3`          |

Es gibt noch viele weitere SVG-Attribute. Nicht alle Attribute funktionieren auf allen Icons, z.B. `fill` wird nicht von allen Icons unterstützt.

Styling auch über CSS möglich, aber bevorzugt über Props regeln. 

## Links

Dokumentation: https://lucide.dev/guide/

Icon-Auswahl:  https://lucide.dev/icons/ 