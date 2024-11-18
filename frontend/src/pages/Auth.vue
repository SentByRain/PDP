<script setup lang="ts">
import {
  Form,
  type FormFieldState,
  type FormSubmitEvent,
} from "@primevue/forms";

import Password from "primevue/password";
import FloatLabel from "primevue/floatlabel";
import Message from "primevue/message";
import InputText from "primevue/inputtext";
import Button from "primevue/button";
import { useToast } from "primevue/usetoast";

import { AxiosKey } from "@/api/symbols";
import { injectStrict } from "@/api/injectTyped";
import { sendAuthInfo } from "@/api/requests";

import { zodResolver } from "@primevue/forms/resolvers/zod";
import { z } from "zod";

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

interface AuthFormFields {
  email: FormFieldState;
  password: FormFieldState;
}

function onFormSubmit(e: FormSubmitEvent) {
  if (e.valid) {
    sendAuthInfo(requestBase, e.states.email.value, e.states.password.value);
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
    v-slot="$form: AuthFormFields"
    :resolver
    :validateOnValueUpdate="false"
    :validateOnBlur="true"
    @submit="onFormSubmit"
    class="form-base"
  >
    <FloatLabel variant="in">
      <InputText name="email" type="text" fluid />
      <label for="email">Почта</label>
    </FloatLabel>
    <Message
      v-if="$form.email?.invalid"
      severity="error"
      size="small"
      variant="simple"
      class="p-invalid-message"
      >{{ $form.email.error.message }}</Message
    >
    <FloatLabel variant="in">
      <Password name="password" toggleMask />
      <label for="password">Пароль</label>
    </FloatLabel>
    <Message
      v-if="$form.password?.invalid"
      severity="error"
      size="small"
      variant="simple"
      class="p-invalid-message"
      >{{ $form.password.error.message }}</Message
    >
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
