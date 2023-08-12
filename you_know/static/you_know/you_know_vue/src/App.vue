<script lang="ts">
import { defineComponent } from "vue";
import NavigationHeader from "@/components/NavigationHeader.vue";
import FooterInformation from "@/components/FooterInformation.vue";
import DataRegisterModalButton from "@/components/DataRegisterModalButton.vue";

export default defineComponent({
  name: "App",
  components: { NavigationHeader, DataRegisterModalButton, FooterInformation },
});
</script>

<template>
  <header>
    <NavigationHeader />
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif+JP:wght@200&display=swap">
  </header>

  <main>
    <DataRegisterModalButton />
  </main>

  <FooterInformation />
</template>

<style scoped>
</style>
