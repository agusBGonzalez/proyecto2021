<template>
  <nav class="navbar static-top bg-navbar navbar-expand-md mb-5">
    <div class="container">
      <router-link to="/" class="navbar-brand d-flex align-items-center">
        <img class="logo" src="../assets/logo.png" alt="Logo de la app" />
        <div class="a-no-style"><strong>EvacuAR</strong></div>
      </router-link>

      <button
        class="navbar-toggler menu-button"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#MenuNavegacion"
        aria-controls="MenuNavegacion"
        aria-expanded="false"
        aria-label="Abrir Menu"
      >
        <i class="bi bi-list menu-size"></i>
      </button>
      <div id="MenuNavegacion" class="collapse navbar-collapse">
        <ul class="navbar-nav ms-auto text-center">
          <li class="nav-item">
            <router-link to="/puntos-y-rutas" class="nav-link link-menu"
              >PUNTOS Y RUTAS</router-link
            >
          </li>
          <li class="nav-item">
            <router-link to="/zonas" class="nav-link link-menu"
              >ZONAS INUNDABLES</router-link
            >
          </li>
          <li class="nav-item">
            <router-link to="/denuncias" class="nav-link link-menu"
              >DENUNCIAS</router-link
            >
          </li>
          <li class="nav-item">
            <router-link to="/estadisticas" class="nav-link link-menu"
              >ESTADISTICAS</router-link
            >
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Nav",
};
</script>

<style scoped>
#MenuNavegacion a.router-link-exact-active {
  background-color: #036b77 !important;
}

.logo {
  height: 40px;
  width: 40px;
}

.bg-navbar {
  background-color: #008290 !important;
}

#MenuNavegacion .link-menu {
  color: #ffffff !important;
  transition: background-color 0.5s ease;
}

#MenuNavegacion .link-menu:hover {
  background-color: #036b77 !important;
  transition: background-color 0.5s ease;
}

.menu-size {
  font-size: 30px;
}

.menu-button {
  border: 1px solid #000000 !important;
}

.a-no-style {
  display: inline-block;
  text-decoration: none;
  color: #ffffff;
  border-left: 3px solid #ffffff;
  font-size: 25px;
  margin-left: 5px;
  padding-left: 5px;
  height: 100%;
}
</style>