<template>
  <span class="sol-adminPanel sol-button" v-on:click="showAdminPanel">
    Admin Panel
    <modal
      name="adminPanel"
      draggable=".dragHandle"
      :focusTrap="true"
      :clickToClose="false"
      classes="modalBox"
      width="850px"
      height="500px"
    >
      <div class="title dragHandle">
        <span>Logbook Administration</span>
        <span class="sol-button" v-on:click="hideAdminPanel">x</span>
      </div>
      <div class="content">
        <div class="tabBar">
          <span
            class="tab"
            v-bind:class="{ active: activeTab === 'Users' }"
            v-on:click="setActiveTab('Users')"
            >Manage users</span
          >
          <span
            class="tab"
            v-bind:class="{ active: activeTab === 'AddUser' }"
            v-on:click="setActiveTab('AddUser')"
            >Add a user</span
          >
          <span
            class="tab"
            v-bind:class="{ active: activeTab === 'Groups' }"
            v-on:click="setActiveTab('Groups')"
            >Groups</span
          >
          <span
            class="tab"
            v-bind:class="{ active: activeTab === 'Application' }"
            v-on:click="setActiveTab('Application')"
            >Application Options</span
          >
        </div>
        <div v-if="activeTab === 'Users'" class="tabContent">
          <table class="userTable">
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
        <div v-if="activeTab === 'AddUser'" class="tabContent">
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
        <div v-if="activeTab === 'Groups'" class="tabContent">
          Here be groups
          <div class="buttons">
            <span class="sol-button" v-on:click="clearAdminPanel">Cancel</span>
            <span class="sol-button" v-on:click="alert('hi')">Save</span>
          </div>
        </div>
        <div v-if="activeTab === 'Application'" class="tabContent">
          Here be application options
          <div class="buttons">
            <span class="sol-button" v-on:click="clearAdminPanel">Cancel</span>
            <span class="sol-button" v-on:click="alert('hi')">Save</span>
          </div>
        </div>
      </div>
    </modal>
  </span>
</template>

<script>
import UserAdminRow from "../UserAdminRow.vue";
export default {
  name: "adminPanel",
  components: { UserAdminRow },
  data: function() {
    return {
      newUserAlertMessage: null,
      alertMessage: null,
      activeTab: "Users",
      users: [],
      newUser: {}
    };
  },
  computed: {
    Groups() {
      return this.$store.state.groups.filter(function(group) {
        return group.name !== "All";
      });
    }
  },
  methods: {
    setActiveTab(tabName) {
      if (tabName) {
        this.activeTab = tabName;
      } else {
        tabName = this.activeTab;
      }
    },
    showAdminPanel() {
      this.$modal.show("adminPanel");
    },
    hideAdminPanel() {
      this.$modal.hide("adminPanel");
    },
    clearAdminPanel() {
      // Reset the panel to default

      this.$modal.hide("adminPanel");
    },
    cancelUserAdd() {
      this.defaultNewUserValues();
      this.$modal.hide("adminPanel");
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
        isAdmin: "False",
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
.modalBox {
  border: @mediumBorder;
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
