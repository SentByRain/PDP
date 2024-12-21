import { createRouter, createWebHistory } from "vue-router";

import LoginBase from "@/pages/LoginBase.vue";
import Auth from "@/pages/Auth.vue";
import Register from "@/pages/Register.vue";
import VerificationCode from "@/pages/VerificationCode.vue";
import User from "@/pages/User.vue";
import Schedule from "@/components/Schedule.vue";
import FileLoader from "@/pages/FileLoader.vue";

const routes = [
  {
    path: "/",
    children: [],
    redirect: "user",
    // redirect: "/auth",
    component: LoginBase,
  },
  {
    path: "/auth",
    name: "auth",
    component: Auth,
  },
  {
    path: "/register",
    name: "register",
    component: Register,
  },
  {
    path: "/register/verification_code",
    name: "verification_code",
    component: VerificationCode,
  },
  {
    path: "/user",
    name: "user",
    children: [],
    redirect: "/user/schedule",
    component: User,
  },
  {
    path: "/user/schedule",
    name: "schedule",
    component: Schedule,
  },
  {
    path: "/user/file_loader",
    name: "file_loader",
    component: FileLoader,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
