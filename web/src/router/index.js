import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import(/* webpackChunkName: "about" */ '../views/Home.vue')
  },
  {
    path: '/zonas',
    name: 'Zonas',
    component: () => import(/* webpackChunkName: "about" */ '../views/Zonas/Zonas.vue')
  },
  {
    path: '/denuncias',
    name: 'Denuncias',
    component: () => import(/* webpackChunkName: "about" */ '../views/Denuncias.vue')
  },
  {
    path: '/puntos-y-rutas',
    name: 'Puntos y Rutas',
    component: () => import(/* webpackChunkName: "about" */ '../views/Puntos_Rutas.vue')
  },
  {
    path: '/zonas/:id',
    name: 'Zona Detalle',
    component: () => import(/* webpackChunkName: "about" */ '../views/Zonas/Zona_Detalle.vue')
  },
  {
    path: '/estadisticas',
    name: 'Estadisticas',
    component: () => import(/* webpackChunkName: "about" */ '../views/Estadisticas.vue')
  },
  {
    path: '/:catchAll(.*)',
    redirect: '/'
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
