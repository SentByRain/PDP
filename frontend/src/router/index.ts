import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    children:[],
    redirect: "/auth",
    component: () => import("@/pages/LoginBase.vue"),
  },
  {
    path: "/auth",
    name: "auth",
    component: () => import("@/pages/Auth.vue"),
  },
  {
    path: "/register",
    name: "register",
    component: () => import("@/pages/Register.vue"),
  },
  {
    path: "/register/verification_code",
    name: "verification_code",
    component: () => import("@/pages/VerificationCode.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
