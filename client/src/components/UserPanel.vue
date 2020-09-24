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
      <div class="content">
        <table>
          <tr>
            <th>Email:</th>
            <td><input type="text" v-model="email" /></td>
          </tr>
          <tr>
            <th>Username:</th>
            <td><input type="text" v-model="username" /></td>
          </tr>
          <tr>
            <th>Group:</th>
            <td>
              <select v-model="selectedGroup">
                <option v-for="group in Groups" :key="group.name">{{
                  group.name
                }}</option>
              </select>
            </td>
          </tr>
          <tr>
            <th>Password:</th>
            <td><input type="password" v-model="password1" /></td>
          </tr>
          <tr>
            <th>Confirm password:</th>
            <td><input type="password" v-model="password2" /></td>
          </tr>
          <tr></tr>
        </table>
      </div>
      <div class="alertMessage" v-if="alertMessage">{{ alertMessage }}</div>
      <div class="buttons">
        <span class="sol-button" v-on:click="clearUserPanel()">Close</span>
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
      email: this.$store.state.user.email,
      selectedGroup: this.$store.state.user.group,
      password1: null,
      password2: null,
    };
  },
  computed: {
    Name() {
      return this.$store.state.user.username;
    },
    Groups() {
      return this.$store.state.groups.filter(function(group) {
        return group.name !== "All";
      });
    },
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
      const revisedUser = {
        username: this.username,
        email: this.email,
        group: this.selectedGroup.name,
      };
      if (this.password1) {
        if (this.password1 !== this.password2) {
          this.alertMessage =
            "Passwords must match. (If you're not intending to update your password, just clear the password fields)";
          return;
        } else {
          revisedUser.password = this.password1;
        }
      }
      if (!this.username) {
        this.alertMessage = "You must have a username";
        return;
      }
      if (!this.email) {
        this.alertMessage = "You must have an email address";
        return;
      }

      const self = this;
      this.$store
        .dispatch("updateUser", revisedUser)
        .then(function() {
          self.clearUserPanel();
        })
        .catch(function(message) {
          self.alertMessage = message;
        });
    },
  },
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
