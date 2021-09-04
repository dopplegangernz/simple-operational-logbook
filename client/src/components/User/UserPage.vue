<template>
  <div id="index">
    <Header pageName="User Information"></Header>
    <Footer />
  </div>
</template>

<script>
import Footer from "../Shared/Footer.vue";
import Header from "../Shared/Header.vue";

export default {
  name: "UserPage",
  components: {
    Footer,
    Header
  },
 
};
</script>

<style lang="less">

</style>
