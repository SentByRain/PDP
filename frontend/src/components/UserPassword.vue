<script setup lang="ts">
import FloatLabel from "primevue/floatlabel";
import Message from "primevue/message";
import Password from "primevue/password";
import type { UserFormFields, PasswordFormFields } from "@/interfaces/reg&auth";

const field = defineProps<{
  name: PasswordFormFields;
  placeholder: string;
  form: UserFormFields;
}>();
</script>

<template>
  <FloatLabel variant="in">
    <Password :name="name" toggleMask />
    <label :for="name">{{ placeholder }}</label>
  </FloatLabel>
  <Message
    v-if="form[name]?.invalid"
    severity="error"
    size="small"
    variant="simple"
    class="p-invalid-message"
  >
    <div v-if="form[name].errors.length === 1">
      {{ form[name].error.message }}
    </div>
    <ul v-else class="my-0 px-4 flex flex-col gap-1">
      <li v-for="(error, index) of form[name].errors" :key="index">
        {{ error.message }}
      </li>
    </ul>
  </Message>
</template>

<style></style>
