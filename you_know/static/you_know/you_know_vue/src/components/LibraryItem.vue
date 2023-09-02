<template>
  <section class="library-item">
    <span @click="removeLibrary" class="delete-item" :data-id="id"></span>
    <section class="title">{{ title }}</section>
  </section>
</template>

<script lang="ts">
import { defineComponent, inject } from 'vue';
import axios, { AxiosResponse, AxiosError } from "axios";

export default defineComponent({
  name: 'LibraryItem',
  components: {},
  props: {
    id: Number,
    title: String,
    content: String,
    custom_user: String,
    custom_user_id: String,
    created_at: String,
    updated_at: String,
  },
  setup(props) {
    interface ErrorResponse {
      message: String,
      name: String,
      code: String
    };

    const store = inject('library');
    const removeLibrary = async (event: HTMLButtonEvent) => {
      if (!window.confirm(`ライブラリ「${props.title}」が削除されますが宜しいですか？`)) {
        return;
      }

      // api実行前に呼ばないとstoreの中身が検索できない
      store.remove(props.id);
      const id = event.currentTarget.getAttribute('data-id');
      await axios.delete(`http://127.0.0.1:8000/api/libraries/${id}`)
      .then((response: AxiosResponse) => {
      })
      .catch((e: AxiosError<ErrorResponse>) => {
        console.log(`${e.message} ( ${e.name} ) code: ${e.code}`);
      });
    };

    return {
      removeLibrary
    };
  },
});
</script>

<style scoped>
.library-item {
  width: calc(30% - 15px);
  margin: 0.6em;
  height: 7em;
  background-color: red;
  flex-wrap: wrap;
  /*box-shadow: 10px 10px 0 #222222;*/
}

.delete-item {
  display: block;
  position: relative;
  width: 2em;
  height: 2em;
  margin-left: auto;
}
.delete-item::before, .delete-item::after {
  display: block;
  position: absolute;
  content: '';
  width: 100%;
  height: 4px;
  top: 50%;
  left: 50%;
  background-color: black;
}
.delete-item::before {
  transform: translate(-50%,-50%) rotate(45deg);
}
.delete-item::after {
  transform: translate(-50%,-50%) rotate(-45deg);
}
</style>
