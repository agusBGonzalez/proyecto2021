<template>
  <div class="container p-5">
    <Estadisticas />
  </div>
</template>

<script>
// @ is an alias to /src
import Estadisticas from '@/components/Estadisticas/Estadisticas.vue'

export default {
  name: 'EstadisticasView',
  components: {
    Estadisticas
  }
}
</script>