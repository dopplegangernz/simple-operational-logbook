<template>
  <div class="footer">
    <span>searchstring = {{ searchString }} </span>
    <span>selectedDate = {{ selectedDate }} </span>
    <span>activeGroup = {{ activeGroup }} </span>
  </div>
</template>

<script>
export default {
  name: "Footer",
  computed: {
    searchString() {
      return this.$store.state.searchString;
    },
    selectedDate() {
      return this.$store.state.selectedDate;
    },
    activeGroup() {
      return this.$store.state.activeGroup;
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
div.footer {
  border-top: solid 1px rgb(#aaa);
}
</style>
