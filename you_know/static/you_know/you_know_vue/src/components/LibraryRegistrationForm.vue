<template>
  <section class="overlay">
    <section class="modal">
      <form action="">
        <span id="close" class="close" @click="closeModal"></span>
        <label for="library_title" class="required">タイトル</label>
        <section class="form-field">
          <input type="text"
            :class="[v$.title.$errors.length >= 1 ? 'error' : '']"
            v-model="state.title"
            id="library_title"
            placeholder="新規ライブラリのタイトル"
            :error-messages="v$.title.$errors.map((e) => e.$message)"
            @blur="v$.title.$touch"
            @input="v$.title.$touch">
          <section v-for="error of v$.title.$errors" :key="error.$uid">
            <section class="error-message">{{ error.$message }}</section>
          </section>
        </section>
        <label for="library_content" class="">説明</label>
        <section class="form-field">
          <textarea v-model="state.content" id="library_content" placeholder="新規ライブラリの説明"></textarea>
        </section>
        <section class="button">
          <button type="button" @click="onSubmit" :disabled="(v$.title.$errors.length === 0 && state.title !== '') ? false : true">ライブラリ追加</button>
        </section>
      </form>
    </section>
  </section>
</template>

<script lang="ts">
import { defineComponent, reactive, onMounted, inject } from 'vue';
import axios, { AxiosResponse, AxiosError } from "axios";
import { useVuelidate } from "@vuelidate/core";
import { required, helpers } from "@vuelidate/validators";
import { requiredMsg, duplicateMsg } from '@/plugin/validatorMessage';

export default defineComponent({
  name: 'LibraryRegistrationForm',
  components: {},
  setup() {
    const store = inject('library');

    let state = reactive({
      title: '',
      content: ''
    });

    const rules = {
      title: {
        required: helpers.withMessage(requiredMsg('タイトル'), required),
        duplicated: helpers.withMessage(duplicateMsg('タイトル'), function (val: String) {
          // API経由で結果を返却させるように後で修正
          const _titles = document.getElementsByClassName('title');
          if (_titles.length <= 0) { return true; }
          const _target = Array.from(_titles).find((element) => element.innerText === val);
          return !_target;
        })
      }
    };

    const v$ = useVuelidate(rules, state);

    interface UserResponse {
      data: {}
    };

    interface ErrorResponse {
      message: String,
      name: String,
      code: String
    };

    interface LibraryRequest {
      custom_user: String,
      title: String
      content: String
    };

    const uuid = window.localStorage.getItem(['UUID']);
    const username = window.localStorage.getItem(['USERNAME']);

    // あとで消す
    onMounted(() => {
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
    });

    // ----------------------- events -----------------------
    const onSubmit = async (event: HTMLButtonEvent) => {
      const requestParam: LibraryRequest = {
        custom_user: uuid,
        title: document.getElementById('library_title').value,
        content: document.getElementById('library_content').value
      };

      await axios.post('http://127.0.0.1:8000/api/libraries/', requestParam)
      .then((response: AxiosResponse) => {
        store.add(response.data);
        closeModal(event);
      })
      .catch((e: AxiosError<ErrorResponse>) => {
        console.log(`${e.message} ( ${e.name} ) code: ${e.code}`);
      });
    };

    const closeModal = (event: HTMLButtonEvent) => {
      event.preventDefault();
      const modal = document.getElementsByClassName('overlay') as HTMLCollectionOf<HTMLElement>;
      modal[0].classList.remove('visible');
      // フォーム初期化
      state.title = '';
      state.content = '';
      v$.value.$reset();
    };

    return {
      v$,
      state,
      onSubmit,
      closeModal,
    };
  }
});
</script>

<style scoped>
.overlay {
  visibility: hidden;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  transition: .17s;
  opacity: 0;
  z-index: 9999;
  background-color: rgba(0,0,0,0.4);
}
.overlay.visible {
  visibility: visible;
  opacity: 1;
}

.modal {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 60%;
  height: auto;
  background-color: white;
}

.modal .close {
  display: block;
  position: relative;
  width: 2em;
  height: 2em;
  margin-left: auto;
}
.modal .close::before, .modal .close::after {
  display: block;
  position: absolute;
  content: '';
  width: 100%;
  height: 4px;
  top: 50%;
  left: 50%;
  background-color: black;
}
.modal .close::before {
  transform: translate(-50%,-50%) rotate(45deg);
}
.modal .close::after {
  transform: translate(-50%,-50%) rotate(-45deg);
}

.modal label {
  font-size: 1.5em;
  font-weight: bold;
}
.modal label.required::after {
  position: relative;
  content: '必須';
  padding: 0.2em;
  top: -2px;
  left: 5px;
  font-size: 0.5em;
  font-weight: bold;
  border-radius: 3px;
  color: white;
  background-color: red;
}

#library_content {
  resize: none;
  width: 40em;
  height: 10em;
}

input.error {
  border-color: rgba(220,0,0,0.3);
  background-color: rgba(220,0,0,0.3);
}


.error-message {
  color: rgba(220,0,0,0.3);
}
</style>
