<template>
  <section class="search-form">
    <form action="">
      <input type="text" name="search" id="search">
      <button type="button" @click="onSearch">ライブラリを検索</button>
    </form>
  </section>
</template>

<script lang="ts">
import { defineComponent, inject } from 'vue';
import axios, { AxiosResponse, AxiosError } from "axios";
import { isConstructorDeclaration } from 'typescript';

export default defineComponent({
  name: 'LibrarySearchForm',
  components: {},
  setup() {
    const store = inject('library');

    interface ErrorResponse {
      message: String,
      name: String,
      code: String
    };

    const onSearch = async (event: HTMLButtonEvent) => {
      const word = document.getElementById('search');
      if (word.value === '') {
        store.restore();
        return;
      }

      await axios.get(`http://127.0.0.1:8000/libraries/search?word=${word.value}`)
      .then((response: AxiosResponse) => {
        const _searchResult = JSON.parse(response.data);
        if (_searchResult.length <= 0) {
          store.allClear();
        }
        const _list = _searchResult.map((r: object, i: Number) => {
          const _pk = r.pk;
          const _fields = r.fields;
          _fields.id = _pk;
          _fields.custom_user_id = r.fields.custom_user;
          return _fields;
        });
        store.search(_list);
      })
      .catch((e: AxiosError<ErrorResponse>) => {
        console.log(`${e.message} ( ${e.name} ) code: ${e.code}`);
      });
    }

    return {
      onSearch
    };
  }
});
</script>
