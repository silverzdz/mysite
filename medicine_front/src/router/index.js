import Vue from 'vue'
import Router from 'vue-router'
import axios from 'axios'
import ElementUI from 'element-ui'
import '@/theme-et/index.css'
Vue.use(ElementUI)
Vue.prototype.axios = axios
Vue.use(Router)

import medicine_lib from '@/components/medicine_lib'
import HelloWorld from '@/components/HelloWorld'
import index from '@/components/index'
import admin_index from '@/components/admin_index'
import add_doctor from '@/components/add_doctor'
import add_merchant from '@/components/add_merchant'
import patient_index from '@/components/patient_index'
import patient_register from '@/components/patient_register'
import patient_query from '@/components/patient_query'
import patient_covid from '@/components/patient_covid'
import patient_medicine from '@/components/patient_medicine'
import merchant_drug from '@/components/merchant_drug'
import sign_up from '@/components/sign_up'
import doctor_index from '@/components/doctor_index'

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: index
    },
    {
      path: '/sign_up',
      name: 'sign_up',
      component: sign_up
    },
    {
      path: '/admin',
      name: 'admin_index',
      component: admin_index
    },
    {
      path: '/admin/add_doctor',
      name: 'add_doctor',
      component: add_doctor
    },
    {
      path: '/admin/add_merchant',
      name: 'add_merchant',
      component: add_merchant
    },
    {
      path: '/patient',
      name: 'patient_index',
      component: patient_index
    },
    {
      path: '/patient/register',
      name: 'patient_register',
      component: patient_register
    },
    {
      path: '/patient/query',
      name: 'patient_query',
      component: patient_query
    },
    {
      path: '/patient/covid',
      name: 'patient_covid',
      component: patient_covid
    },
    {
      path: '/patient/medicine',
      name: 'patient_medicine',
      component: patient_medicine
    },
    {
      path: '/doctor',
      name: 'doctor_index',
      component: doctor_index
    },
    {
      path: '/merchant/drug',
      name: 'merchant_drug',
      component: merchant_drug
    },
    {
      path: '/medicine',
      name: 'medicine_lib',
      component: medicine_lib
    }
  ]
})
