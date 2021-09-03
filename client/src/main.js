import Vue from "vue";
import VueRouter from "vue-router";
import LogsPage from "./components/Logs/LogsPage.vue";
import AdminPage from "./components/Admin/AdminPage.vue";
import UserPage from "./components/User/UserPage.vue"
import VCalendar from "v-calendar";
import Vuex from "vuex";
import VModal from "vue-js-modal";
import Loading from "vue-loading-overlay";

const vuexMutations = require("./vuex/mutations.js");
const vuexActions = require("./vuex/actions.js");

Vue.config.productionTip = false;

Vue.use(VueRouter);
Vue.use(VCalendar);
Vue.use(Vuex);
Vue.use(VModal);
Vue.use(Loading);

const store = new Vuex.Store({
  state: {
    appName: "Simple Operational Logbook",
    logo: "sol-logo.svg",
    user: {
      username: null,
      email: null,
      group: null,
      id: null,
      authKey: null,
      isAdmin: null
    },
    selectedDate: new Date(),
    activeGroup: "All",
    date: null,
    searchString: null,
    entries: [],
    groups: []
  },
  mutations: vuexMutations,
  actions: vuexActions
});
// Define routes

const routes = [
  { 
    path: "/", 
    name: "Root",
    redirect: "/logs" 
  },
  { 
    path: "/logs", 
    name: "Logs",
    component: LogsPage 
  },
  { 
    path: "/admin", 
    name: "Admin",
    component: AdminPage 
  },
  {
    path: "/user/:name",
    name: "Users",
    component: UserPage
  }
];

const Router = new VueRouter({ 
  routes: routes 
});

new Vue({
  store: store,
  router: Router,

}).$mount("#app");
