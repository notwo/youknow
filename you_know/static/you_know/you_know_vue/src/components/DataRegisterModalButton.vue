<template>
  <section id="" class="btn-register floating">
    <a @click="openModal"></a>
  </section>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "DataRegisterButton",
  setup() {
    const openModal = () => {
      const modal = document.getElementsByClassName('overlay') as HTMLCollectionOf<HTMLElement>;
      modal[0].classList.add('visible');
    };

    return {
      openModal,
    };
  }
})
</script>

<style scoped>
.btn-register {
  position: fixed;
  top: 8rem;
  right: 6rem;
  z-index: 9999;
}
.btn-register a {
  display: block;
  position: relative;
  border-radius: 50%;
  width: 3.5rem;
  height: 3.5rem;
  cursor: pointer;
  background-color: rgba(0,180,180,.6);
  overflow: hidden;
}
.btn-register a:before {
  display: block;
  position: absolute;
  top: 50%;
  left: 50%;
  margin-left: -23%;
  margin-top: -28%;
  color: #FFF;
  font-size: 2rem;
  content: "+";
}

.floating {
  transition: .6s;
}
</style>
