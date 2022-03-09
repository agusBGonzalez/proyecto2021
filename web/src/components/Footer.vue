<template>
  <footer class="bg-dark text-white">
    <div class="container">
      <div class="d-flex flex-wrap flex-row justify-content-center">
        <div class="pt-5 ps-4 pe-4">
          <p class="text-center num-size fw-bold fonth">100</p>
          <p class="text-center fw-bold fonth">Bomberos</p>
        </div>
        <div class="pt-5 ps-4 pe-4">
          <p class="text-center num-size fw-bold fonth">103</p>
          <p class="text-center fw-bold fonth">Defensa Civil</p>
        </div>
        <div class="pt-5 ps-4 pe-4">
          <p class="text-center num-size fw-bold fonth">106</p>
          <p class="text-center fw-bold fonth">Prefectura</p>
        </div>
        <div class="pt-5 ps-4 pe-4">
          <p class="text-center num-size fw-bold fonth">107</p>
          <p class="text-center fw-bold fonth">Ambulancia</p>
        </div>
        <div class="pt-5 ps-4 pe-4">
          <p class="text-center num-size fw-bold fonth">147</p>
          <p class="text-center fw-bold fonth">Atencion al Vecino</p>
        </div>
        <div class="pt-5 ps-4 pe-4">
          <p class="text-center num-size fw-bold fonth">911</p>
          <p class="text-center fw-bold fonth">Seguridad</p>
        </div>
      </div>
      <div class="row p-2 d-flex flex-wrap align-items-center">
        <div class="col-sm-10 text-center">
          <p class="navbar-brand text-wrap">
            <img class="logo" src="../assets/logo.png" alt="Logo de la app" />
            © 2021 Copyright: Esta pagina fue desarrollada por el Grupo 8 de la
            asignatura Proyecto de Software
          </p>
        </div>
        <div class="col-sm-2 text-center">
          <a class="navbar-brand">
            <i class="bi bi-instagram"></i>
          </a>
          <a class="navbar-brand">
            <i class="bi bi-twitter"></i>
          </a>
          <a class="navbar-brand">
            <i class="bi bi-facebook"></i>
          </a>
        </div>
        
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "Footer",
};
</script>

<style scoped>
.logo {
  height: 40px;
  width: 40px;
}

.num-size {
  font-size: 80px;
} 

.fonth {
  line-height: 0.7;
}
</style>