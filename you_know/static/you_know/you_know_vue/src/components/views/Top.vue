<template>
  <h3>TOP</h3>
</template>

<script lang="ts">
const modal = document.getElementsByClassName('search-wrap') as HTMLCollectionOf<HTMLElement>;
console.log(modal)
modal[0].style.display = 'none';
/*
import { defineComponent } from '@vue/composition-api'

export default defineComponent({
  setup() {
    
  },
})
*/
</script>

<style scoped>
</style>
