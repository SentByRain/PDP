<script setup lang="ts">
import { requestVerificationCode } from "@/api/requests";
import { ref } from "vue";
import type { AxiosInstance } from "axios";
import type { registrationInfo } from "@/stores/userRegistration";

function setTimer() {
  const newLetterTimer = setInterval(() => {
    timeLeft.value--;

    if (timeLeft.value === 0) {
      showSendButton.value = true;
      clearInterval(newLetterTimer);
    }
  }, 1000);
}

function refreshTimer() {
  timeLeft.value = refreshTime;

  showSendButton.value = false;
  setTimer();
}

const props = defineProps<{
  showSendButton: Boolean;
  requestBase: AxiosInstance;
  userRegStore: registrationInfo;
}>();

//потом поставить 30
const refreshTime: number = 5;
const timeLeft = ref<number>(refreshTime);
const showSendButton = ref<Boolean>(false);
setTimer();
</script>

<template>
  <div style="display: flex; flex-direction: column; text-align: center">
    <span
      v-if="!showSendButton"
      class="gen-code-text"
      style="font-size: 0.9rem"
    >
      Повторно код можно запросить через:
      {{ timeLeft }}
    </span>
    <span
      v-else
      class="gen-code-text"
      style="
        font-size: 0.9rem;
        text-decoration-skip-ink: none;
        text-decoration: underline;
      "
      @click="
        requestVerificationCode(props.requestBase, props.userRegStore),
          refreshTimer()
      "
      >Отправить новый код</span
    >
  </div>
</template>

<style></style>
