<template>
  <div class="tabBar">
    <span v-for="group in Groups" :key="group">{{ group }}</span>
  </div>
</template>

<script>
export default {
  name: "TabBar",
  props: {
    Groups: Array,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
div.tabBar {
  padding-top: 6px;
  border-bottom: solid 1px rgb(#aaa);
  width: 100%;
  background: rgb(#888);
}
span {
  border: solid 1px rgb(#aaa);
  background: rgb(#fff);
  margin-left: 1em;
  padding-left: 0.5em;
  padding-right: 0.5em;
  border-top-left-radius: 0.5em;
  border-top-right-radius: 0.5em;
}
</style>
