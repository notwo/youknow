<template>
  <DataRegisterModalButton />
  <LibraryRegistrationForm />
  <LibraryList />
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import DataRegisterModalButton from '@/components/DataRegisterModalButton.vue';
import LibraryRegistrationForm from '@/components/LibraryRegistrationForm.vue';
import LibraryList from '@/components/LibraryList.vue';

export default defineComponent({
  name: 'Libraries',
  components: {
    DataRegisterModalButton,
    LibraryRegistrationForm,
    LibraryList
  },
  setup () {
    //
  }
});
</script>
