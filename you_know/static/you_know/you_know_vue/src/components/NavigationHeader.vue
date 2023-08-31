<template>
  <header>
    <nav class="menu-wrap">
      <section class="flex-contents">
        <section class="service-icon">サービスアイコン</section>
        <section class="menu">
          <ul class="menu-item">
            <li><a class="sp-char-mini" href="/you_know/">Profile</a></li>
            <li><a class="sp-char-mini" href="/you_know/library/">登録済み<br>ライブラリ</a></li>
          </ul>
        </section>
      </section>
    </nav>
  </header>
</template>

<script setup></script>

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
