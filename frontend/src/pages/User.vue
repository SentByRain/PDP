<script setup lang="ts">
import { ref } from "vue";
import Menu from "primevue/menu";
import Drawer from "primevue/drawer";

import type { Link } from "../interfaces/index";
import NavigationBar from "@/components/NavigationBar.vue";
import SearchBar from "@/components/SearchBar.vue";

const menu = ref();
const visible = ref(false);

const items = ref([
  {
    label: "Options",
    items: [
      {
        label: "Refresh",
        icon: "pi pi-refresh",
      },
      {
        label: "Export",
        icon: "pi pi-upload",
      },
    ],
  },
]);

const toggle = (event: Event) => {
  menu.value.toggle(event);
};

const links: Link[] = [
  {
    name: "Расписание",
    path: "/user/schedule",
  },
  {
    name: "Материалы",
    path: "/user/file_loader",
  },
  {
    name: "Чат",
    path: "/auth",
  },
];
</script>

<template>
  <div class="account">
    <div class="account-header">
      <div class="logo">
        <i class="pi pi-bars navigation-button" @click="visible = true"> </i>
        <Drawer v-model:visible="visible" header="">
          <!-- change style in class -->
          <nav class="navigation-side-bar-mobile">
            <NavigationBar :links="links"></NavigationBar>
          </nav>
        </Drawer>
      </div>

      <div class="account-search-bar">
        <SearchBar></SearchBar>
      </div>
      <div class="account-header-buttons">
        <i class="pi pi-bell"> </i>
        <img
          src="../components/fake_img/me.jpg"
          alt="user"
          class="avatar"
          type="button"
          @click="toggle"
          aria-haspopup="true"
          aria-controls="overlay_menu"
        />
        <Menu ref="menu" id="overlay_menu" :model="items" :popup="true" />
      </div>
    </div>
    <div class="account-main">
      <nav class="navigation-bar">
        <NavigationBar :links="links"></NavigationBar>
      </nav>
      <div class="content-container">
        <div class="content">
          <RouterView></RouterView>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
:root {
  --header-container-height: 60px;
  --content-padding: 40px;
  --elements-radius: 10px;
  --blocks-gap: 15px;
}

.account {
  width: 100%;
  height: 100%;
  background-color: #333;
  overflow: hidden;
}
.account-header {
  display: grid;
  grid-template-columns: 1fr 5fr 1fr;
  height: var(--header-container-height);
  background-color: #444;
}

.logo {
  display: flex;
  align-items: center;
  justify-content: center;
}
.account-search-bar {
  /* display: flex;
  align-items: center; */
}
.account-header-buttons {
  display: flex;
  gap: 10%;
  align-items: center;
  justify-content: center;
}

/* temporal styles for pictures */
.avatar {
  margin: auto 0;
  object-fit: cover;
  border-radius: 50%;
  height: 40px;
  aspect-ratio: 1;
  cursor: pointer;
}

.account-main {
  /* display: flex; */
  height: calc(100vh - var(--header-container-height));
  overflow-y: auto;
  overflow-x: hidden;
}

.navigation-bar {
  display: flex;
  margin: var(--blocks-gap) 0;

  @media screen and (max-width: 500px) {
    display: none;
  }
}
.navigation-side-bar-mobile {
  display: flex;
  flex-direction: column;
  align-items: center;

  padding-top: var(--content-padding);
  gap: 10px;
}

.navigation-button {
  @media screen and (min-width: 500px) {
    display: none;
  }
}
.content-container {
  width: 100%;
  height: fit-content;
  padding: var(--blocks-gap);
  padding-top: 0;
}

.content {
  width: 100%;
  height: 100%;

  background-color: #444;
  border-radius: 20px;
  height: fit-content;
  padding: var(--content-padding);
}
</style>
