<template>
  <div class="tabBar">
    <span
      class="tab"
      v-for="tabName in tabSet"
      :key="tabName"
      v-bind:class="{
        active: tabName === selectedTab,
      }"
      v-on:click="selectTab(tabName)"
    >{{ tabName }}</span>
  </div>
</template>

<script>
export default {
  name: "TabBar",
  props:{
    "tabSet":Array,
    "activeTab": String
  },
  emits: ['tabSelected'],
  data: function(){
    return {
      "selectedTab": this.activeTab
    }
  },
  methods: {
    selectTab(tabName){
      this.selectedTab = tabName;
      this.$emit("tabSelected", tabName)
    }
  },
};
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
</style>
