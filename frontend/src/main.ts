import "./assets/main.css";
import "primeicons/primeicons.css";

import router from "@/router/router";

import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";

import PrimeVue from "primevue/config";
import Aura from "@primevue/themes/aura";

import ToastService from "primevue/toastservice";

import requestBase from "./api/requestBase";
import { AxiosKey } from "./api/symbols";

// import userRegStore from "./App.vue";
// import { StoreKey } from "./api/symbols";

const app = createApp(App);

app.use(router);

app.use(createPinia());

app.provide(AxiosKey, requestBase);

app.use(ToastService);

app.use(PrimeVue, {
  theme: {
    preset: Aura,
  },
});

app.mount("#app");
