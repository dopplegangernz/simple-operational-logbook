<template>
  <span class="sol-button sol-loginDialog" v-on:click="showLoginDialog">
    Log in
    <modal
      name="loginDialog"
      :resizable="true"
      draggable=".dragHandle"
      :focusTrap="true"
      :clickToClose="false"
      classes="modalBox"
      width="300px"
      height="160px"
    >
      <div class="title dragHandle">
        <span>Login</span>
        <span class="sol-button" v-on:click="hideLoginDialog">x</span>
      </div>
      <div class="loginContent"></div>
      <table>
        <tr>
          <th>Email address:</th>
          <td>
            <input type="text" v-model="email" />
          </td>
        </tr>
        <tr>
          <th>Password:</th>
          <td>
            <input type="password" v-model="password" />
          </td>
        </tr>
      </table>

      <div class="alertMessage" v-if="alertMessage">{{ alertMessage }}</div>
      <div class="buttons">
        <span class="sol-button" v-on:click="clearLoginDialog">Cancel</span>
        <span class="sol-button" v-on:click="processLogin">Log in</span>
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
      email: null,
      password: null
    };
  },
  methods: {
    showLoginDialog() {
      this.$modal.show("loginDialog");
    },
    hideLoginDialog() {
      this.$modal.hide("loginDialog");
    },
    clearLoginDialog() {
      this.email = null;
      this.password = null;

      this.$modal.hide("loginDialog");
    },
    processLogin() {
      const loginDetails = {
        email: this.email,
        password: this.password
      };

      if (!loginDetails.email) {
        this.alertMessage = "Please enter a email address.";
      } else if (!loginDetails.password) {
        this.alertMessage = "Please enter a password.";
      } else {
        const self = this;
        this.$store
          .dispatch("processLogin", loginDetails)
          .then(function() {
            self.clearLoginDialog("loginDialog");
          })
          .catch(function(reason) {
            self.alertMessage = reason;
          });
      }
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
.modalBox {
  border: @mediumBorder;
}
div.title {
  width: 100%;
  text-align: center;
  background: @lightBorder;
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
