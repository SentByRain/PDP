<script setup lang="ts">
import { provide} from "vue";

import { useUserRegStore } from "./stores/userRegistration";
import { RegStoreKey } from "./api/symbols";

import LoginBase from "./pages/LoginBase.vue";
import User from "./pages/User.vue";

const userRegStore = useUserRegStore();
provide(RegStoreKey, userRegStore);

// const weekDays = ["ПН", "ВТ", "СР", "ЧТ", "ПТ", "СБ", "ВС"];

// const currentWeekday = ref<number>(DateTime.now().weekday);

// currentWeekday.value === 1
//   ? DateTime.now()
//   : DateTime.now().minus({ days: currentWeekday.value + 1 });

// let daysDates: number[] = [];

// for (let i = 1; i < 8; i++) {
//   daysDates[i - 1] = DateTime.now().minus({
//     days: currentWeekday.value - i,
//   }).day;
// }

// let weekDates = [];
// const dayTime = [
//   "9:00",
//   "10:00",
//   "11:00",
//   "12:00",
//   "13:00",
//   "14:00",
//   "15:00",
//   "16:00",
//   "17:00",
//   "18:00",
//   "19:00",
//   "20:00",
//   "21:00",
//   "22:00",
// ];
</script>

<template>
  <!-- <Slot></Slot> -->
  <!-- 
  <Schedule :time="dayTime" :weekDays = "weekDays" :daysDates = "daysDates"></Schedule> -->

  <!-- <LoginBase></LoginBase> -->
  <User></User>
</template>

<style scoped>
</style>
