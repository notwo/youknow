interface HTMLEvent<T extends EventTarget> extends Event {
  target: T;
}

import Vue from "vue";
export default Vue.extend({
  methods: {
    onClick(event: { target: HTMLButtonElement }) {
      console.log(event.target.parentElement?.getElementsByTagName("input"));
    },
  },
});

import { createApp } from 'vue';
import App from './App.vue';
const app = createApp(App);
app.mount('#app');
