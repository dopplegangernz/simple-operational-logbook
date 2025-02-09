<template>
  <div id="sol-contentArea">
    <h1>User information for {{ Name }}</h1>
    <table>
      <tr>
        <th>Email:</th>
        <td>
          <input v-if="editMode" type="text" v-model="email" />
          <span v-else>{{ email }}</span>
        </td>
      </tr>
      <tr>
        <th>Username:</th>
        <td>
          <input v-if="editMode" type="text" v-model="username" />
          <span v-else>{{ username }}</span>
        </td>
      </tr>
      <tr>
        <th>Group:</th>
        <td>
          <select v-if="editMode" v-model="selectedGroup">
            <option v-for="group in Groups" :key="group.name">
              {{ group.name }}
            </option>
          </select>
          <span v-else>{{ selectedGroup }}</span>
        </td>
      </tr>
      <tr v-if="editMode">
        <th>Password:</th>
        <td>
          <input type="password" v-model="password1" />
        </td>
      </tr>
      <tr v-if="editMode">
        <th>Confirm password:</th>
        <td>
          <input type="password" v-model="password2" />
        </td>
      </tr>
      <tr></tr>
    </table>

    <div class="alertMessage" v-if="alertMessage">{{ alertMessage }}</div>
    <div class="buttons">
      <span class="sol-button" v-if="editMode" v-on:click="updateUser">
        Save
      </span>
      <span class="sol-button" v-if="editMode" v-on:click="cancelEditUser">
        Cancel
      </span>
      <span class="sol-button" v-else v-on:click="editUser">
        Edit
      </span>
    </div>
  </div>
</template>

<script>
export default {
  name: "UserPanel",
  data: function() {
    return {
      editMode: false,
      alertMessage: null,
      username: this.$store.state.user.username,
      password: null,
      email: this.$store.state.user.email,
      selectedGroup: this.$store.state.user.group,
      password1: null,
      password2: null
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
    }
  },
  methods: {
    editUser() {
      this.editMode = true;
    },
    cancelEditUser(){
      this.editMode = false;
      this.clearUserPanel();
    },
    clearUserPanel() {
      // Reset the panel to default
      this.editMode = false;
      this.username = this.$store.state.user.username;
      this.password = null;
      this.email = this.$store.state.user.email;
    },
    updateUser() {
      const revisedUser = {
        id: this.$store.state.user.id,
        username: this.username,
        email: this.email,
        group: this.selectedGroup
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
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">

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
