<template>
  <section class="library-item">
    <button @click="removeLibrary"></button>
  </section>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'LibraryItem',
  components: {},
  props: {
    id: Number,
    title: String,
    content: String,
    created_at: Date
  },
  setup(props) {
    const removeLibrary = () => {
    };

    return {
      removeLibrary
    };
  },
});
</script>
