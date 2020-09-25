<template>
  <div class="uiBar">
    <div class="search">
      <label for="searchInput">Search:</label>
      <span class="pseudoInput">
        <input v-model="SearchInputValue" class="hasX" id="searchInput" type="text" />
        <svg
          v-on:click="clearSearchInput"
          width="15px"
          height="15px"
          viewBox="-5 -5 30 30"
          version="1.1"
          xmlns="http://www.w3.org/2000/svg"
          xmlns:xlink="http://www.w3.org/1999/xlink"
          xml:space="preserve"
          xmlns:serif="http://www.serif.com/"
        >
          <path d="M1,1L19,19" />
          <path d="M1,19L19,1" />
        </svg>
      </span>
      <span class="sol-button" v-on:click="searchByString(SearchInputValue)">Go</span>
    </div>
    <span class="buttons">
      <AdminPanel v-if="isAdmin" />
      <UserPanel v-if="isLoggedIn" />
      <LoginDialog />
    </span>
  </div>
</template>

<script>
import AdminPanel from "./AdminPanel.vue";
import UserPanel from "./UserPanel.vue";
import LoginDialog from "./LoginDialog.vue";

export default {
  name: "UIBar",
  components: {
    UserPanel,
    LoginDialog,
    AdminPanel
  },
  data: function() {
    return {
      SearchInputValue: null
    };
  },
  computed: {
    isAdmin() {
      return this.$store.state.user.isAdmin;
    },
    isLoggedIn() {
      return this.$store.state.user.username !== null;
    }
  },
  methods: {
    clearSearchInput() {
      this.SearchInputValue = null;
      this.$store
        .dispatch("fetchEntriesByDate", this.$store.state.selectedDate)
        .catch(function(reason) {
          alert(reason);
        });
    },
    searchByString(searchString) {
      this.$store
        .dispatch("fetchEntriesBySearchString", searchString)
        .catch(function(message) {
          alert(message);
        });
    }
  }
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
.pseudoInput {
  padding-left: 0.5em;
  margin-left: 0.5em;
  height: 1em;
  width: 20em;
  border-radius: 0.5em;
  border: solid;
  border-color: @lightColour;
  border-width: 1px;
  font-size: large;
  cursor: text;
}
.pseudoInput input {
  border: none;
  padding-top: @smallPadding;
  padding-bottom: @smallPadding;
}
.pseudoInput input:focus {
  outline: none;
}
.pseudoInput svg {
  vertical-align: middle;
  padding-right: @mediumPadding;
  padding-left: @mediumPadding;
  stroke-linecap: square;
  stroke-linejoin: round;
  padding-top: @smallPadding;
  padding-bottom: @smallPadding;
  cursor: pointer;
}
.pseudoInput svg path {
  fill: none;
  stroke: @darkColour;
  stroke-width: 3px;
}
div.search span {
  font-size: large;
}
span.buttons {
  float: right;
}
</style>
