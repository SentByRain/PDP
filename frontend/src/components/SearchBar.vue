<script setup lang="ts">
import { ref } from "vue";
const searcbarActive = ref(false);
// export default {
//   data() {
//     return {
//       contactQuery: "",
//       searcboxActive: false,
//     };
//   },
//   inject: ["contactStore"],
//   methods: {
//     searchSimilarContacts() {
//       const lettersInQuery = this.contactQuery.length;
//       this.contactStore.contacts.forEach((contact) => {
//         const cutContactName = contact.name
//           .substring(0, lettersInQuery)
//           .toLowerCase();
//         if (cutContactName !== this.contactQuery.toLowerCase()) {
//           document.querySelector(
//             'div[name = "' + contact.id + '"]'
//           ).style.display = "none";
//         } else {
//           document.querySelector(
//             'div[name = "' + contact.id + '"]'
//           ).style.display = "";
//         }
//       });
//     },
//     clearInline() {
//       this.contactQuery = "";
//       this.searchSimilarContacts();
//     },
//   },
// };
</script>

<template>
  <IconField class="search-bar-container">
    <InputText
      @focus="() => {}"
      @blur="() => {}"
      @keyup=""
      placeholder="Search"
      class="search-bar"
    />

    <transition name="spin-and-zoom">
      <InputIcon class="pi pi-times" @click="" />
    </transition>
  </IconField>
</template>

<style scoped>
.search-bar-container {
  display: flex;
  align-items: center;
  margin: 0 auto;
  padding: 0 1rem;
  max-width: 700px;
  min-height: 40px;
  height: 100%;
}

.search-bar {
  width: 100%;
  height: 25px;
  color: var(--p-secondary-color);
  font-size: medium;
  outline: none;
  border: none;
  background-color: #333;
  /* transform-origin: bottom left;
  transform: skew(-15deg); */
  margin-right: 10px;

  border-radius: 5px;
}

.searchbox:focus {
  box-shadow: none;
}

:deep(.pi-times) {
  color: var(--p-primary-color);
}
/* .searchbox::placeholder,
 {
  color: var(--p-primary-color);
} */

.searchbox:focus::placeholder {
  color: gray;
}

.p-input-icon {
  right: 1.5rem;
  cursor: pointer;
}

.spin-and-zoom-enter-active {
  animation: spin-and-zoom 200ms;
}

.spin-and-zoom-leave-active {
  animation: spin-and-zoom 200ms reverse;
}

@keyframes spin-and-zoom {
  from {
    transform: rotate(0deg);
    scale: 0;
  }
  to {
    transform: rotate(90deg);
    scale: 1;
  }
}
</style>
