<template>
  <div id="sol-contentArea">
    <div class="buttonBar">
      <NewLogEntryDialog v-if="isLoggedIn" />
    </div>
    <LogEntry v-for="entry in visibleEntries" :key="entry.id" :entryData="entry" />
  </div>
</template>

<script>
import LogEntry from "./LogEntry.vue";
import NewLogEntryDialog from "./NewLogEntryDialog.vue";

export default {
  name: "LogArea",
  components: {
    LogEntry,
    NewLogEntryDialog
  },
  computed: {
    contentAreaHeight() {
      const header = document.getElementById("sol-header");
      const footer = document.getElementById("sol-footer");

      if (header && footer) {
        const viewHeight = document.documentElement.clientHeight;
        const headerHeight = header.offsetHeight;
        const footerHeight = footer.offsetHeight;

        const areaHeight = viewHeight - headerHeight - 2 * footerHeight;
        return areaHeight + "px";
      } else {
        return "50px";
      }
    },
    isLoggedIn() {
      return this.$store.state.user.username !== null;
    },
    ActiveGroup() {
      return this.$store.state.activeGroup;
    },
    visibleEntries() {
      const entries = this.$store.state.entries;
      const activeGroup = this.$store.state.activeGroup;

      if (activeGroup === "All") {
        return entries;
      } else {
        return entries.filter(function(entry) {
          return entry.group_name === activeGroup;
        });
      }
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
div.buttonBar {
  text-align: center;
}
#sol-contentArea {
  overflow: scroll;
}
</style>
