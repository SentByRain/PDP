<script setup lang="ts">
import type { Link } from "../interfaces/index";

defineProps<{
  links: Link[];
}>();
</script>

<template>
  <div class="links-bar">
    <RouterLink
      :to="link.path"
      class="bar-link link-container"
      :class="{ 'link-container-active': $route.path === link.path }"
      v-for="link in links"
    >
      {{ link.name }}
    </RouterLink>
  </div>
</template>
<style>
.links-bar {
  display: flex;
  margin: 0 auto;

  --links-bar-radius: 12px;
  --links-bar-padding: 3px;

  border-radius: var(--links-bar-radius);
  border: 1px solid white;
  padding: var(--links-bar-padding);
}

.link-container {
  width: 100%;
  padding: 5px 15px;
  align-items: center;
  justify-content: center;
  cursor: pointer;

  --link-container-radius: calc(
    var(--links-bar-radius) - var(--links-bar-padding)
  );

  border-radius: var(--link-container-radius);

  &:hover {
    background-color: #5a5a5a;
  }
}

.link-container-active {
  background-color: var(--p-primary-color);
}

/* .link-container:first-child {
  border-radius: var(--link-container-radius) 0 0 var(--link-container-radius);
}
.link-container:last-child {
  border-radius: 0 var(--link-container-radius) var(--link-container-radius) 0;
} */

/* .link-container:hover:first-child {
  background-color: #5a5a5a;
  border-radius: var(--link-container-radius) 0 0 var(--link-container-radius);
} */
/* .link-container:hover {
  background-color: #5a5a5a;
} */
/* .link-container:hover:last-child {
  background-color: #5a5a5a;
  border-radius: 0 var(--link-container-radius) var(--link-container-radius) 0;
} */

.bar-link {
  text-align: center;
  color: var(--p-primary-color);
  text-decoration: none;
}
.bar-link:hover {
  color: var(--p-primary-hover-color);
  text-decoration: underline;
  transition: 0.1s;
}

.router-link-active {
  color: var(--p-secondary-color);
}
</style>
