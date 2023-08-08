<script setup>
  import Vue from 'vue'

  interface HTMLEvent<T extends EventTarget> extends Event {
    target: T;
  }

  export default Vue.extend({
  methods: {
    onMyClick(event: { target: HTMLButtonElement }) {
      console.log(event.target.parentElement?.getElementsByTagName("input"));
    },
  },
});
</script>

<template>
  <h2>kuzu</h2>
</template>
