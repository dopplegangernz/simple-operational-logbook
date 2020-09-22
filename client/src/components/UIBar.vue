<template>
  <div class="uiBar">
    <div class="search">
      <label for="searchInput"> Search:</label>
      <input v-model="SearchInputValue" id="searchInput" type="text" />
      <span class="sol-button" v-on:click="setSearchString(SearchInputValue)"
        >Go</span
      >
    </div>
    <span class="login sol-button">{{ Name }}</span>
  </div>
</template>

<script>
import { mapMutations } from "vuex";
export default {
  name: "UIBar",
  data: function() {
    return {
      SearchInputValue: this.$store.state.searchString,
    };
  },
  computed: {
    Name() {
      const name = this.$store.state.user.username;

      if (name === null) {
        return "Log in";
      } else {
        return name;
      }
    },
  },
  methods: {
    ...mapMutations(["setSearchString"]),
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
div.uiBar {
  border-bottom: solid 1px rgb(#aaa);
  overflow: hidden;
  padding-top: 6px;
  padding-bottom: 6px;
}
div.search {
  float: left;
  margin-left: 2em;
}
div.search label {
  font-size: large;
}
#searchInput {
  padding-left: 0.5em;
  margin-left: 0.5em;
  height: 1em;
  width: 20em;
  border-radius: 0.5em;
  border: solid;
  border-color: rgb(#aaa);
  border-width: 1px;
  font-size: large;
}
div.search span {
  font-size: large;
}
span.login {
  float: right;
}
</style>
