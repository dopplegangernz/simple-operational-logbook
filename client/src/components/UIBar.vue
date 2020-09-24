<template>
  <div class="uiBar">
    <div class="search">
      <label for="searchInput">Search:</label>
      <input v-model="SearchInputValue" id="searchInput" type="text" />
      <span class="sol-button" v-on:click="searchByString(SearchInputValue)"
        >Go</span
      >
    </div>
    <span class="buttons">
      <UserPanel v-if="isLoggedIn" />
      <LoginDialog />
    </span>
  </div>
</template>

<script>
import UserPanel from "./UserPanel.vue";
import LoginDialog from "./LoginDialog.vue";

export default {
  name: "UIBar",
  components: {
    UserPanel,
    LoginDialog,
  },
  data: function() {
    return {
      SearchInputValue: null,
    };
  },
  computed: {
    isAdmin() {
      return this.$store.state.user.isAdmin;
    },
    isLoggedIn() {
      return this.$store.state.user.username !== null;
    },
  },
  methods: {
    searchByString(searchString) {
      this.$store
        .dispatch("fetchEntriesBySearchString", searchString)
        .catch(function(message) {
          alert(message);
        });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
div.uiBar {
  overflow: hidden;
  padding-top: 6px;
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
  border-color: @lightColour;
  border-width: 1px;
  font-size: large;
}
div.search span {
  font-size: large;
}
span.buttons {
  float: right;
}
</style>
