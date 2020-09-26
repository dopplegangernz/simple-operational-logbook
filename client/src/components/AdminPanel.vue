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
        <div id="Users" class="tabContent">
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
        <div id="AddUser" class="tabContent" style="display:none">
          Add a user, yo
          <div class="buttons">
            <span class="sol-button" v-on:click="clearAdminPanel">Cancel</span>
            <span class="sol-button" v-on:click="alert('hi')">Save</span>
          </div>
        </div>
        <div id="Groups" class="tabContent" style="display:none">
          Here be groups
          <div class="buttons">
            <span class="sol-button" v-on:click="clearAdminPanel">Cancel</span>
            <span class="sol-button" v-on:click="alert('hi')">Save</span>
          </div>
        </div>
        <div id="Application" class="tabContent" style="display:none">
          Here be application options
          <div class="buttons">
            <span class="sol-button" v-on:click="clearAdminPanel">Cancel</span>
            <span class="sol-button" v-on:click="alert('hi')">Save</span>
          </div>
        </div>
      </div>
      <div class="alertMessage" v-if="alertMessage">{{ alertMessage }}</div>
    </modal>
  </span>
</template>

<script>
import UserAdminRow from "./UserAdminRow.vue";
export default {
  name: "adminPanel",
  components: { UserAdminRow },
  data: function() {
    return {
      alertMessage: null,
      activeTab: "Users",
      users: []
    };
  },
  computed: {},
  methods: {
    setActiveTab(tabName) {
      if (tabName) {
        this.activeTab = tabName;
      } else {
        tabName = this.activeTab;
      }

      const contentDivs = document.getElementsByClassName("tabContent");

      for (let i = 0; i < contentDivs.length; i++) {
        contentDivs[i].style.display = "none";
      }

      document.getElementById(tabName).style.display = "block";
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
    }
  },
  mounted: function() {
    const self = this;
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
