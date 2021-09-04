<template>
  <div class="uiBar">
    <slot name="UIComponents" />
    <span class="buttons">
      <span class="sol-button" v-if="this.$route.name !== 'Logs'">
        <router-link to="/logs" >
          Logs Panel
        </router-link>
      </span>
      <span class="sol-button" v-if="isAdmin && this.$route.name !== 'Admin'">
        <router-link to="/admin"> 
          Admin Panel
        </router-link>
      </span >
      <span class="sol-button" v-if="isLoggedIn" >
        <router-link :to="'/user/'+Name">
          {{ Name }}
        </router-link>
      </span>
      <LoginDialog />
    </span>
  </div>
</template>

<script>
import LoginDialog from "../Shared/LoginDialog.vue";

export default {
  name: "UIBar",
  components: {
    LoginDialog
  },
  computed: {
    isAdmin() {
      return this.$store.state.user.isAdmin;
    },
    isLoggedIn() {
      return this.$store.state.user.username !== null;
    },
    Name() {
      return this.$store.state.user.username;
    }
  },
  methods: {
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
