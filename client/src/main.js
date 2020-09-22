import Vue from "vue";
import App from "./App.vue";
import VCalendar from "v-calendar";
import Vuex from "vuex";
import VModal from "vue-js-modal";

Vue.config.productionTip = false;

Vue.use(VCalendar, {
  "disabled-dates": {},
});

Vue.use(Vuex);
Vue.use(VModal);

const store = new Vuex.Store({
  state: {
    appName: "Simple Operational Logbook",
    logo: "logo.png",
    user: {
      username: null,
      email: null,
      group: "Design",
      id: null,
      authKey: null,
      admin: false,
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
    groups: ["All", "Operations", "Design", "OSP"],
  },
  mutations: {
    setSearchString(state, searchString) {
      state.searchString = searchString;
    },
    setSelectedDate(state, selectedDate) {
      state.selectedDate = selectedDate;
    },
    selectGroup(state, group) {
      state.activeGroup = group;
    },
    saveEntry(state, newEntry) {
      state.entries.push(newEntry);
    },
  },
  actions: {
    saveEntry(context, newEntry) {
      newEntry.timestamp = new Date();
      newEntry.author_name = context.state.user.username;

      context.commit("saveEntry", newEntry);
    },
    processLogin(context, loginDetails) {
      return { context, loginDetails };
    },
  },
});

new Vue({
  store: store,
  render: (h) => h(App),
}).$mount("#app");
