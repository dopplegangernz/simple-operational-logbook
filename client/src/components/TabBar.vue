<template>
  <div class="tabBar">
    <span
      v-for="group in Groups"
      :key="group"
      v-bind:class="{
        active:
          (group === 'All' && ActiveGroup === null) || group === ActiveGroup,
      }"
      v-on:click="selectGroup(group)"
      >{{ group }}</span
    >
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
    },
  },
  methods: {
    ...mapMutations(["selectGroup"]),
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
  background: rgb(#ddd);
  margin-left: 1em;
  padding-left: 0.5em;
  padding-right: 0.5em;
  border-top-left-radius: 0.5em;
  border-top-right-radius: 0.5em;
}
span:hover {
  background: rgb(#fff);
}
span.active {
  background: rgb(#888);
}
span.active:hover {
  background: rgb(#000);
  color: rgb(#fff);
}
</style>
