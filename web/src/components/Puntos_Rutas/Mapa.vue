<template>
  <div>
    <div class="mb-3 map-size">
      <l-map :zoom="zoom" :center="center">
        <l-tile-layer :url="url"></l-tile-layer>
        <div v-for="(punto, index) in puntos" :key="`puntos.${index}`">
          <l-marker :lat-lng="[punto.lat, punto.long]">
            <l-popup>
              <h4>{{ punto.nombre }}</h4>
              <div><strong>direccion:</strong> {{ punto.direccion }}</div>
              <div><strong>email:</strong> {{ punto.email }}</div>
              <div><strong>tel:</strong> {{ punto.telefono }}</div>
            </l-popup>
            <l-tooltip>¡Haga click para ver la informacion!</l-tooltip>
          </l-marker>
        </div>
        <div v-for="(recorrido, index) in recorridos" :key="`recorridos.${index}`">
          <l-polyline :lat-lngs="recorrido.coordenadas">
            <l-popup>
              <h4>{{ recorrido.nombre }}</h4>
            </l-popup>
            <l-tooltip>¡Haga click para ver la informacion!</l-tooltip>
          </l-polyline>
        </div>
      </l-map>
    </div>
    <div class="row d-flex flex-wrap">
      <div class="col-md-6 mt-5">
        <h2 class="mb-4"><i class="bi bi-geo-alt-fill"></i> Puntos</h2>
        <div v-for="(punto, index) in puntos" :key="`puntos.${index}`">
          <div class="card mt-2 p-2 border-gradient">
            <h4>{{ punto.nombre }}</h4>
            <div><strong>direccion:</strong> {{ punto.direccion }}</div>
            <div><strong>email:</strong> {{ punto.email }}</div>
            <div><strong>tel:</strong> {{ punto.telefono }}</div>
          </div>
        </div>
      </div>
      <div class="col-md-6 mt-5">
        <h2 class="mb-4"><i class="bi bi-signpost-2-fill"></i> Rutas</h2>
        <div v-for="(recorrido, index) in recorridos" :key="`recorridos.${index}`">
          <div class="card mt-2 p-2 border-gradient">
            <h4>{{ recorrido.nombre }}</h4>
            <div><strong>descripcion:</strong> {{ recorrido.descripcion }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { LMap, LTileLayer, LMarker, LPopup, LTooltip, LPolyline } from "@vue-leaflet/vue-leaflet";

export default {
  name: "Mapa",
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LPopup,
    LTooltip, 
    LPolyline
  },
  data() {
    return {
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      center: [-34.921302, -57.954297],
      zoom: 14,
      puntos: [],
      recorridos: [],
    };
  },
  created() {
    fetch(
      "https://admin-grupo8.proyecto2021.linti.unlp.edu.ar/api/puntos-encuentro/not-pages"
    )
      .then((response) => {
        return response.json();
      })
      .then((json) => {
        this.puntos = json.puntos_encuentro;
      })
      .catch((e) => {
        console.log(e);
      });
    fetch(
      "https://admin-grupo8.proyecto2021.linti.unlp.edu.ar/api/recorrido-evacuacion/not-pages-latlng"
    )
      .then((response) => {
        return response.json();
      })
      .then((json) => {
        this.recorridos = json.recorrido_evacuacion;
      })
      .catch((e) => {
        console.log(e);
      });
  },
  mounted() {
    this.getUserPosition();
  },
  methods: {
    async getUserPosition() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(pos => {
          this.center = [ pos.coords.latitude , pos.coords.longitude ];
        });
      } else {
        alert("Su navegador no soporta geo localizacion.");
      }
    }
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