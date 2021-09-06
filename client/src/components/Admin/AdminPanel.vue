<template>
  <div id="sol-contentArea">
    <div v-if="!isLoggedIn">
      <h1>You must be logged in to access the administation panel</h1>
    </div>
    <div v-else-if="!isAdmin">
      <h1>You must be an administrator to access the administation panel</h1>
    </div>
    <div v-else>
      <SubPanelUsers :users="users" v-if="this.activeTab === 'Users'" />
      <SubPanelAddUser :groups="Groups" v-if="this.activeTab === 'Add User'" />
      <SubPanelGroups :groups="Groups" v-if="this.activeTab === 'Groups'" />
      <SubPanelApplication v-if="this.activeTab === 'Application'" />

    </div>
  </div>
</template>

<script>
import SubPanelUsers from "./SubPanelUsers.vue";
import SubPanelAddUser from "./SubPanelAddUser.vue";
import SubPanelGroups from "./SubPanelGroups.vue";
import SubPanelApplication from "./SubPanelApplication.vue";

export default {
  name: "adminPanel",
  components: {
    SubPanelUsers,
    SubPanelAddUser,
    SubPanelGroups,
    SubPanelApplication
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
  watch: {
    isLoggedIn(newState){
      // alert("Bob" + newState);
      if(newState === true){
        init(this);
      }
    }
  },
  methods: {
  },
  mounted: function(){
    init(this);
  }
};

function init(self){
  // alert(this.isLoggedIn);
  if(self.isLoggedIn){
    self.$store.dispatch("fetchUsers").then(function(users) {
      self.users = users;
    });
  }
}
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
