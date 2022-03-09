import { createApp } from 'vue'
import router from './router'
import 'leaflet/dist/leaflet.css'
import App from './App.vue'

createApp(App).use(router).mount('#app')
