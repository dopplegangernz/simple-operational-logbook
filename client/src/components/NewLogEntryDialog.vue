<template>
  <span class="sol-button" id="newEntryButton" v-on:click="showNewEntryDialog">
    Create new entry
    <modal
      name="newEntryDialog"
      :resizable="true"
      draggable=".dragHandle"
      :focusTrap="true"
      :clickToClose="false"
      classes="modalBox"
    >
      <div class="title dragHandle">
        <span>New Log Entry</span>
        <span class="sol-button" v-on:click="hideNewEntryDialog"> x</span>
      </div>
      <div class="content">
        <table>
          <tr>
            <th>Group:</th>
            <td>
              <select v-model="selectedGroup"
                ><option v-for="group in Groups" :key="group"
                  >{{ group }}
                </option>
              </select>
            </td>
          </tr>
          <th>Subject:</th>
          <td><input v-model="subject" type="text" /></td>
          <tr>
            <th>Text:</th>
            <td><textarea v-model="text" /></td>
          </tr>
        </table>
      </div>
      <div class="alertMessage" v-if="alertMessage">{{ alertMessage }}</div>
      <div class="buttons">
        <span class="sol-button" v-on:click="clearNewEntryDialog">Cancel</span>
        <span class="sol-button" v-on:click="saveEntry">Save</span>
      </div>
    </modal>
  </span>
</template>

<script>
export default {
  name: "NewLogEntryDialog",
  data: function() {
    return {
      selectedGroup:
        this.$store.state.activeGroup === "All"
          ? this.$store.state.user.group
          : this.$store.state.activeGroup,
      subject: null,
      text: null,
      alertMessage: null,
    };
  },
  computed: {
    Groups() {
      return this.$store.state.groups.filter(function(name) {
        return name !== "All";
      });
    },
  },
  methods: {
    showNewEntryDialog() {
      this.$modal.show("newEntryDialog");
    },
    hideNewEntryDialog() {
      this.$modal.hide("newEntryDialog");
    },
    clearNewEntryDialog() {
      this.subject = null;
      this.text = null;
      this.selectedGroup =
        this.$store.state.activeGroup === "All"
          ? this.$store.state.user.group
          : this.$store.state.activeGroup;
      this.$modal.hide("newEntryDialog");
    },

    saveEntry() {
      const newEntry = {
        group_name: this.selectedGroup,
        subject: this.subject,
        text: this.text,
      };

      if (!newEntry.subject) {
        this.alertMessage = "Entry requires a subject.";
      } else if (!newEntry.text) {
        this.alertMessage = "Entry requires text.";
      } else {
        this.$store.dispatch("saveEntry", newEntry);
        this.clearNewEntryDialog();
      }
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
#newEntryButton {
  margin-top: 6px;
  margin-bottom: 6px;
}
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
table {
  width: 98%;
}
th {
  width: 15%;
}
td {
  width: 80%;
}
input {
  width: 100%;
}
textarea {
  width: 100%;
  height: 14em;
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
