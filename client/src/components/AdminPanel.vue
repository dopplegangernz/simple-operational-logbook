<template>
  <span class="sol-adminPanel sol-button" v-on:click="showAdminPanel">
    Admin Panel
    <modal
      name="adminPanel"
      draggable=".dragHandle"
      :focusTrap="true"
      :clickToClose="false"
      classes="modalBox"
    >
      <div class="title dragHandle">
        <span>Logbook Administration</span>
        <span class="sol-button" v-on:click="hideAdminPanel">x</span>
      </div>
      <div class="content">
        <div class="tabBar">
          <span
            class="tab"
            v-bind:class="{active: activeTab === 'Users'}"
            v-on:click="setActiveTab('Users')"
          >Users</span>
          <span
            class="tab"
            v-bind:class="{active: activeTab === 'Groups'}"
            v-on:click="setActiveTab('Groups')"
          >Groups</span>
        </div>
        <div id="Users" class="tabContent">Here be users</div>
        <div id="Groups" class="tabContent" style="display:none">Here be groups</div>
      </div>
      <div class="alertMessage" v-if="alertMessage">{{ alertMessage }}</div>
      <div class="buttons">
        <span class="sol-button" v-on:click="clearAdminPanel">Close</span>
        <span class="sol-button" v-on:click="alert('hi')">Save</span>
      </div>
    </modal>
  </span>
</template>

<script>
export default {
  name: "adminPanel",
  data: function() {
    return {
      alertMessage: null,
      activeTab: "Users"
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
</style>
