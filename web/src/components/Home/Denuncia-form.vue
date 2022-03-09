<template>
  <div class="container mb-5">
    <div id="seccion-denuncia" class="text-center mb-5">
      <h1>¿Tienes alguna denuncia?</h1>
    </div>
    <div class="row justify-content-center">
      <div class="col-lg-6 denuncia-form-container p-5">
        <div>
          <h2>Informacion de la denuncia</h2>
          <div class="mb-3">
            <label for="titulo" class="form-label">Titulo</label>
            <input
              ref="titulo"
              type="text"
              class="form-control"
              id="titulo"
              placeholder="Ingrese un titulo descriptivo de su denuncia"
              v-model="modelo.titulo"
              @keyup="validateInput('titulo')"
              @blur="validateInput('titulo')"
              v-bind:class="{
                input_forms: input_selected.titulo,
                input_forms_valid: input_valid.titulo,
                input_forms_invalid: input_invalid.titulo,
              }"
            />
            <small
              id="mensaje-ayuda-titulo"
              v-bind:class="{
                mensaje_ayuda_desactivado: !input_invalid.titulo,
              }"
              >de 4 a 100 caracteres, sin caracteres especiales ( @ , - , _ ,
              etc. ).</small
            >
          </div>
          <div class="mb-3">
            <label for="categoria" class="form-label">Categoria</label>
            <select
              ref="categoria"
              id="categoria"
              class="form-select"
              aria-label="Categorias"
              v-model="modelo.categoria"
              @keyup="validateInput('categoria')"
              @blur="validateInput('categoria')"
              v-bind:class="{
                input_forms: input_selected.categoria,
                input_forms_valid: input_valid.categoria,
                input_forms_invalid: input_invalid.categoria,
              }"
            >
              <option v-for="categoria in categorias" :key="categoria" :value="categoria.id">{{ categoria.nombre }}</option>
            </select>
            <small
              id="mensaje-ayuda-categoria"
              v-bind:class="{
                mensaje_ayuda_desactivado: !input_invalid.categoria,
              }"
              >debe seleccionar una categoria para su denuncia.</small
            >
          </div>
          <div class="mb-3">
            <label for="descripcion" class="form-label">Descripcion</label>
            <textarea
              ref="descripcion"
              class="form-control"
              id="descripcion"
              rows="3"
              maxlength="250"
              v-model="modelo.descripcion"
              @keyup="validateInput('descripcion')"
              @blur="validateInput('descripcion')"
              v-bind:class="{
                input_forms: input_selected.descripcion,
                input_forms_valid: input_valid.descripcion,
                input_forms_invalid: input_invalid.descripcion,
              }"
            ></textarea>
            <small
              id="mensaje-ayuda-descripcion"
              v-bind:class="{
                mensaje_ayuda_desactivado: !input_invalid.descripcion,
              }"
              >de 7 a 250 caracteres, cualquier tipo de caracter.</small
            >
          </div>
          <h2>Lugar de la denuncia</h2>
          <div class="mb-3 map-size">
            <l-map :zoom="zoom" :center="center" @click="onClick">
              <l-tile-layer :url="url"></l-tile-layer>
              <l-marker :lat-lng="markerLatLng"></l-marker>
            </l-map>
          </div>

          <h2>Informacion personal</h2>
          <div class="mb-3">
            <label for="apellido" class="form-label">Apellido</label>
            <input
              ref="apellido"
              type="text"
              class="form-control"
              id="apellido"
              placeholder="Ingrese su apellido"
              v-model="modelo.apellido"
              @keyup="validateInput('apellido')"
              @blur="validateInput('apellido')"
              v-bind:class="{
                input_forms: input_selected.apellido,
                input_forms_valid: input_valid.apellido,
                input_forms_invalid: input_invalid.apellido,
              }"
            />
            <small
              id="mensaje-ayuda-apellido"
              v-bind:class="{
                mensaje_ayuda_desactivado: !input_invalid.apellido,
              }"
              >de 4 a 100 caracteres, sin caracteres especiales ( @ , - , _ ,
              etc. ).</small
            >
          </div>
          <div class="mb-3">
            <label for="nombre" class="form-label">Nombre</label>
            <input
              ref="nombre"
              type="text"
              class="form-control"
              id="nombre"
              placeholder="Ingrese su nombre"
              v-model="modelo.nombre"
              @keyup="validateInput('nombre')"
              @blur="validateInput('nombre')"
              v-bind:class="{
                input_forms: input_selected.nombre,
                input_forms_valid: input_valid.nombre,
                input_forms_invalid: input_invalid.nombre,
              }"
            />
            <small
              id="mensaje-ayuda-nombre"
              v-bind:class="{
                mensaje_ayuda_desactivado: !input_invalid.nombre,
              }"
              >de 4 a 100 caracteres, sin caracteres especiales ( @ , - , _ ,
              etc. ).</small
            >
          </div>
          <div class="mb-3">
            <label for="telefono" class="form-label">Telefono o Celular</label>
            <input
              ref="telefono"
              type="text"
              class="form-control"
              id="telefono"
              placeholder="Ingrese su numero de telefono o de celular"
              v-model="modelo.telefono"
              @keyup="validateInput('telefono')"
              @blur="validateInput('telefono')"
              v-bind:class="{
                input_forms: input_selected.telefono,
                input_forms_valid: input_valid.telefono,
                input_forms_invalid: input_invalid.telefono,
              }"
            />
            <small
              id="mensaje-ayuda-telefono"
              v-bind:class="{
                mensaje_ayuda_desactivado: !input_invalid.telefono,
              }"
              >de 7 a 14 numeros, sin separacion.</small
            >
          </div>
          <div class="mb-3">
            <label for="email" class="form-label">Email</label>
            <input
              ref="email"
              type="email"
              class="form-control"
              id="email"
              placeholder="Ingrese su email"
              v-model="modelo.email"
              @keyup="validateInput('email')"
              @blur="validateInput('email')"
              v-bind:class="{
                input_forms: input_selected.email,
                input_forms_valid: input_valid.email,
                input_forms_invalid: input_invalid.email,
              }"
            />
            <small
              id="mensaje-ayuda-email"
              v-bind:class="{
                mensaje_ayuda_desactivado: !input_invalid.email,
              }"
              >ejemplos de emails validos: ejemplo@ejemplo.com ó
              ejemplo@ejemplo.com.ar</small
            >
          </div>
          <button class="btn btn-info" @click="save">Enviar</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { LMap, LTileLayer, LMarker } from "@vue-leaflet/vue-leaflet";
