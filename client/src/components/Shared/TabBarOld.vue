<template>
  <div class="tabBar">
    <span
      class="tab"
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
</style>
