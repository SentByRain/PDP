<script setup lang="ts">
import { defineComponent } from "vue";
import WeekDay from "./WeekDay.vue";
import Slot from "./Slot.vue";

const props = defineProps<{
  time: string[];
  weekDays: string[];
  daysDates: number[];
}>();
</script>

<template>
  <div id="schecule-container">
    <div id="time-column">
      <div v-for="hour in time" class="time-container">
        {{ hour }}
      </div>
    </div>

    <div id="weekday-row">
      <WeekDay
        v-for="(el, index) in weekDays"
        :key="index"
        :dayStr="el"
        :dayNum="daysDates[index]"
      >
      </WeekDay>
    </div>
    <!-- draw the table -->
    <div id="weekday-colomns">
      <!-- <div v-for="n in 7 * 14" class="weekday-content"></div> -->
      <div class="column" v-for="n in 7">
        <Slot style="grid-area: 1/-1"></Slot>
        <div
          style="
            grid-area: 1/-1;
            display: grid;
            grid-template-rows: repeat(14, 60px);
          "
        >
          <div v-for="n in 14" class="cell"></div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
#schecule-container {
  display: grid;

  grid-template-columns: 40px auto;
  grid-template-rows: 30px auto;

  grid-template-areas:
    ". weekday"
    "time content";

  /* временное свойство */
  margin: 100px;
  /* удалить все, что выше */
  overflow-y: auto;
  overflow-x: hidden;
}

#time-column {
  grid-area: time;

  margin-top: -1px;
  display: flex;
  flex-direction: column;
}

.time-container {
  display: flex;
  align-items: start;
  justify-content: end;

  height: 60px;
  padding: 2px 5px;
  border-top: 1px solid rgba(0, 0, 0, 0.2);

  color: rgba(0, 0, 0, 0.5);

  font-size: 13px;
}

#weekday-row {
  grid-area: weekday;

  display: grid;
  grid-template-columns: repeat(7, 1fr);

  border-right: 1px solid rgba(0, 0, 0, 0.2);
  /* border-top: 1px solid rgba(0, 0, 0, 0.2); */
}

.weekday {
  display: flex;
  flex-direction: row;
  justify-content: left;
  align-items: center;

  padding-left: 10px;

  border-left: 1px solid rgba(0, 0, 0, 0.2);
  border-bottom: 1px solid rgba(0, 0, 0, 0.2);

  color: rgba(0, 0, 0, 0.5);
  font-size: 20px;
}

#weekday-colomns {
  grid-area: content;

  display: grid;
  grid-template-columns: repeat(7, 1fr);

  border-right: 1px solid rgba(0, 0, 0, 0.2);
}
.column {
  /* display: flex;
  flex-direction: column; */
  display: grid;
  /* grid-template-rows: repeat(14,60px); */

  height: 100%;

  /* grid-template-rows: repeat(14, 60px); */
}

.cell {
  z-index: 1;
  height: 60px;
  border-left: 1px solid rgba(0, 0, 0, 0.2);
  border-bottom: 1px solid rgba(0, 0, 0, 0.2);
}
</style>
