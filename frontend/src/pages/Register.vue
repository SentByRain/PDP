<script setup lang="ts">
import UserToggle from "@/components/UserToggle.vue";
import Button from "primevue/button";
import Toast from "primevue/toast";

import UserInput from "@/components/UserInput.vue";
import UserPassword from "@/components/UserPassword.vue";

import { Form, type FormSubmitEvent } from "@primevue/forms";

import type { UserFormFields } from "@/interfaces/reg&auth";

import { useToast } from "primevue/usetoast";

import { zodResolver } from "@primevue/forms/resolvers/zod";
import { z } from "zod";

import { injectStrict } from "@/api/injectTyped";
import { AxiosKey } from "@/api/symbols";
import { RegStoreKey } from "@/api/symbols";
import { requestVerificationCode } from "@/api/requests";

import type {
  FormField,
  InputFormFields,
  PasswordFormFields,
} from "@/interfaces/reg&auth";

import router from "@/router";

const regInputFields: FormField<InputFormFields>[] = [
  {
    name: "username",
    placeholder: "Имя",
  },
  {
    name: "surname",
    placeholder: "Фамилия",
  },
  {
    name: "email",
    placeholder: "Почта",
  },
];

const regPasswordFields: FormField<PasswordFormFields>[] = [
  {
    name: "password",
    placeholder: "Пароль",
  },
  {
    name: "repeatedPassword",
    placeholder: "Повторите пароль",
  },
];

const toast = useToast();

const requestBase = injectStrict(AxiosKey);
const userRegStore = injectStrict(RegStoreKey);

const resolver = zodResolver(
  z
    .object({
      username: z.string({ message: "Введите ваше имя" }),
      surname: z.string({ message: "Введите вашу фамилию" }),
      email: z
        .string({ message: "Введите вашу почту" })
        .email({ message: "Проверьте адрес почты" }),
      password: z
        .string({ message: "Введите пароль" })
        .min(5, { message: "Минимум 5 знаков" })
        .max(20, { message: "Максимум 20 знаков." })
        .refine((value) => /[0-9]/.test(value), {
          message: "Пароль должен содержать число",
        })
        .refine((value) => /[a-z]/.test(value), {
          message: "Пароль должен содержать прописную букву",
        })
        .refine((value) => /[A-Z]/.test(value), {
          message: "Пароль должен содержать заглавную букву",
        }),
      repeatedPassword: z
        .string({ message: "Введите пароль еще раз" })
        .min(5, { message: "Минимум 5 знаков" })
        .max(20, { message: "Максимум 20 знаков" }),
    })
    .refine(
      (values) => {
        return values.password === values.repeatedPassword;
      },
      {
        message: "Пароли не совпадают",
        path: ["repeatedPassword"],
      }
    )
);

const onFormSubmit = async (e: FormSubmitEvent) => {
  if (e.valid) {
    userRegStore.username = e.states.username.value;
    userRegStore.surname = e.states.surname.value;
    userRegStore.email = e.states.email.value;
    userRegStore.password = e.states.password.value;

    requestVerificationCode(requestBase, userRegStore);
    router.push({ name: "verification_code" });
  } else {
    toast.add({
      severity: "warn",
      summary: "Проверьте введенные данные",
      life: 3000,
    });
  }
};
</script>

<template>
  <div class="reg-form-header">
    <h1>Регистрация</h1>
  </div>
  <section
    style="
      width: 100%;
      height: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;

      gap: 30px 0;
    "
  >
    <UserToggle v-model="userRegStore.role"></UserToggle>
    <Toast />
    <Form
      v-slot="$form: UserFormFields"
      :resolver
      :validateOnValueUpdate="false"
      :validateOnBlur="true"
      @submit="onFormSubmit"
      class="form-base"
    >
      <UserInput
        :form="$form"
        v-for="field in regInputFields"
        :name="field.name"
        :placeholder="field.placeholder"
      ></UserInput>

      <UserPassword
        :form="$form"
        v-for="field in regPasswordFields"
        :name="field.name"
        :placeholder="field.placeholder"
      >
      </UserPassword>
      <Button id="form-button" type="submit" label="Отправить" />
    </Form>
    <div>
      <p style="text-align: center; font-size: 12px; margin: 0; color: #34d399">
        У вас уже есть аккаунт?<br />
        <router-link to="/auth" class="form-link">Войти</router-link>
      </p>
    </div>
  </section>
</template>

<style>
body {
  margin: 0;
}

.reg-form-header {
  /* background-color: #34d399; */
  color: #34d399;
  border-bottom: 1px solid #34d399;
  padding: 0 10px;
  /* border-radius: 10px; */
  width: 100%;
  text-align: center;
}

.reg-form-header h1 {
  font-size: 2rem;
  font-weight: 450;
  margin: 0;
}

#reg-page {
  display: flex;
  align-items: center;
  justify-content: center;

  width: 100%;
  height: 100vh;
  background-color: #333;
  overflow: hidden;
}

.p-formfield,
.p-floatlabel,
.p-inputtext,
.p-password {
  width: 100%;
}

.p-inputtext.p-variant-filled {
  --p-inputtext-filled-background: var(--p-inputtext-background);
}
.p-inputtext.p-variant-filled:focus {
  --p-inputtext-filled-focus-background: var(--p-inputtext-background);
}
.p-inputtext.p-variant-filled:enabled:hover {
  --p-inputtext-filled-hover-background: var(--p-inputtext-background);
}

#form-button {
  margin-top: 20px;
}
.p-floatlabel label {
  --p-floatlavel-font-weight: 400;
}
.p-invalid-message {
  font-size: 0.8rem;
  color: rgb(248, 113, 113);
}

.gen-code-text {
  padding: 10px;
  border-radius: 15px;
  color: #34d399;
}
.hide {
  color: #27272a;
}
</style>
