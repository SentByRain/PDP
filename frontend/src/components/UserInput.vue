<script setup lang="ts">
import FloatLabel from "primevue/floatlabel";
import Message from "primevue/message";
import InputText from "primevue/inputtext";

import type { FormFieldState } from "@primevue/forms";
import { ref } from "vue";
import type { UserFormFields, InputFormFields } from "@/interfaces/reg&auth";
import { onMounted } from "vue";

const field = defineProps<{
  name: InputFormFields;
  placeholder: string;
  form: UserFormFields;
}>();
</script>

<template>
  <FloatLabel variant="in">
    <InputText :name="name" type="text" fluid />
    <label :for="name"> {{ placeholder }}</label>
  </FloatLabel>
  <Message
    v-if="form[name]?.invalid"
    severity="error"
    size="small"
    variant="simple"
    class="p-invalid-message"
    >{{ form[name].error.message }}</Message
  >
</template>

<style></style>
