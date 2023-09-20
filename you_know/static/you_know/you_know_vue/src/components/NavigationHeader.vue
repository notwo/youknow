<template>
  <header>
    <nav class="menu-wrap">
      <section class="flex-contents">
        <section class="service-icon">サービスアイコン</section>
        <section class="menu">
          <ul class="menu-item">
            <li v-if="!auth0.isAuthenticated.value"><button @click="login">ログイン</button></li>
            <li v-if="auth0.isAuthenticated.value"><a class="sp-char-mini" href="/">Profile</a></li>
            <li v-if="auth0.isAuthenticated.value"><a class="sp-char-mini" :href="'/' + auth0.user.value?.nickname + '/library/'">登録済み<br>ライブラリ</a></li>
            <li v-if="auth0.isAuthenticated.value"><button @click="logout">ログアウト</button></li>
          </ul>
        </section>
      </section>
    </nav>
  </header>
</template>

<script lang="ts">
import { defineComponent, inject } from 'vue'
import { useAuth0 } from '@auth0/auth0-vue';

export default defineComponent({
  name: 'Login',
  components: {},
  setup() {
    const store = inject('library');
    if (store.getUser()) { console.log('aho') }

    const auth0 = useAuth0();
    const { logout } = useAuth0();

    store.setUser(auth0);

    return {
      auth0,
      login: () => {
        auth0.loginWithRedirect();
      },
      logout: () => {
        logout({ logoutParams: { returnTo: window.location.origin } });
      }
    };
  }
});
</script>

<style scoped>
header.fixed {
  position: fixed;
}

nav {
  width: 100%;
  z-index: 10000;
  justify-content: space-between;
  background-color: black;
  color: white;
}

.menu-wrap {
  padding: 0.2em;
}
.menu {
  display: flex;
}
.menu li {
  padding: 0.5em 2em;
  font-size: 1.0rem;
  font-weight: 700;
}
.menu-item {
  display: flex;
  justify-content: center;
}

.search-wrap {
  position: relative;
  display: flex;
}
.searchbox {
  position: absolute;
  top: 30%;
}
</style>
