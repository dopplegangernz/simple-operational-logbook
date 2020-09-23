import Vue from "vue";
import App from "./App.vue";
import VCalendar from "v-calendar";
import Vuex from "vuex";
import VModal from "vue-js-modal";
import Loading from "vue-loading-overlay";

const vuexMutations = require("./vuex/mutations.js");
const vuexActions = require("./vuex/actions.js");

Vue.config.productionTip = false;

Vue.use(VCalendar);
Vue.use(Vuex);
Vue.use(VModal);
Vue.use(Loading);

const store = new Vuex.Store({
  state: {
    appName: "Simple Operational Logbook",
    logo: "logo.png",
    user: {
      username: null,
      email: null,
      group: null,
      id: null,
      authKey: null,
      isAdmin: null,
    },
    selectedDate: new Date(),
    activeGroup: "All",
    date: null,
    searchString: null,
    entries: [],
    groups: [],
  },
  mutations: vuexMutations,
  actions: vuexActions,
});

new Vue({
  store: store,
  render: (h) => h(App),
}).$mount("#app");
