<template>
  <div id="app">
    <Header />
    <LogArea />
    <Footer />
  </div>
</template>

<script>
import Footer from "./components/Footer.vue";
import Header from "./components/Header.vue";
import LogArea from "./components/LogArea.vue";

export default {
  name: "App",
  components: {
    Footer,
    Header,
    LogArea
  },
  mounted: function() {
    this.$store.commit("defaultUserDetails");
    this.$store.dispatch("fetchGroups").catch(function(reason) {
      alert(reason);
    });
    this.$store
      .dispatch("fetchEntriesByDate", new Date())
      .catch(function(reason) {
        alert(reason);
      });
  }
};
</script>

<style lang="less">
#app {
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
.linkText {
  color: @linkcolour;
  cursor: pointer;
  text-decoration: underline;
}
</style>
