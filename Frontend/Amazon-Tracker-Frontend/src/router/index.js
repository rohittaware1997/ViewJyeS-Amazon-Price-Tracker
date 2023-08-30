import { route } from 'quasar/wrappers'
import { createRouter, createMemoryHistory, createWebHistory, createWebHashHistory } from 'vue-router'
import routes from './routes'
import { getAuth, onAuthStateChanged } from "firebase/auth";
import {useStore} from "vuex";
import axios from "axios";


// get the current user's email address

/*
 * If not building with SSR mode, you can
 * directly export the Router instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Router instance.
 */

export default route(function (/* { store, ssrContext } */) {
  const createHistory = process.env.SERVER
    ? createMemoryHistory
    : (process.env.VUE_ROUTER_MODE === 'history' ? createWebHistory : createWebHashHistory)

  const Router = createRouter({
    scrollBehavior: () => ({ left: 0, top: 0 }),
    routes,

    // Leave this as is and make changes in quasar.conf.js instead!
    // quasar.conf.js -> build -> vueRouterMode
    // quasar.conf.js -> build -> publicPath
    history: createHistory(process.env.MODE === 'ssr' ? void 0 : process.env.VUE_ROUTER_BASE)
  })
  const getCurrentUser = () => {
    return new Promise((resolve, reject) => {
      const removeListener = onAuthStateChanged(
        getAuth(),
        (user) => {
          removeListener()
          resolve(user)
        },
        reject
      );
    });
  };



  Router.beforeEach(async (to, from, next)=>{
    if (to.matched.some((record) => record.meta.requiresAuth)) {
      if (await getCurrentUser()){
        console.log("inside current user")
        next();
      } else {
        next("/");
        alert("You dont have access");
      }
    }else{
      next();
    }
  });
  return Router
})
