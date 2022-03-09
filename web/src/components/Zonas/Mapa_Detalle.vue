<template>
  <div>
    <div class="mb-3 map-size">
      <l-map :zoom="zoom" :center="center">
        <l-tile-layer :url="url"></l-tile-layer>
        <l-polygon
          :lat-lngs="zona.coordenadas"
          :color="zona.color"
          :fill="true"
          :fillColor="zona.color"
        >
          <l-popup>
            <h4>{{ zona.nombre }}</h4>
          </l-popup>
          <l-tooltip>¡Haga click para ver la informacion!</l-tooltip>
        </l-polygon>
      </l-map>
    </div>
    <div class="row justify-content-center">
      <div class="col-lg-6 mt-5">
        <h2 class="mb-4 text-center">
          <i class="bi bi-info-square-fill"></i> Informacion de la Zona
        </h2>

        <div class="card mt-2 p-2 border-gradient">
          <div class="row">
            <div class="col-8">
              <div class="row">
                <h4>{{ zona.nombre }}</h4>
                <div>
                  <strong>Cantidad de coordenadas:</strong> {{ cant_coords }}
                </div>
                <div><strong>Hex. del color:</strong> {{ zona.color }}</div>
              </div>
              <div class="row">
                <div class="col">
                  <button class="btn btn-info" @click="go_back">
                    <i class="bi bi-arrow-left-square"></i> Volver al mapa de
                    zonas
                  </button>
                </div>
              </div>
            </div>
            <div class="col-4">
              <div class="color-zona" :style="`--color: ${zona.color}`"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {
  LMap,
  LTileLayer,
  LPolygon,
  LPopup,
  LTooltip,
} from "@vue-leaflet/vue-leaflet";

export default {
  name: "MapaDetalle",
  components: {
    LMap,
    LTileLayer,
    LPolygon,
    LPopup,
    LTooltip,
  },
  data() {
    return {
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      center: [-34.921302, -57.954297],
      zoom: 12,
      zona: "",
      cant_coords: "",
    };
  },
  created() {
    fetch(
      `https://admin-grupo8.proyecto2021.linti.unlp.edu.ar/api/zonas-inundables/${this.$route.params.id}/latlng`
    )
      .then((response) => {
        return response.json();
      })
      .then((json) => {
        this.zona = json.atributos;
        this.cant_coords = this.zona.coordenadas.length;
        this.center = this.zona.coordenadas[0];
      })
      .catch((e) => {
        console.log(e);
      });
  },
  methods: {
    go_back() {
      this.$router.go(-1);
    },
  },
};
</script>

<style scoped>
.map-size {
  width: 100%;
  height: 500px;
  border: 1px solid #000000;
}

.color-zona {
  --color: #ffffff;
  height: 100%;
  width: 100%;
  background-color: var(--color);
  border: 2px solid #000000;
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