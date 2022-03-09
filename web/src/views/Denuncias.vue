<template>
  <div class="container p-5">
    <Mapa />
  </div>
</template>

<script>
// @ is an alias to /src
import Mapa from '@/components/Denuncias/Mapa.vue'

export default {
  name: 'Denuncias',
  components: {
    Mapa
  }
}
</script>