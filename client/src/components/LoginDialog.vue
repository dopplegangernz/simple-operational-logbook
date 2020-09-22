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
      width="260px"
      height="160px"
    >
      <div class="title dragHandle">
        <span>Login</span>
        <span class="sol-button" v-on:click="hideLoginDialog"> x</span>
      </div>
      <div class="loginContent"></div>
      <table>
        <tr>
          <th>User name:</th>
          <td><input type="text" v-model="username" /></td>
        </tr>
        <tr>
          <th>
            Password:
          </th>
          <td>
            <input type="password" v-model="password" />
          </td>
        </tr>
      </table>

      <div class="alertMessage" v-if="alertMessage">
        {{ alertMessage }}
      </div>
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
      username: null,
      password: null,
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
      this.username = null;
      this.password = null;

      this.$modal.hide("loginDialog");
    },
    processLogin() {
      const loginDetails = {
        username: this.loginDialog.username,
        subject: this.loginDialog.password,
      };

      if (!loginDetails.username) {
        this.loginDialog.alertMessage = "Please enter a username.";
      } else if (!loginDetails.password) {
        this.loginDialog.alertMessage = "Please enter a password.";
      } else {
        this.$store.dispatch("processLogin", loginDetails);
        this.clearModal("loginDialog");
      }
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
.modalBox {
  border: 1px solid rgb(#aaa);
}
div.title {
  width: 100%;
  text-align: center;
  background: rgb(#ddd);
  font-size: larger;
}
div.title span.sol-button {
  float: right;
  font-size: small;
  margin-top: 3px;
}
div.alertMessage {
  text-align: center;
  color: red;
  font-weight: bold;
}
div.buttons {
  text-align: center;
}
</style>
