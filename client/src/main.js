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
    entries: [
      {
        id: "21341234123",
        subject: "some subject",
        timestamp: new Date("2020-09-22 09:20:00"),
        text: "words words words",
        author_name: "john smith",
        group_name: "Operations",
      },
      {
        id: "23453",
        subject: "some subject",
        timestamp: new Date("2020-09-22 09:20:00"),
        text: "different words",
        author_name: "john Jones",
        group_name: "Operations",
      },
      {
        id: "2349y",
        subject: "some subject",
        timestamp: new Date("2020-09-22 09:20:00"),
        text: "an anecdote about fish",
        author_name: "Steve smith",
        group_name: "Design",
      },
    ],
    groups: [],
  },
  mutations: vuexMutations,
  actions: vuexActions,
});

new Vue({
  store: store,
  render: (h) => h(App),
}).$mount("#app");
