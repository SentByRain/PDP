<script setup lang="ts">
import { Form, type FormSubmitEvent } from "@primevue/forms";

import Button from "primevue/button";

import UserInput from "@/components/UserInput.vue";
import UserPassword from "@/components/UserPassword.vue";

import { useToast } from "primevue/usetoast";

import { AxiosKey } from "@/api/symbols";
import { injectStrict } from "@/api/injectTyped";
import { sendAuthInfo } from "@/api/requests";

import type {
  FormField,
  InputFormFields,
  PasswordFormFields,
} from "@/interfaces/reg&auth";

import router from "@/router/router";

import type { UserFormFields } from "@/interfaces/reg&auth";

import { zodResolver } from "@primevue/forms/resolvers/zod";
import { z } from "zod";

const authInputFields: FormField<InputFormFields>[] = [
  {
    name: "email",
    placeholder: "Почта",
  },
];

const authPasswordFields: FormField<PasswordFormFields>[] = [
  {
    name: "password",
    placeholder: "Пароль",
  },
];

const requestBase = injectStrict(AxiosKey);
const toast = useToast();

const resolver = zodResolver(
  z.object({
    email: z
      .string({ message: "Введите вашу почту" })
      .email({ message: "Проверьте адрес почты" }),
    password: z.string({ message: "Введите пароль" }),
  })
);

async function onFormSubmit(e: FormSubmitEvent) {
  if (e.valid) {
    const response = await sendAuthInfo(
      requestBase,
      e.states.email.value,
      e.states.password.value
    );
    if (response) {
      router.push("user");
    }
  } else {
    toast.add({
      severity: "warn",
      summary: "Проверьте введенные данные",
      life: 3000,
    });
  }
}
</script>

<template>
  <div class="auth-form-header">
    <h1>Войти</h1>
  </div>

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
      v-for="field in authInputFields"
      :name="field.name"
      :placeholder="field.placeholder"
    ></UserInput>
    <UserPassword
      :form="$form"
      v-for="field in authPasswordFields"
      :name="field.name"
      :placeholder="field.placeholder"
    >
    </UserPassword>
    <Button id="form-button" type="submit" label="Войти" />
    <div>
      <p style="text-align: center; font-size: 12px; margin: 0; color: #34d399">
        Еще нет аккаунта?<br />
        <router-link to="/register" class="form-link"
          >Зарегистрироваться</router-link
        >
      </p>
    </div>
  </Form>
</template>

<style>
.auth-form-header {
  color: #34d399;
  border-bottom: 1px solid #34d399;
  padding: 0 50px;
  text-align: center;
}
.auth-form-header h1 {
  font-size: 2rem;
  font-weight: 450;
  margin: 0;
}
</style>
