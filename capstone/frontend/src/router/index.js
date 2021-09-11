/* eslint-disable no-unused-vars */
import Vue from 'vue'
import VueRouter from 'vue-router'
import Layout from '../components/Layout.vue'
import LayoutMobile from '../components/LayoutMobile.vue'
import AppointmentEntry from '../views/AppointmentEntry/AppointmentEntry.vue'
import Appointments from '../views/Appointments/Appointments.vue'
import AppointmentsMobile from '../views/Appointments/AppointmentsMobile.vue'
import PatientDirectory from '../views/PatientDirectory/PatientDirectory.vue'
import PatientDirectoryMobile from '../views/PatientDirectory/PatientDirectoryMobile.vue'
import Reports from '../views/Reports/Report.vue'
import ReportMobile from '../views/Reports/ReportMobile.vue'
import PatientMain from '../views/PatientInfo/PatientMain.vue'
import Upcoming from '../views/PatientInfo/Upcoming.vue'
import PatientMainMobile from '../views/PatientInfo/PatientMainMobile.vue'
import Settings from '../views/Settings/Settings.vue'
import SettingsMobile from '../views/Settings/SettingsMobile.vue'
import NewAppointment from '../views/NewAppointment/NewAppointment.vue'
import NewAppointmentMobile from '../views/NewAppointment/NewAppointmentMobile.vue'
import NewPatient from '../views/NewPatient/NewPatient.vue'
import NewPatientMobile from '../views/NewPatient/NewPatientMobile.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    components: {
      default: Layout,
      mobile: LayoutMobile
    },
    children: [
      {
        path: '',
        name: 'mainPage',
        components: {
          default: () => import('../views/MainPage/MainContainer.vue'),
          mobile: () => import('../views/MainPage/MainContainerMobile.vue')
        }
      },
      {
        path: 'schedule',
        name: 'schedule'
      },
      {
        path: 'appointments',
        name: 'appointments',
        components: {
          default: Appointments,
          mobile: AppointmentsMobile
        }
        // component: () => import('../views/AppointmentsMobile/AppointmentsMobile.vue')
      },
      {
        path: 'directory',
        name: 'directory',
        components: {
          default: PatientDirectory,
          mobile: PatientDirectoryMobile
        }
      },
      {
        path: 'p/:id',
        name: 'patient-main',
        redirect: 'p/:id/upcoming',
        components: {
          default: PatientMain,
          mobile: PatientMainMobile
        },
        props: (route) => ({ id: parseInt(route.params.id) }),
        children: [
          {
            path: 'upcoming',
            name: 'upcoming',
            components: {
              default: Upcoming,
              mobile: null
            }
          },
          {
            path: 'history',
            name: 'history',
            components: {
              default: Upcoming,
              mobile: null
            }
          },
          {
            path: 'reports',
            name: 'reports',
            components: {
              default: Reports,
              mobile: null
            }
          },
          {
            path: 'notes',
            name: 'notes',
            components: {
              default: Upcoming,
              mobile: null
            }
          }
        ]
      },
      {
        path: 'p/:id/v/:visitNumber',
        name: 'visit',
        components: {
          default: AppointmentEntry,
          mobile: ReportMobile
        },
        props: (route) => ({
          id: parseInt(route.params.id),
          visitNumber: parseInt(route.params.visitNumber)
        })
      },
      {
        path: 'support',
        name: 'support'
      },
      {
        path: '/add/a',
        name: 'add-appointment',
        components: {
          default: NewAppointment,
          mobile: NewAppointmentMobile
        }
      },
      {
        path: '/add/p',
        name: 'add-patient',
        components: {
          default: NewPatient,
          mobile: NewPatientMobile
        }
      },
      {
        path: '/settings',
        name: 'settings',
        components: {
          default: Settings,
          mobile: SettingsMobile
        }
      }
    ]
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
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
