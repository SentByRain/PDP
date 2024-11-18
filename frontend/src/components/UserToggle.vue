<script setup lang="ts">
import { ref } from "vue";
import Button from "primevue/button";

import type { User } from "@/stores/userRegistration";

enum ButtonStatus {
  Selected = "",
  Default = "secondary",
}

type UserStatus = ButtonStatus.Selected | ButtonStatus.Default;

const studentButtonStatus = ref<UserStatus>(ButtonStatus.Selected);
const teacherButtonStatus = ref<UserStatus>(ButtonStatus.Default);

const userRole = defineModel<User>();

function selectUser(event: Event) {
  const selectedButton = event.currentTarget as HTMLInputElement;

  //check if the button's been already selected
  if (selectedButton.dataset.pSeverity === "") {
    return;
  }

  if (selectedButton.id === "student-button") {
    userRole.value = "student";
    studentButtonStatus.value = ButtonStatus.Selected;
    teacherButtonStatus.value = ButtonStatus.Default;
  } else {
    userRole.value = "teacher";
    studentButtonStatus.value = ButtonStatus.Default;
    teacherButtonStatus.value = ButtonStatus.Selected;
  }
}
</script>

<template>
  <div class="toggle-container">
    <Button
      label="Ученик"
      id="student-button"
      :severity="studentButtonStatus"
      @click="selectUser"
    />

    <Button
      label="Преподаватель"
      id="teacher-button"
      :severity="teacherButtonStatus"
      @click="selectUser"
    />
  </div>
</template>

<style>
.toggle-container {
  display: flex;
  align-items: center;
  justify-content: center;

  width: 100%;
  border: 1px solid var(--p-button-secondary-color);

  --p-toggle-container-radius: 12px;
  --p-toggle-container-padding: 2px;
  border-radius: var(--p-toggle-container-radius);

  padding: var(--p-toggle-container-padding);
}

.p-button {
  width: 50%;
}

#student-button {
  --p-button-border-radius: calc(
      var(--p-toggle-container-radius) - var(--p-toggle-container-padding)
    )
    0 0
    calc(var(--p-toggle-container-radius) - var(--p-toggle-container-padding));
}

#teacher-button {
  --p-button-border-radius: 0
    calc(var(--p-toggle-container-radius) - var(--p-toggle-container-padding))
    calc(var(--p-toggle-container-radius) - var(--p-toggle-container-padding)) 0;
}
</style>
