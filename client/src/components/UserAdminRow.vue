<template>
  <tr v-if="editMode">
    <td><input type="text" v-model="candidateUser.username" /></td>
    <td><input type="text" v-model="candidateUser.email" /></td>
    <td>
      <select v-model="candidateUser.group">
        <option v-for="group in Groups" :key="group.name">
          {{ group.name }}
        </option>
      </select>
    </td>
    <td><input type="checkbox" v-model="candidateUser.isAdmin" /></td>
    <td>
      <svg
        v-on:click="saveChanges"
        width="20px"
        height="20px"
        viewBox="0 0 20 20"
        version="1.1"
        xmlns="http://www.w3.org/2000/svg"
        xmlns:xlink="http://www.w3.org/1999/xlink"
        xml:space="preserve"
        xmlns:serif="http://www.serif.com/"
      >
        <path d="M1,1L15,1L19,5L19,19L1,19Z" />
        <path d="M7,1L7,5L13,5L13,1" />
        <path d="M5,19L5,10L15,10L15,19" />
      </svg>
      <svg
        v-on:click="cancelEdit"
        width="20px"
        height="20px"
        viewBox="0 0 20 20"
        version="1.1"
        xmlns="http://www.w3.org/2000/svg"
        xmlns:xlink="http://www.w3.org/1999/xlink"
        xml:space="preserve"
        xmlns:serif="http://www.serif.com/"
      >
        <circle cx="10" cy="10" r="9" />
        <path d="M6,6L14,14" />
        <path d="M6,14L14,6" />
      </svg>
    </td>
  </tr>
  <tr v-else>
    <td>{{ userData.username }}</td>
    <td>{{ userData.email }}</td>
    <td>{{ userData.group }}</td>
    <td>{{ userData.isAdmin }}</td>
    <td>
      <svg
        v-on:click="editRow"
        width="20px%"
        height="20px"
        viewBox="0 0 20 20"
        version="1.1"
        xmlns="http://www.w3.org/2000/svg"
        xmlns:xlink="http://www.w3.org/1999/xlink"
        xml:space="preserve"
        xmlns:serif="http://www.serif.com/"
      >
        <path d="M1,19L4,13L16,1L19,4L7,16Z" />

        <path d="M4,13L7,16" />

        <path class="fine filled" d="M1,19L2,17L3,18Z" />
      </svg>
    </td>
  </tr>
</template>

<script>
export default {
  name: "UserAdminRow",
  props: ["userData"],
  data: function() {
    return {
      editMode: false,
      candidateUser: {
        id: this.userData.id,
        username: this.userData.username,
        email: this.userData.email,
        group: this.userData.group,
        isAdmin: this.userData.isAdmin
      }
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
    editRow: function() {
      this.editMode = true;
    },
    saveChanges: function() {
      const self = this;
      this.$store
        .dispatch("updateUser", this.candidateUser)
        .then(function() {
          self.editMode = false;
          self.userData.username = self.candidateUser.username;
          self.userData.email = self.candidateUser.email;
          self.userData.group = self.candidateUser.group;
          self.userData.isAdmin = self.candidateUser.isAdmin;
        })
        .catch(function(message) {
          alert(message);
        });
    },
    cancelEdit: function() {
      this.editMode = false;
      this.candidateUser.username = this.userData.username;
      this.candidateUser.email = this.userData.email;
      this.candidateUser.group = this.userData.group;
      this.candidateUser.isAdmin = this.userData.isAdmin;
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
tr {
  text-align: left;
}
.modalBox {
  border: @mediumBorder;
}
svg {
  vertical-align: middle;
  margin-left: @mediumPadding;
  cursor: pointer;
}
svg path,
svg circle {
  fill: none;
  stroke: @darkColour;
  stroke-width: 2px;
}
svg path.fine {
  stroke-width: 1px;
}
svg path.filled {
  fill: @darkColour;
}
td {
  border: @lightBorder;
}
td input {
  width: 95%;
}
</style>
