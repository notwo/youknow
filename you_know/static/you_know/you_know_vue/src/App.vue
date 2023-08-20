<template>
  <section class="full-layout">
    <header>
      <NavigationHeader />
      <link rel="preconnect" href="https://fonts.googleapis.com">
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
      <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif+JP:wght@200&display=swap">
    </header>

    <main class="container">
      <section class="main-right-pane"></section>
      <router-view></router-view>
      <section class="main-left-pane"></section>
    </main>

    <FooterInformation />
  </section>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import NavigationHeader from "@/components/NavigationHeader.vue";
import FooterInformation from "@/components/FooterInformation.vue";

export default defineComponent({
  name: "App",
  components: { NavigationHeader, FooterInformation },
});

</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  margin: 0 auto;
  background: rgb(240, 242, 242);
}

.main-right-pane  {
  display: flex;
  justify-content: left;
}
.main-left-pane  {
  display: flex;
  justify-content: right;
}
</style>
