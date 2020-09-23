<template>
  <span class="sol-userPanel" v-on:click="showUserPanel">
    {{ Name }}
    <modal
      name="userPanel"
      :resizable="true"
      draggable=".dragHandle"
      :focusTrap="true"
      :clickToClose="false"
      classes="modalBox"
    >
      <div class="title dragHandle">
        <span>User information for {{ Name }}</span>
        <span class="sol-button" v-on:click="hideUserPanel()">x</span>
      </div>
      <div class="content">I'm a user panel, mum</div>
      <div class="alertMessage" v-if="alertMessage">{{ alertMessage }}</div>
      <div class="buttons">
        <span class="sol-button" v-on:click="clearUserPanel()">Cancel</span>
        <span class="sol-button" v-on:click="updateUser">Save</span>
      </div>
    </modal>
  </span>
</template>

<script>
export default {
  name: "UserPanel",
  data: function() {
    return {
      alertMessage: null,
      username: this.$store.state.user.username,
      password: null,
      email: this.$store.state.user.email
    };
  },
  computed: {
    Name() {
      return this.$store.state.user.username;
    }
  },
  methods: {
    showUserPanel() {
      this.$modal.show("userPanel");
    },
    hideUserPanel() {
      this.$modal.hide("userPanel");
    },
    clearUserPanel() {
      // Reset the panel to default
      this.username = this.$store.state.user.username;
      this.password = null;
      this.email = this.$store.state.user.email;

      this.$modal.hide("userPanel");
    },
    updateUser() {
      let foo = "baa";
      return foo;
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
.modalBox {
  border: @mediumBorder;
}
span.sol-userPanel {
  color: @linkcolour;
}

span.sol-userPanel div {
  color: @textColour;
}
div.title {
  width: 100%;
  text-align: center;
  background: @mediumColour;
  font-size: larger;
}
div.title span.sol-button {
  float: right;
  font-size: small;
  margin-top: @smallPadding;
}
div.alertMessage {
  text-align: center;
  color: @alertColour;
  font-weight: bold;
}
div.buttons {
  text-align: center;
}
</style>
