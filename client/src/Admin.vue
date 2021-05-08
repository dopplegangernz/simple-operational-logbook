<template>
  <div id="admin">
    <Header />
    <LogArea />
    <Footer />
  </div>
</template>

<script>
import Header from "./components/Header.vue";

export default {
  name: "Almin",
  components: {
    Header,
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
