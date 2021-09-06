<template>
  <div id="sol-adminPanel-AddUser" class="sol-subPanel" >
    <h1> Add User</h1>
    <table>
          <tr>
            <th>Email:</th>
            <td>
              <input type="text" v-model="newUser.email" />
            </td>
          </tr>
          <tr>
            <th>Username:</th>
            <td>
              <input type="text" v-model="newUser.username" />
            </td>
          </tr>
          <tr>
            <th>Group:</th>
            <td>
              <select v-model="newUser.group">
                <option v-for="group in groups" :key="group.name">
                  {{ group.name }}
                </option>
              </select>
            </td>
          </tr>
          <tr>
            <th>Administrator:</th>
            <td>
              <input type="checkbox" v-model="newUser.isAdmin" />
            </td>
          </tr>
          <tr>
            <th>Password:</th>
            <td>
              <input type="password" v-model="newUser.password" />
            </td>
          </tr>
          <tr>
            <th>Confirm password:</th>
            <td>
              <input type="password" v-model="newUser.password2" />
            </td>
          </tr>
          <tr></tr>
        </table>

        <div class="alertMessage" v-if="newUserAlertMessage">
          {{ newUserAlertMessage }}
        </div>
        <div class="buttons">
          <span class="sol-button" v-on:click="cancelUserAdd">Cancel</span>
          <span class="sol-button" v-on:click="createUser">Save</span>
        </div>
      
  </div>
</template>

<script>

export default {
  name: "SubPanelAddUser",
  props:["groups"],
  data: function() {
    return {
      newUserAlertMessage: null,
      alertMessage: null,
      newUser: {}
    };
  },
  methods: {
    cancelUserAdd() {
      this.defaultNewUserValues();
    },
    createUser() {
      if (!this.newUser.email) {
        return (this.newUserAlertMessage = "You must enter an email address");
      }
      if (!this.newUser.username) {
        return (this.newUserAlertMessage = "You must enter a username");
      }
      if (!this.newUser.password) {
        return (this.newUserAlertMessage = "You must enter a password");
      }
      if (this.newUser.password !== this.newUser.password2) {
        return (this.newUserAlertMessage = "Passwords must match");
      }
      this.newUserAlertMessage = "";

      this.$store
        .dispatch("createUser", this.newUser)
        .then(function() {
          this.newUserAlertMessage = `User ${self.newUser.username} successfully created`;
          this.defaultNewUserValues;
        })
        .catch(function(message) {
          this.newUserAlertMessage = message;
        });
    },
    defaultNewUserValues() {
      this.newUser = {
        username: null,
        email: null,
        group: this.$store.state.groups[1].name,
        isAdmin: false,
        password: null,
        password2: null
      };
    }
  },
  mounted: function() {
    this.defaultNewUserValues();
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">

div.alertMessage {
  text-align: center;
  color: @alertColour;
  font-weight: bold;
}
div.buttons {
  text-align: center;
}
.userTable {
  width: 95%;
  margin-right: 2.5%;
  margin-left: 2.5%;
  border-collapse: collapse;
}
th.username {
}
th.email {
  width: 16em;
}
th.group {
  width: 8em;
}
th.admin {
  width: 4em;
}
th.actions {
  width: 3.5em;
}
</style>
