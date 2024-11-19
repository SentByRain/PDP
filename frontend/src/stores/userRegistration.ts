import { defineStore } from "pinia";
import type { registrationInfo } from "@/interfaces/reg&auth";

export const useUserRegStore = defineStore("userRegStore", {
  state: (): registrationInfo => {
    return {
      role: "student",
      username: "",
      surname: "",
      email: "",
      password: "",
      enteredCode: "",
    };
  },
});
