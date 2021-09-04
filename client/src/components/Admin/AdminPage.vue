<template>
  <div id="index">
    <Header 
      pageName="Administration"
      :tabSet="tabSet"
      :activeTab="selectedTab" 
      v-on:tabSelected="selectTab"></Header>
      <AdminPanel :activeTab="selectedTab"/>
    <Footer />
  </div>
</template>

<script>
import Footer from "../Shared/Footer.vue";
import Header from "../Shared/Header.vue";
import AdminPanel from "./AdminPanel.vue";

export default {
  name: "AdminPage",
  components: {
    Footer,
    Header,
    AdminPanel
  },
  data: function(){
    return {
      "selectedTab": "Users",
      "tabSet":["Users", "Add User", "Groups", "Application"]
    }
  },
  methods: {
    selectTab(tabName){
      this.selectedTab = tabName;

    }
  },
 
};
</script>

<style lang="less">

</style>
