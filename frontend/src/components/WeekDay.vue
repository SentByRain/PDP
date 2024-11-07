<script setup lang="ts">
const props = defineProps<{
  dayNum: number;
  dayStr: string;
}>();
</script>

<template>
  <div class="weekday">
    <span class="day-number"> {{ dayNum }} </span>
    <span class="day-word">{{ dayStr }}</span>
  </div>
</template>

<style>
.day-number {
  color: rgba(0, 0, 0, 0.8);
}

.day-word {
  font-size: 10px;
  margin-bottom: 10px;
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
</style>
