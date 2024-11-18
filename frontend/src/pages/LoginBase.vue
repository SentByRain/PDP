<script setup lang="ts"></script>

<template>
  <div id="reg-page">
    <div
      style="
        display: flex;
        flex-direction: column;

        align-items: center;
        justify-content: center;

        gap: 30px 0;

        max-width: 400px;
        width: 50%;
        /* background-color: var(--p-button-secondary-background); */
        background-color: #27272a;
        padding: 45px;
        border-radius: 40px;
      "
    >
      <RouterView> </RouterView>
    </div>
  </div>
</template>

<style>
body {
  margin: 0;
}

.form-base {
  display: flex;
  flex-direction: column;
  gap: 10px 0;
  justify-content: center;
  align-items: center;
  width: 100%;
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

.form-link {
  color: #34d399;
}

/* .form-link:visited {
  color: #333;
} */
</style>
