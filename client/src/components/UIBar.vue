<template>
  <div class="uiBar">
    <div class="search">search</div>
    <div class="login">login</div>
  </div>
</template>

<script>
export default {
  name: "UIBar",
  props: {}
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
div.uiBar {
  border-bottom: solid 1px rgb(#aaa);
  overflow: hidden;
}
div.search {
  float: left;
  margin-left: 2em;
  display: inline-block;
}
div.login {
  float: right;
  display: inline-block;
  margin-right: 2em;
}
</style>
