<template>
  <div class="tabBar">
    <span
      v-for="group in Groups"
      :key="group.id"
      v-bind:class="{
        active: group.name === ActiveGroup,
      }"
      v-on:click="selectGroup(group.name)"
    >{{ group.name }}</span>
  </div>
</template>

<script>
import { mapMutations } from "vuex";
export default {
  name: "TabBar",
  computed: {
    ActiveGroup() {
      return this.$store.state.activeGroup;
    },
    Groups() {
      return this.$store.state.groups;
    }
  },
  methods: {
    ...mapMutations(["selectGroup"])
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
div.tabBar {
  padding-top: @mediumPadding;
  border-bottom: @mediumBorder;
  width: 100%;
  background: @darkColour;
}
span {
  border: @mediumBorder;
  background: @mediumColour;
  margin-left: 1em;
  padding-left: 0.5em;
  padding-right: 0.5em;
  border-top-left-radius: 0.5em;
  border-top-right-radius: 0.5em;
  cursor: pointer;
}
span:hover {
  background: @backgroundColour;
}
span.active {
  border: @veryDarkBorder;
  background: @darkColour;
}
span.active:hover {
  background: @veryDarkColour;
  color: @backgroundColour;
}
</style>
