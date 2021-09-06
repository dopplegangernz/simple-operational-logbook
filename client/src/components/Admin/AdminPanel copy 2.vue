<template>
  <div id="sol-contentArea">
    <div v-if="!isLoggedIn">
      <h1>You must be logged in to access the administation panel</h1>
    </div>
    <div v-else-if="!isAdmin">
      <h1>You must be an administrator to access the administation panel</h1>
    </div>
    <div v-else>
      <div id="sol-adminPanel-Users" class="sol-subPanel" v-if="this.activeTab === 'Users'">
        <h1> Users</h1>
        <table>
          <thead>
            <tr>
              <th class="username">Username</th>
              <th class="email">Email address</th>
              <th class="group">Default group</th>
              <th class="admin">Admin</th>
              <th class="actions"></th>
            </tr>
          </thead>
          <UserAdminRow
            v-for="user in users"
            :key="user.id"
            :userData="user"
          />
        </table>
      </div>
      <div id="sol-adminPanel-AddUser" class="sol-subPanel" v-if="this.activeTab === 'Add User'">
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
                    <option v-for="group in Groups" :key="group.name">
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
      <div id="sol-adminPanel-Groups" class="sol-subPanel" v-if="this.activeTab === 'Groups'">
        <h1> Groups</h1>
      </div>
      <div id="sol-adminPanel-Application" class="sol-subPanel" v-if="this.activeTab === 'Application'">
        <h1> Application</h1>
      </div>
    </div>
  </div>
</template>

<script>
import UserAdminRow from "../UserAdminRow.vue";

export default {
  name: "adminPanel",
  components: {
    UserAdminRow
  },
  props:["activeTab"],
  data: function() {
    return {
      newUserAlertMessage: null,
      alertMessage: null,
      users: [],
      newUser: {}
    };
  },
  computed: {
    isAdmin() {
      return this.$store.state.user.isAdmin;
    },
    isLoggedIn() {
      return this.$store.state.user.username !== null;
    },
    Groups() {
      return this.$store.state.groups.filter(function(group) {
        return group.name !== "All";
      });
    }
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
    const self = this;
    this.defaultNewUserValues();
    this.$store.dispatch("fetchUsers").then(function(users) {
      self.users = users;
    });
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">

div.sol-subPanel {
  margin: auto;
  max-width: 60em;
  text-align: center;
}
div.sol-subPanel table {
  margin: auto;
  text-align: left;
}

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
