<template>
  <nav class="menu-wrap">
    <section class="flex-contents">
      <section class="service-icon">アイコンとか</section>
      <ul class="menu">
        <li><a class="sp-char-mini" href="/you_know/">Profile</a></li>
        <li><a class="sp-char-mini" href="/you_know/library/">登録済み<br>ライブラリ</a></li>
      </ul>
    </section>
  </nav>
</template>

<script setup></script>

<style scoped>
nav {
  position: fixed;
  width: 100%;
  top: 0;
  z-index: 1000;
  justify-content: space-between;
  background-color: black;
  color: white;
}

.menu-wrap {
  padding: 0.2em;
}
ul.menu li {
  padding: 0.5em 0.1em;
  font-size: 1.0rem;
  font-weight: 700;
}
</style>
