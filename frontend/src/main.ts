import './assets/main.css'
import 'primeicons/primeicons.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'

import PrimeVue from 'primevue/config';
import Aura from '@primevue/themes/aura';



const app = createApp(App)

app.use(createPinia())

app.use(PrimeVue,{
    theme: {
        preset: Aura
    }
});

app.mount('#app');
