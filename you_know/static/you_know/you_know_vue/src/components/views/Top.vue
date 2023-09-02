<template>
  <h3>TOP</h3>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import axios, { AxiosResponse, AxiosError } from "axios";

export default defineComponent({
  setup() {
    interface UserResponse {
      data: {}
    };

    interface ErrorResponse {
      message: String,
      name: String,
      code: String
    };

    // ----------------------- events -----------------------
    const uuid = window.localStorage.getItem(['UUID']);
    const username = window.localStorage.getItem(['USERNAME']);

    // あとで消す
    if (!uuid) {
      (async () => {
        await axios.get<UserResponse>('http://127.0.0.1:8000/api/users/', {
          params: { username: username }
        })
        .then((response: AxiosResponse) => {
          window.localStorage.setItem(['UUID'], response.data[0].uuid);
        })
        .catch((e: AxiosError<ErrorResponse>) => {
          console.log(`${e.message} ( ${e.name} ) code: ${e.code}`);
        });
      })();
    }
  },
})
</script>

<style scoped>
</style>
