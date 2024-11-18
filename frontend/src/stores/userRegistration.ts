import { ref, computed } from "vue";
import { defineStore } from "pinia";

export type User = "teacher" | "student" | null;

export interface registrationInfo {
  role: User;
  username: String;
  surname: String;
  email: String;
  password: String;
  enteredCode: string;
}

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
