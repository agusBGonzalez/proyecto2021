<template>
  <div class="row justify-content-center">
    <div class="col-lg-6">
      <h2 class="mb-4 text-center">
        <i class="bi bi-bar-chart-line-fill"></i> Estadisticas de la Pagina
      </h2>
      <!-- seccion -->
      <div class="card mt-2 p-2 border-gradient">
        <h4>Cantidad de Puntos</h4>
        <div><strong>publicados:</strong> {{ this.puntos_pub }}</div>
        <div><strong>despublicados:</strong> {{ this.puntos_despub }}</div>
      </div>
      <!-- seccion -->
      <div class="card mt-2 p-2 border-gradient">
        <h4>Cantidad de Zonas</h4>
        <div><strong>publicadas:</strong> {{ this.zonas_pub }}</div>
        <div><strong>despublicadas:</strong> {{ this.zonas_despub }}</div>
      </div>
      <!-- seccion -->
      <div class="card mt-2 p-2 border-gradient">
        <h4>Cantidad de Recorridos</h4>
        <div><strong>publicados:</strong> {{ this.recorridos_pub }}</div>
        <div><strong>despublicados:</strong> {{ this.recorridos_despub }}</div>
      </div>
      <!-- seccion -->
      <div class="card mt-2 p-2 border-gradient">
        <h4>Zona con mayor cantidad de coordenadas</h4>
        <div><strong>cantidad de coordenadas:</strong> {{ this.zona_max }}</div>
        <div>
          <strong>info:</strong> {{ this.zona_max_info.nombre }}
          <div
            class="color-zona"
            :style="`--color: ${zona_max_info.color}`"
          ></div>
        </div>
      </div>
      <!-- seccion -->
      <div class="card mt-2 p-2 border-gradient">
        <h4>Zona con menor cantidad de coordenadas</h4>
        <div><strong>cantidad de coordenadas:</strong> {{ this.zona_min }}</div>
        <div>
          <strong>info:</strong> {{ this.zona_min_info.nombre }}
          <div
            class="color-zona"
            :style="`--color: ${zona_min_info.color}`"
          ></div>
        </div>
      </div>
      <!-- seccion -->
      <div class="card mt-2 p-2 border-gradient">
        <h4>Recorrido con mayor cantidad de coordenadas</h4>
        <div>
          <strong>cantidad de coordenadas:</strong> {{ this.recorrido_max }}
        </div>
        <div><strong>nombre:</strong> {{ this.recorrido_max_info.nombre }}</div>
        <div>
          <strong>descripcion:</strong>
          {{ this.recorrido_max_info.descripcion }}
        </div>
      </div>
      <!-- seccion -->
      <div class="card mt-2 p-2 border-gradient">
        <h4>Recorrido con menor cantidad de coordenadas</h4>
        <div>
          <strong>cantidad de coordenadas:</strong> {{ this.recorrido_min }}
        </div>
        <div><strong>nombre:</strong> {{ this.recorrido_min_info.nombre }}</div>
        <div>
          <strong>descripcion:</strong>
          {{ this.recorrido_min_info.descripcion }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Estadisticas",
  data() {
    return {
      zona_max: "",
      zona_max_info: "",
      zona_min: "",
      zona_min_info: "",
      zonas_pub: "",
      zonas_despub: "",
      recorrido_max: "",
      recorrido_max_info: "",
      recorrido_min: "",
      recorrido_min_info: "",
      recorridos_pub: "",
      recorridos_despub: "",
      puntos_pub: "",
      puntos_despub: "",
    };
  },
  created() {
    fetch(
      `https://admin-grupo8.proyecto2021.linti.unlp.edu.ar/api/zonas-inundables/cant-pub`
    )
      .then((response) => {
        return response.json();
      })
      .then((json) => {
        this.zonas_pub = json.cantidad_publicados;
      })
      .catch((e) => {
        console.log(e);
      });
    fetch(
      `https://admin-grupo8.proyecto2021.linti.unlp.edu.ar/api/zonas-inundables/cant-despub`
    )
      .then((response) => {
        return response.json();
      })
      .then((json) => {
        this.zonas_despub = json.cantidad_despublicados;
      })
      .catch((e) => {
        console.log(e);
      });
    fetch(
      `https://admin-grupo8.proyecto2021.linti.unlp.edu.ar/api/zonas-inundables/max-coords`
    )
      .then((response) => {
        return response.json();
      })
      .then((json) => {
        this.zona_max = json.cant_coords;
        this.zona_max_info = json.zona_info;
      })
      .catch((e) => {
        console.log(e);
      });
    fetch(
      `https://admin-grupo8.proyecto2021.linti.unlp.edu.ar/api/zonas-inundables/min-coords`
    )
      .then((response) => {
        return response.json();
      })
      .then((json) => {
        this.zona_min = json.cant_coords;
        this.zona_min_info = json.zona_info;
      })
      .catch((e) => {
        console.log(e);
      });
    fetch(
      `https://admin-grupo8.proyecto2021.linti.unlp.edu.ar/api/recorrido-evacuacion/cant-pub`
    )
      .then((response) => {
        return response.json();
      })
      .then((json) => {
        this.recorridos_pub = json.cantidad_publicados;
      })
      .catch((e) => {
        console.log(e);
      });
    fetch(
      `https://admin-grupo8.proyecto2021.linti.unlp.edu.ar/api/recorrido-evacuacion/cant-despub`
    )
      .then((response) => {
        return response.json();
      })
      .then((json) => {
        this.recorridos_despub = json.cantidad_despublicados;
      })
      .catch((e) => {
        console.log(e);
      });
    fetch(
      `https://admin-grupo8.proyecto2021.linti.unlp.edu.ar/api/recorrido-evacuacion/max-coords`
    )
      .then((response) => {
        return response.json();
      })
      .then((json) => {
        this.recorrido_max_info = json.recorrido_info;
        this.recorrido_max = json.cant_coords;
      })
      .catch((e) => {
        console.log(e);
      });
    fetch(
      `https://admin-grupo8.proyecto2021.linti.unlp.edu.ar/api/recorrido-evacuacion/min-coords`
    )
      .then((response) => {
        return response.json();
      })
      .then((json) => {
        this.recorrido_min_info = json.recorrido_info;
        this.recorrido_min = json.cant_coords;
      })
      .catch((e) => {
        console.log(e);
      });
    fetch(
      `https://admin-grupo8.proyecto2021.linti.unlp.edu.ar/api/puntos-encuentro/cant-pub`
    )
      .then((response) => {
        return response.json();
      })
      .then((json) => {
        this.puntos_pub = json.cantidad_publicados;
      })
      .catch((e) => {
        console.log(e);
      });
    fetch(
      `https://admin-grupo8.proyecto2021.linti.unlp.edu.ar/api/puntos-encuentro/cant-despub`
    )
      .then((response) => {
        return response.json();
      })
      .then((json) => {
        this.puntos_despub = json.cantidad_despublicados;
      })
      .catch((e) => {
        console.log(e);
      });
  },
};
</script>

<style scoped>
.color-zona {
  display: inline-block;
  margin-left: 5px;
  --color: #ffffff;
  height: 15px;
  width: 15px;
  background-color: var(--color);
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