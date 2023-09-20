<template>
  <!--
  <h2>login</h2>
  <section class="login-form">
    <form action="">
      <section class="error-message hidden">メールアドレスもしくはパスワードに誤りがあります</section>
      <section class="form-field">
        <input type="email" name="email" id="email" placeholder="メールアドレス"
          v-model="state.email"
          :class="[v$.email.$errors.length >= 1 ? 'form-input error' : 'form-input']"
          :error-messages="v$.email.$errors.map((e) => e.$message)"
          @blur="v$.email.$touch">
        <section v-for="error of v$.email.$errors" :key="error.$uid">
          <section class="error-message">{{ error.$message }}</section>
        </section>
      </section>
      <section class="form-field">
        <input type="password" name="password" id="password" placeholder="パスワード"
          v-model="state.password"
          :class="[v$.password.$errors.length >= 1 ? 'form-input error' : 'form-input']"
          :error-messages="v$.password.$errors.map((e) => e.$message)"
          @blur="v$.password.$touch">
        <section v-for="error of v$.password.$errors" :key="error.$uid">
          <section class="error-message">{{ error.$message }}</section>
        </section>
      </section>
      <section class="">
        <button type="button"
          @click="login"
          :disabled="(v$.email.$errors.length === 0 && state.email !== '' && v$.password.$errors.length === 0 && state.password !== '') ? false : true">
          ログイン
        </button>
      </section>
    </form>
  </section>
  -->
  <section>
    <button @click="login">Log in</button>
  </section>
</template>

<script lang="ts">
import { defineComponent, reactive } from 'vue'
import { useAuth0 } from '@auth0/auth0-vue';
/*
import { useVuelidate } from "@vuelidate/core";
import axios, { AxiosResponse, AxiosError } from "axios";
import Cookies from 'js-cookie';
import { required, email, helpers } from "@vuelidate/validators";
import { requiredMsg, emailFormat } from '@/plugin/validatorMessage';
import router from '@/router/index';
*/

export default defineComponent({
  name: 'Login',
  components: {},
  setup() {
    const auth0 = useAuth0();
    /*
    const state = reactive({
      email: '',
      password: ''
    });

    interface LoginRequest {
      email: String,
      password: String
    };

    const rules = {
      email: {
        required: helpers.withMessage(requiredMsg('メールアドレス'), required),
        email: helpers.withMessage(emailFormat(), email)
      },
      password: {
        required: helpers.withMessage(requiredMsg('パスワード'), required),
      }
    };

    const v$ = useVuelidate(rules, state);

    const login = (event: HTMLButtonEvent) => {
      event.preventDefault();
      const requestParam: LoginRequest = {
        email: document.getElementById('email').value,
        password: document.getElementById('password').value
      };
      axios.post('http://127.0.0.1:8000/api/token/', requestParam).then(res => {
        console.log(res.headers['x-auth-token']);
        console.log(res.request);
        const jsonData = JSON.stringify(res.data.access);
        Cookies.set('token', jsonData, { expires: 30 });
        router.push('/');
      }).catch((e: AxiosError<ErrorResponse>) => {
        console.log(`${e.message} ( ${e.name} ) code: ${e.code}`);
      });
    };

    return {
      v$,
      state,
      login,
    };
    */
    return {
      login: () => {
        auth0.loginWithRedirect();
      }
    };
  },
})
</script>

<style scoped>
/*
.form-field {
  padding: 1.2em 0;
}
.form-input {
  padding: 0 0.5em;
  border: none;
  outline: none;
  padding-bottom: 0.4em;
  border-bottom: 1px solid #c2c2c2;
  background: rgb(240, 242, 242);
}
.form-input.error {
  border-color: rgba(200, 0, 0, 0.95);
}
.form-input.error::placeholder {
  color: rgba(200, 0, 0, 0.95);
}


.error-message {
  color: rgba(200, 0, 0, 0.95);
}
*/
</style>
