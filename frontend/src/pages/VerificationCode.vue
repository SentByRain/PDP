<script setup lang="ts">
import NewCodeButton from "@/components/NewCodeButton.vue";
import InputOtp from "primevue/inputotp";

import { injectStrict } from "@/api/injectTyped";
import { AxiosKey } from "@/api/symbols";
import { RegStoreKey } from "@/api/symbols";

import { sendUserInfo } from "@/api/requests";

import { ref } from "vue";

const requestBase = injectStrict(AxiosKey);
const userRegStore = injectStrict(RegStoreKey);

const showSendButton = ref<Boolean>(false);

// function sendVerificationCode(){
// const response = sendUserInfo(requestBase, userRegStore);
//  if(response.status===2000){

//  }
// };

</script>
<template>
  <section
    style="
      width: 100%;
      height: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;

      gap: 20px 0;
    "
  >
    <div style="display: flex; flex-direction: column; text-align: center">
      <span
        class="gen-code-text"
        style="
          font-size: 0.9rem;
          line-height: 1.3rem;
          border: 1px solid #34d399;
          background-color: #333;
        "
      >
        На вашу почту направлено письмо c кодом для подверждения
        регистрации.</span
      >
      <span class="gen-code-text" style="font-size: 1.5rem; margin-top: 10px"
        >Введите код ниже:
      </span>
    </div>

    <InputOtp
      v-model="userRegStore.enteredCode"
      @keyup.enter.exact="sendUserInfo(requestBase, userRegStore)"
    />
    <NewCodeButton
      :show-send-button="showSendButton"
      :user-reg-store="userRegStore"
      :request-base="requestBase"
    />
  </section>
</template>
<style></style>
