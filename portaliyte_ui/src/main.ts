import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import VueCookies from 'vue-cookies'

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import '@mdi/font/css/materialdesignicons.css'
const vuetify = createVuetify({
  components,
  directives,
  icons: {
    defaultSet: 'mdi'
  }
})

import App from './App.vue'
import router from './router'
import type { Plugin } from '@vue/runtime-core'
const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(vuetify)
app.use(VueCookies as unknown as Plugin<[]>)

app.mount('#app')
