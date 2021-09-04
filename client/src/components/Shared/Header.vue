<template>
  <div class="header" id="sol-header">
    <slot name="left"><Logo/></slot>
    <div class="restOfHeader">
       <div class="table">
        <div class="row">
          <div class="title">
            <h1>{{ Name }}</h1>
            <h2>{{pageName}}</h2>
          </div>
        </div>
      </div>
      <TabBar :tabSet="tabSet" :activeTab="activeTab" v-on:tabSelected="bubbleSelection"/>
      <UIBar > <template v-slot:UIComponents><slot name="UIComponents" /> </template></UIBar>
    </div>
    <slot name="right"><Logo/></slot>
  </div>
</template>

<script>
import TabBar from "./TabBar.vue";
import UIBar from "./UIBar.vue";
import Logo from "./Logo.vue";

export default {
  name: "Header",
  props: {
    pageName:{
      type: String,
      default: ""
    },
    tabSet: Array,
    activeTab: String
  },
  methods: {
    bubbleSelection(tabName){
      this.$emit("tabSelected", tabName)
    }
  },
  components: {
    TabBar,
    UIBar,
    Logo
  },
  computed: {
    Name() {
      return this.$store.state.appName;
    },
}
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
div.header {
  width: 100%;
  display: block;
  overflow: hidden;
  border-bottom: @mediumBorder;
}
div.logo {
  display: inline-block;
  margin-left: 1em;
  width: 250px;
  padding-right: 6px;
  border-right: @mediumBorder;
}
div.restOfHeader {
  display: inline-block;
  width: calc(100vw - 570px);
}
div.table {
  display: table;
  width: 100%;
}
div.row {
  display: table-row;
  width: 100%;
}

div.title {
  display: table-cell;
  text-align: center;
}
div.calendar {
  width: 260px;
  display: inline-block;
  vertical-align: bottom;
}
</style>
<style lang="less">
div.calendar input {
  width: 14em;
}
div.calendar .vc-text-sm {
  font-size: 12px;
}
</style>
