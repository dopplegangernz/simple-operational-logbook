<template>
  <span class="sol-button sol-userPanel" v-on:click="handleButtonClick">
    {{ Name }}
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
        <span class="sol-button" v-on:click="hideModal('loginDialog')"> x</span>
      </div>
      <div class="loginContent"></div>
      <table>
        <tr>
          <th>User name:</th>
          <td><input type="text" v-model="loginDialog.username" /></td>
        </tr>
        <tr>
          <th>
            Password:
          </th>
          <td>
            <input type="password" v-model="loginDialog.password" />
          </td>
        </tr>
      </table>

      <div class="alertMessage" v-if="loginDialog.alertMessage">
        {{ loginDialog.alertMessage }}
      </div>
      <div class="buttons">
        <span class="sol-button" v-on:click="clearModal('loginDialog')"
          >Cancel</span
        >
        <span class="sol-button" v-on:click="processLogin">Log in</span>
      </div>
    </modal>

    <modal
      name="userPanel"
      :resizable="true"
      draggable=".dragHandle"
      :focusTrap="true"
      :clickToClose="false"
      classes="modalBox"
    >
      <div class="title dragHandle">
        <span>User informatioon for {{ Name }} </span>
        <span class="sol-button" v-on:click="hideModal('userPanel')"> x</span>
      </div>
      <div class="content"></div>
      <div class="alertMessage" v-if="userPanel.alertMessage">
        {{ userPanel.alertMessage }}
      </div>
      <div class="buttons">
        <span class="sol-button" v-on:click="clearModal('userPanel')"
          >Cancel</span
        >
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
      loginDialog: {
        alertMessage: null,
        username: null,
        password: null,
      },
      userPanel: {
        alertMessage: null,
      },
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
    handleButtonClick() {
      if (this.$store.state.user.username === null) {
        this.showModal("loginDialog");
      } else {
        this.showModal("userPanel");
      }
    },
    showModal(modalName) {
      this.$modal.show(modalName);
    },
    hideModal(modalName) {
      this.$modal.hide(modalName);
    },
    clearModal(modalName) {
      if (modalName === "loginDialog") {
        this.loginDialog.username = null;
        this.loginDialog.password = null;
      }

      this.$modal.hide(modalName);
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
    updateUser() {
      let foo = "baa";
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
