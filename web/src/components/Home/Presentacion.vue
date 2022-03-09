<template>
  <div class="container mb-5">
    <div class="row d-flex flex-wrap">
      <div class="col-md-6">
        <div class="d-flex justify-content-center text-center p-3 transition">
          <router-link to="/puntos-y-rutas" class="no-style-a">
            <div class="icono-puntos p-3 mb-3">
              <i class="bi bi-geo-alt-fill punto-size"></i>
            </div>
            <h3>Puntos de Encuentro</h3>
            <p>
              ¿No conoces los puntos de encuentro en caso de emergencias? ¡Entra
              a esta seccion!
            </p>
          </router-link>
        </div>
      </div>
      <div class="col-md-6">
        <div class="d-flex justify-content-center text-center p-3 transition">
          <a href="#seccion-denuncia" class="no-style-a">
            <div class="icono-den p-3 mb-3">
              <i class="bi bi-chat-left-text-fill den-size"></i>
            </div>
            <h3>Haz una Denuncia</h3>
            <p>
              ¿Sabes de algun evento o situacion que pueda producir una
              inundacion? ¡Denuncialo!
            </p>
          </a>
        </div>
      </div>
    </div>
    <div class="row d-flex flex-wrap">
      <div class="col-md-6">
        <div class="d-flex justify-content-center text-center p-3 transition">
          <router-link to="/puntos-y-rutas" class="no-style-a">
            <div class="icono-recs p-3 mb-3">
              <i class="bi bi-geo-fill rec-size"></i>
            </div>
            <h3>Rutas de Evacuacion</h3>
            <p>
              ¿Quieres mantenerte informado sobre que rutas tomar en caso de
              inundacion? ¡Ven y conoce esas rutas!
            </p>
          </router-link>
        </div>
      </div>
      <div class="col-md-6">
        <div class="d-flex justify-content-center text-center p-3 transition">
          <router-link to="/zonas" class="no-style-a">
            <div class="icono-zonas p-3 mb-3">
              <i class="bi bi-map-fill zona-size"></i>
            </div>
            <h3>Zonas de Inudacion</h3>
            <p>
              ¿No estas seguro de que zonas de La Plata son mas propensas a
              inundaciones? ¡Esta seccion es para vos!
            </p>
          </router-link>
        </div>
      </div>
    </div>
    <div class="row d-flex flex-wrap">
      <div class="col-md-6">
        <div class="d-flex justify-content-center text-center p-3 transition">
          <router-link to="/estadisticas" class="no-style-a">
            <div class="icono-est p-3 mb-3">
              <i class="bi bi-bar-chart-line-fill est-size"></i>
            </div>
            <h3>Estadisticas</h3>
            <p>
              Examina las estadisticas de la pagina e informate de muchas mas cosas.
            </p>
          </router-link>
        </div>
      </div>
      <div class="col-md-6">
        <div class="d-flex justify-content-center text-center p-3 transition">
          <router-link to="/denuncias" class="no-style-a">
            <div class="icono-dens p-3 mb-3">
              <i class="bi bi-exclamation-diamond-fill dens-size"></i>
            </div>
            <h3>Ver Denuncias</h3>
            <p>
              ¡Entra y mira la ubicacion de todas las denuncias que fueron confirmadas!
            </p>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Content",
};
</script>

<style scoped>
.punto-size,
.zona-size,
.rec-size,
.den-size,
.dens-size,
.est-size {
  font-size: 80px;
  color: #ffffff;
}

.icono-puntos,
.icono-zonas,
.icono-est,
.icono-den,
.icono-recs,
.icono-dens {
  display: inline-block;
  width: 160px;
  height: 160px;
  border-radius: 50%;
  justify-content: center;
}

.icono-puntos {
  background: linear-gradient(to right, #22c1c3, #fdbb2d);
}

.icono-zonas {
  background: linear-gradient(to right, #ffab13, #4f76fb);
}

.icono-est {
  background: linear-gradient(to right, #c35122, #352dfd);
}

.icono-den {
  background: linear-gradient(to right, #efff01, #fd2df0);
}

.icono-recs {
  background: linear-gradient(to right, #00ff71, #644bb8);
}

.icono-dens {
  background: linear-gradient(to right, #c322b0, #2dfd74);
}

.no-style-a {
  text-decoration: none;
  color: #000000;
}

.transition {
  transition: background-color 0, 5s ease;
}

.transition:hover {
  background-color: #f5f5f5;
  transition: background-color 0.5s ease;
  border-radius: 10px;
  box-shadow: rgba(0, 0, 0, 0.15) 1.95px 1.95px 2.6px;
}
</style>