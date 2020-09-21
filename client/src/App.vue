<template>
  <div id="app">
    <Header name="Simple operational logbook" Logo="logo.png" />
    <TabBar :v-bind:Groups="groups" />
    <UIBar />
    <LogArea />
    <Footer />
  </div>
</template>

<script>
import Footer from "./components/Footer.vue";
import Header from "./components/Header.vue";
import LogArea from "./components/LogArea.vue";
import TabBar from "./components/TabBar.vue";
import UIBar from "./components/UIBar.vue";

export default {
  name: "App",
  components: {
    Footer,
    Header,
    LogArea,
    TabBar,
    UIBar,
  },
};
</script>

<style lang="less">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
