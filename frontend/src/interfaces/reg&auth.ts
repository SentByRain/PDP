import type { FormFieldState, FormSlots } from "@primevue/forms";

export type User = "teacher" | "student" | null;

export interface registrationInfo {
  role: User;
  username: String;
  surname: String;
  email: String;
  password: String;
  enteredCode: string;
}

export interface UserFormFields extends FormSlots {
  username: FormFieldState;
  surname: FormFieldState;
  email: FormFieldState;
  password: FormFieldState;
  repeatedPassword: FormFieldState;
}

export type InputFormFields = "username" | "surname" | "email";
export type PasswordFormFields = "password" | "repeatedPassword";

export interface FormField <T> {
  name: T;
  placeholder: string;
}
