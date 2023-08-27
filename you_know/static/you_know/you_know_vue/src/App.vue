<template>
  <section class="full-layout">
    <section class="main">
      <NavigationHeader />

      <main class="container">
        <section class="main-right-pane"></section>
        <router-view></router-view>
        <section class="main-left-pane"></section>
      </main>
    </section>

  </section>
  <FooterInformation />
</template>

<script lang="ts">
import { defineComponent, provide } from "vue";
import { useStore } from '@/store/index';
import NavigationHeader from "@/components/NavigationHeader.vue";
import FooterInformation from "@/components/FooterInformation.vue";

export default defineComponent({
  name: "App",
  components: { NavigationHeader, FooterInformation },
  setup() {
    const store = useStore();
    provide('library', store);
  }
});

</script>

<style scoped>
.full-layout {
  display: flex;
  flex-direction: column;
  min-height: 100%;
}

.main {
  flex: 1;
}

.container {
  margin: 0 auto;
  max-width: 1100px;
  background: rgb(240, 242, 242);
}

.main-right-pane  {
}
.main-left-pane  {
}
</style>
