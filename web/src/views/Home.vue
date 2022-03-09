<template>
  <div class="home">
    <Bienvenida/>
    <Presentacion/>
    <Denuncia/>
  </div>
</template>

<script>
// @ is an alias to /src
import Presentacion from '@/components/Home/Presentacion.vue'
import Denuncia from '@/components/Home/Denuncia-form.vue'
import Bienvenida from '@/components/Home/Bienvenida.vue'

export default {
  name: 'Home',
  components: {
    Presentacion,
    Denuncia,
    Bienvenida
  }
}
</script>
