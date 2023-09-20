import { createRouter, createWebHistory, RouteRecordRaw  } from 'vue-router';

const routes: Array<RouteRecordRaw> = [
  { path: '/', name: 'top', component: () => import('../components/views/Top.vue') },
  //{ path: '/login', name: 'login', component: () => import('../components/views/Login.vue') },
  { path: '/:username/library', name: 'library', component: () => import('../components/views/Libraries.vue') },
  { path: '/category', name: 'category', component: () => import('../components/views/Categories.vue') },
  { path: '/keyword', name: 'keyword', component: () => import('../components/views/Keywords.vue') },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
