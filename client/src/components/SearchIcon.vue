<template>
  <svg
    v-on:click="search"
    class="magnifyingGlass"
    width="18"
    height="18"
    xmlns="http://www.w3.org/2000/svg"
  >
    <g>
      <title>Magnifying glass</title>
      <ellipse ry="6" rx="6" cy="8" cx="8" stroke-width="2" fill="none" />
      <line stroke-linecap="round" y2="18" x2="18" y1="14" x1="14" stroke-width="3" />
    </g>
  </svg>
</template>

<script>
export default {
  name: "SearchIcon",
  props: ["action", "payload"],
  methods: {
    search() {
      this.$store.dispatch(this.action, this.payload).catch(function(message) {
        alert(message);
      });
      if (this.payload instanceof Date) {
        this.$store.commit("setSelectedDate", this.payload);
      }
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
.magnifyingGlass {
  stroke: @darkColour;
  position: absolute;
  margin-left: @mediumPadding;
  cursor: pointer;
}
</style>