import axios from "axios";

export default {
  name: "Denuncia",
  components: {
    LMap,
    LTileLayer,
    LMarker,
  },
  data() {
    return {
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      center: [-34.921302, -57.954297],
      zoom: 14,
      markerLatLng: [],
      categorias: [],
      modelo: {
        titulo: "",
        categoria: "",
        descripcion: "",
        apellido: "",
        nombre: "",
        telefono: "",
        email: "",
      },
      campos_ok: {
        titulo: false,
        categoria: false,
        descripcion: false,
        coord: false,
        apellido: false,
        nombre: false,
        telefono: false,
        email: false,
      },
      patrones: {
        titulo: /^[a-zA-ZÀ-ÿ\s0-9]{4,100}$/,
        categoria: /./,
        descripcion: /.{7,250}/,
        nombre: /^[a-zA-ZÀ-ÿ\s]{4,100}$/,
        apellido: /^[a-zA-ZÀ-ÿ\s]{4,100}$/,
        email:
          /^([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+)\.([a-z]{2,8})(\.[a-z]{2,8})?$/,
        telefono: /^\d{7,14}/,
      },
      input_selected: {
        titulo: true,
        categoria: true,
        descripcion: true,
        nombre: true,
        apellido: true,
        email: true,
        telefono: true,
      },
      input_valid: {
        titulo: false,
        categoria: false,
        descripcion: false,
        nombre: false,
        apellido: false,
        email: false,
        telefono: false,
      },
      input_invalid: {
        titulo: false,
        categoria: false,
        descripcion: false,
        nombre: false,
        apellido: false,
        email: false,
        telefono: false,
      },
    };
  },
  created() {
    fetch("https://admin-grupo8.proyecto2021.linti.unlp.edu.ar/api/categorias/")
      .then((response) => {
        return response.json();
      })
      .then((json) => {
        this.categorias = json.categorias;
      })
      .catch((e) => {
        console.log(e);
      });
  },
  methods: {
    onClick(e) {
      if (e.latlng) {
        this.markerLatLng = e.latlng;
        this.campos_ok.coord = true;
      }
    },
    validateInput(ref) {
      let aRef = this.$refs[ref].id;
      if (this.patrones[aRef].test(this.modelo[aRef])) {
        this.campos_ok[aRef] = true;
        this.input_selected[aRef] = false;
        this.input_valid[aRef] = true;
        this.input_invalid[aRef] = false;
      } else {
        this.campos_ok[aRef] = false;
        this.input_selected[aRef] = false;
        this.input_valid[aRef] = false;
        this.input_invalid[aRef] = true;
      }
    },
    save() {
      if (
        !this.campos_ok.titulo ||
        !this.campos_ok.categoria ||
        !this.campos_ok.descripcion ||
        !this.campos_ok.coord ||
        !this.campos_ok.apellido ||
        !this.campos_ok.nombre ||
        !this.campos_ok.telefono ||
        !this.campos_ok.email
      ) {
        alert(
          "Por favor, complete el formularido de denuncia como es debido. Tenga en cuenta que debe seleccionar un punto en el mapa."
        );
      } else {
        axios
          .post(
            `https://admin-grupo8.proyecto2021.linti.unlp.edu.ar/api/denuncias/`,
            {
              titulo: this.modelo.titulo,
              categoria_id: this.modelo.categoria,
              descripcion: this.modelo.descripcion,
              latitud: this.markerLatLng.lat,
              longitud: this.markerLatLng.lng,
              apellido_denunciante: this.modelo.apellido,
              nombre_denunciante: this.modelo.nombre,
              telcel_denunciante: this.modelo.telefono,
              email_denunciante: this.modelo.email,
            }
          )
          .then((response) => {
            console.log(response);
          });
        // alert(
        //   `informacion de la denuncia:\nnombre completo del denunciante: ${this.modelo.apellido}, ${this.modelo.nombre}\ntelefono del denunciante: ${this.modelo.telefono}\nemail del denunciante: ${this.modelo.email}\ntitulo de la denuncia: ${this.modelo.titulo}\ncategoria: ${this.modelo.categoria}\ndescripcion: ${this.modelo.descripcion}\ncoordenadas de la denuncia: ${this.markerLatLng.lat},${this.markerLatLng.lng}`
        // );
        alert("Su denuncia fue enviada, en los proximos dias se comunicaran con usted para corroborar la informacion proporcionada.");
        //reseteo las variables del modelo
        for (const variable in this.modelo) {
          this.modelo[variable] = "";
        }
        //reseteo las variables del input_valid
        for (const variable in this.input_valid) {
          this.input_valid[variable] = false;
        }
        //reseteo las variables del input_selected
        for (const variable in this.input_selected) {
          this.input_selected[variable] = true;
        }
        //reseteo las variables de campos_ok
        for (const variable in this.campos_ok) {
          this.campos_ok[variable] = false;
        }
      }
    },
  },
};
</script>

<style scoped>
.denuncia-form-container {
  background-color: #eeeeee;
  border-radius: 8px;
  border: 1px;
  border-style: solid;

  border-image: linear-gradient(
      to right,
      rgba(214, 30, 178, 1) 0%,
      rgba(255, 231, 26, 1) 50%,
      rgba(0, 200, 255, 1) 100%
    )
    1;
}

.map-size {
  width: 100%;
  height: 500px;
  border: 1px solid #000000;
}

.input_forms:focus {
  box-shadow: none !important;
  border: 2px solid blue !important;
}

.input_forms_invalid {
  border: 2px solid red !important;
}

.input_forms_invalid:focus {
  box-shadow: none !important;
}

.input_forms_valid {
  border: 2px solid green !important;
}

.input_forms_valid:focus {
  box-shadow: none !important;
}

.mensaje_ayuda_desactivado {
  display: none;
}
</style>