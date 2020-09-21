import Vue from "vue";
import App from "./App.vue";
import VCalendar from "v-calendar";
import Vuex from "vuex";

Vue.config.productionTip = false;

Vue.use(VCalendar, {
  componentPrefix: "vc",
});

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    user: {
      username: null,
      email: null,
      group: null,
      id: null,
      authKey: null,
      admin: false,
    },
    date: null,
    searchString: null,
    entries: [],
    groups: ["All", "A tab", "Another tab", "Yet another tab"],
  },
  mutations: {},
});

new Vue({
  store: store,
  render: (h) => h(App),
}).$mount("#app");
