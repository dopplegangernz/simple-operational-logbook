<template>
  <div class="logArea">
    <h1>Logs go here</h1>
    <p>searchstring = {{ searchString }}</p>
    <p>selectedDate = {{ selectedDate }}</p>
  </div>
</template>

<script>
export default {
  name: "LogArea",
  computed: {
    searchString() {
      return this.$store.state.searchString;
    },
    selectedDate() {
      return this.$store.state.selectedDate;
    },
  },

  props: {
    Entries: Array,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less"></style>
