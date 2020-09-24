<template>
  <span class="sol-adminPanel" v-on:click="showadminPanel">
    {{ Name }}
    <modal
      name="adminPanel"
      :resizable="true"
      draggable=".dragHandle"
      :focusTrap="true"
      :clickToClose="false"
      classes="modalBox"
    >
      <div class="title dragHandle">
        <span>User information for {{ Name }}</span>
        <span class="sol-button" v-on:click="hideadminPanel()">x</span>
      </div>
      <div class="content"></div>
      <div class="alertMessage" v-if="alertMessage">{{ alertMessage }}</div>
      <div class="buttons">
        <span class="sol-button" v-on:click="clearadminPanel()">Close</span>
        <span class="sol-button" v-on:click="updateUser">Save</span>
      </div>
    </modal>
  </span>
</template>

<script>
export default {
  name: "adminPanel",
  data: function() {
    return {};
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
    showadminPanel() {
      this.$modal.show("adminPanel");
    },
    hideadminPanel() {
      this.$modal.hide("adminPanel");
    },
    clearadminPanel() {
      // Reset the panel to default

      this.$modal.hide("adminPanel");
    },
    updateGroup() {
      const revisedGroup = {
        username: this.username,
        email: this.email,
        group: this.selectedGroup.name
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

      const self = this;
      this.$store
        .dispatch("updateUser", revisedUser)
        .then(function() {
          self.clearadminPanel();
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
.modalBox {
  border: @mediumBorder;
}
span.sol-adminPanel {
  color: @linkcolour;
}

span.sol-adminPanel div {
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
