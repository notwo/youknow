<template>
  <article id="library-list">
    <LibraryItem
      v-for="library in libraryList"
      :key="library.id"
      :id="library.id"
      :title="library.title"
      :content="library.content"
      :custom_user="library.custom_user"
      :custom_user_id="library.custom_user_id"
      :created_at="library.created_at"
      :updated_at="library.updated_at"
    />
  </article>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted, inject } from 'vue';
import axios, { AxiosResponse, AxiosError } from "axios";
import LibraryItem from "@/components/LibraryItem.vue";

export default defineComponent({
  name: 'LibraryList',
  components: {
    LibraryItem
  },
  setup() {
    const libraryList = ref([]);
    const store = inject('library');
    const auth0 = store.getUser();

    onMounted(() => {
      interface LibraryResponse {
        data: []
      };
      interface ErrorResponse {
        error: string
      };

      // ----------------------- events -----------------------
      (async () => {
        await axios.get<LibraryResponse>('http://127.0.0.1:8000/api/libraries/')
          .then((response: AxiosResponse) => {
            if (response.data.length >= 1) {
              libraryList.value = response.data;
              store.setItem(response.data);
            }
          })
          .catch((e: AxiosError<ErrorResponse>) => {
          });
      })();
    });

    return {
      libraryList
    };
  },
});
</script>

<style scoped>
#library-list {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
}
</style>
