import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import axios from './plugins/axios'
import "@/assets/bootstrap.scss"
import "@/assets/main.scss"

let app = createApp(App).use(store).use(router).use(axios)
app.mount('#app')
