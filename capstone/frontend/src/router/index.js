import Vue from 'vue'
import VueRouter from 'vue-router'
import Layout from '../components/Layout.vue'
import Appointments from '../views/Appointments/Appointments.vue'
import PatientDirectory from '../views/PatientDirectory/PatientDirectory.vue'
import Report from '../views/Reports/Report.vue'
import PatientMain from '../views/PatientInfo/PatientMain.vue'
import Settings from '../views/Settings/Settings.vue'
import NewAppointment from '../views/NewAppointment/NewAppointment.vue'
import NewPatient from '../views/NewPatient/NewPatient.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    component: Layout,
    children: [
      {
        path: '',
        name: 'mainPage',
        component: () => import('../views/MainPage/MainContainer.vue')
      },
      {
        path: 'schedule',
        name: 'schedule'
      },
      {
        path: 'appointments',
        name: 'appointments',
        component: Appointments
        // component: () => import('../views/Appointments/Appointments.vue')
      },
      {
        path: 'directory',
        name: 'directory',
        component: PatientDirectory
      },
      {
        path: 'p/:id',
        name: 'patient-main',
        component: PatientMain,
        props: (route) => ({ id: parseInt(route.params.id) })
      },
      {
        path: 'p/:id/v/:visitNumber',
        name: 'report',
        component: Report,
        props: (route) => ({
          id: parseInt(route.params.id),
          visitNumber: parseInt(route.params.visitNumber)
        })
      },
      {
        path: 'support',
        name: 'support'
      }
    ]
  },
  {
    path: '/add/a',
    name: 'add-appointment',
    component: NewAppointment
  },
  {
    path: '/add/p',
    name: 'add-patient',
    component: NewPatient
  },
  {
    path: '/settings',
    name: 'settings',
    component: Settings
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../components/LoginPage.vue')
  },
  {
    path: '/*',
    name: 'NotFound',
    component: Settings
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
