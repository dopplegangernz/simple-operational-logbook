<template>
  <div id="sol-adminPanel-Users" class="sol-subPanel">
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
</template>

<script>
import UserAdminRow from "../UserAdminRow.vue";

export default {
  name: "SubPanelUsers",
  components: {
    UserAdminRow
  },
  props: [
    "users"
  ],
  computed: {
  },
  methods: {
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
</style>
