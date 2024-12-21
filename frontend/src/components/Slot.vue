<script setup lang="ts"></script>

<template>
  <div class="base blank">
    <div class="action-circle blank-circle">
      <span class="pi pi-plus blank-plus" style="font-size: 25px"> </span>
    </div>
  </div>
  <!-- <div class="base reserved">
    <div class="action-circle reserved-circle">
      <span class="pi pi-pen-to-square reserved-plus" style="font-size: 0.7rem">
      </span>
    </div>
  </div>
  <div class="base lesson">
    <div style=""></div>
  </div> -->
</template>

<style>
.base {
  display: flex;
  align-items: center;
  justify-content: center;

  margin: auto;
  height: 100%;
  width: 90%;

  border: 1px solid;
  border-radius: 10px;

  font-family: Arial, Helvetica, sans-serif;
  color: black;

  z-index: 2;

  /* background-color: white; */
}

.blank {
  background-color: rgba(20, 113, 167, 0.1);
  border: 1px solid rgba(32, 57, 184, 0.3);
}

.reserved {
  background-color: rgba(250, 26, 75, 0.3);
  border: 1px solid rgba(255, 0, 120, 0.6);
}

.action-circle {
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 30px;
  width: 20%;
  aspect-ratio: 1;
  border-radius: 50%;
  background-color: white;
}

.blank-circle {
  border: 1px solid rgba(10, 14, 247, 0.2);
}
.reserved-circle {
  border: 1px solid rgba(214, 7, 93, 0.5);
}

.pi {
  padding: 10px;
  margin: -10px;

  cursor: pointer;
}

.blank-plus {
  color: rgba(3, 41, 255, 0.25);
}

.reserved-plus {
  color: rgba(255, 6, 81, 0.5);
}

.lesson {
  border-color: #f9c434;
  background-color: rgba(238, 255, 6, 0.3);
}
</style>
