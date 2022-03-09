<template>
  <div>
    <div class="mb-3 map-size">
      <l-map :zoom="zoom" :center="center">
        <l-tile-layer :url="url"></l-tile-layer>
        <div v-for="(denuncia, index) in denuncias" :key="`denuncias.${index}`">
          <l-marker :lat-lng="[denuncia.latitud, denuncia.longitud]">
            <l-popup>
              <h4>{{ denuncia.titulo }}</h4>
              <div>
                <strong>descripcion:</strong> {{ denuncia.descripcion }}
              </div>
              <div><strong>estado:</strong> {{ denuncia.estado }}</div>
            </l-popup>
            <l-tooltip>¡Haga click para ver la informacion!</l-tooltip>
          </l-marker>
        </div>
      </l-map>
    </div>

    <div class="mt-5">
      <div class="card mt-2 p-2 border-gradient">
        <h4>Informacion de la seccion</h4>
        <p>
          En esta seccion usted puede informarse sobre las denuncias
          cargadas en el sistema.
        </p>
        <p>
          Tenga en cuenta que es un mapa interactivo, por lo que podra hacerle
          click a los marcadores para ver la informacion de dichas denuncias,
          tanto su estado, descripcion y la propia ubicacion, esta ultima la
          brinda el propio marcador.
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import {
  LMap,
  LTileLayer,
  LMarker,
  LPopup,
  LTooltip,
} from "@vue-leaflet/vue-leaflet";

export default {
  name: "Mapa",
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LPopup,
    LTooltip,
  },
  data() {
    return {
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      center: [-34.921302, -57.954297],
      zoom: 14,
      denuncias: [],
    };
  },
  created() {
    fetch(
      "https://admin-grupo8.proyecto2021.linti.unlp.edu.ar/api/denuncias/not-pages"
    )
      .then((response) => {
        return response.json();
      })
      .then((json) => {
        this.denuncias = json.denuncias;
      })
      .catch((e) => {
        console.log(e);
      });
  },
};
</script>

<style scoped>
.map-size {
  width: 100%;
  height: 500px;
  border: 1px solid #000000;
}

.border-gradient {
  border: 1px !important;
  border-style: solid !important;
  border-image: linear-gradient(
      to right,
      rgba(214, 30, 178, 1) 0%,
      rgba(255, 231, 26, 1) 50%,
      rgba(0, 200, 255, 1) 100%
    )
    1 !important;
}
</style>