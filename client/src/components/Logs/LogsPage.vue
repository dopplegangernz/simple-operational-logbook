<template>
  <div id="index">
    <Header 
      pageName="Log Entries" 
      :tabSet="tabSet"
      :activeTab="activeTab" 
      v-on:tabSelected="selectTab">
      <template v-slot:right> 
        <DatePicker/>
      </template> 
      <template v-slot:UIComponents> 
        <TextSearch v-on:searchCleared = "searchInputCleared" v-on:searchSubmitted="searchByString"/>
      </template>
    </Header>
    <LogArea />
    <Footer />
  </div>
</template>

<script>
import Footer from "../Shared/Footer.vue";
import Header from "../Shared/Header.vue";
import LogArea from "./LogArea.vue";
import DatePicker from "../Shared/DatePicker.vue";
import TextSearch from "../Shared/TextSearch.vue"

export default {
  name: "LogsPage",
  components: {
    Footer,
    Header,
    LogArea,
    DatePicker,
    TextSearch
  },
  computed:{
    tabSet() {
      return this.$store.state.groups.map(group => group.name);
    },
    activeTab() {
      return this.$store.state.activeGroup;
    },
  },
  methods: {
    selectTab(tabName){
      this.$store
        .commit("selectGroup", tabName);
;    },
    searchInputCleared() {
      this.$store
        .dispatch("fetchEntriesByDate", this.$store.state.selectedDate)
        .catch(function(reason) {
          alert(reason);
        });
    },
    searchByString(searchString) {
      this.$store
        .dispatch("fetchEntriesBySearchString", searchString)
        .catch(function(message) {
          alert(message);
        });
    }
  },
};
</script>

<style lang="less">
#client {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: @textColour;
}
span.sol-button {
  display: inline-block;
  margin-right: 2em;
  margin-left: 2em;
  padding-left: 1em;
  padding-right: 1em;
  background: @lightColour;
  border: solid;
  border-radius: 0.5em;
  border: @mediumBorder;
  cursor: pointer;
}
span.sol-button:hover {
  border: @lightBorder;
  background: @veryLightColour;
}
div.modalBox {
  cursor: default;
}
.linkText {
  color: @linkcolour;
  cursor: pointer;
  text-decoration: underline;
}
div.tabBar {
  padding-top: @mediumPadding;
  border-bottom: @mediumBorder;
  width: 100%;
  background: @darkColour;
}
span.tab {
  border: @mediumBorder;
  background: @mediumColour;
  margin-left: 1em;
  padding-left: 0.5em;
  padding-right: 0.5em;
  border-top-left-radius: 0.5em;
  border-top-right-radius: 0.5em;
  cursor: pointer;
}
span.tab:hover {
  background: @backgroundColour;
}
span.tab.active {
  border: @veryDarkBorder;
  background: @darkColour;
}
span.tab.active:hover {
  background: @veryDarkColour;
  color: @backgroundColour;
}
</style>
