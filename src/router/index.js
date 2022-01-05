import { createRouter, createWebHistory } from 'vue-router'
import store from "@/store"
import Login from "@/views/Login.vue"
import Home from "@/views/Home.vue"

const routes = [
  {
    path: "/",
    name: "home",
    component: Home
  },
  {
    path: "/login",
    name: "login",
    component: Login
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  let toLogin = to.name === "login";
  let fromLogin = from.name === "login";
  if (!store.getters.isAuthenticated) {
    if (fromLogin) {
      return;
    }
    if (!toLogin) {
      next({name: 'login'});
      return;
    }
    next();
    return;
  }
  if (toLogin) {
    next({name: 'home'})
    return;
  }

  next();
})

export default router
