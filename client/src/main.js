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
    appName: "Simple Operational Logbook",
    logo: "logo.png",
    user: {
      username: null,
      email: null,
      group: null,
      id: null,
      authKey: null,
      admin: false,
    },
    activeGroup: null,
    date: null,
    searchString: "steve",
    entries: [],
    groups: ["All", "Operations", "Design", "OSP"],
  },
  mutations: {
    setSearchString(state, searchString) {
      state.searchString = searchString;
    },
    selectGroup(state, group) {
      state.activeGroup = group;
    },
  },
});

new Vue({
  store: store,
  render: (h) => h(App),
}).$mount("#app");
