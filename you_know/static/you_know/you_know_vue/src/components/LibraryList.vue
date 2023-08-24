<template>
  <h3>librarylist</h3>
  <article id="library-list">
    <LibraryItem
      v-for="library in state.libraryList"
      :key="library.id"
      :title="library.title"
      :content="library.content"
      :created_at="library.created_at"
    />
  </article>
</template>

<script lang="ts">
import { defineComponent, reactive, onMounted } from 'vue';
import axios, { AxiosResponse, AxiosError } from "axios";
import LibraryItem from "@/components/LibraryItem.vue";

export default defineComponent({
  name: 'LibraryList',
  components: {
    LibraryItem
  },
  setup() {
    let state = reactive({
      libraryList: []
    });

    onMounted(() => {
      interface LibraryResponse {
        data: []
      };
      interface ErrorResponse {
        error: string
      };

      // ----------------------- events -----------------------
      axios.get<LibraryResponse>('http://127.0.0.1:8000/api/libraries/')
          .then((response: AxiosResponse) => {
            console.log(response)
            if (response.data.length >= 1) {
              state.libraryList = response.data;
            } else {
              //
            }
          })
          .catch((e: AxiosError<ErrorResponse>) => {
          });
    });

    return {
      state
    };
  },
});
</script>
