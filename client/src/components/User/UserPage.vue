<template>
  <div id="index">
    <Header pageName="User Information"></Header>
    <UserPanel />
    <Footer />
  </div>
</template>

<script>
import Footer from "../Shared/Footer.vue";
import UserPanel from "./UserPanel.vue";
import Header from "../Shared/Header.vue";

export default {
  name: "UserPage",
  components: {
    Footer,
    Header,
    UserPanel
  },
 
};
</script>

<style lang="less">

</style>
