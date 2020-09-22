<template>
  <div class="logArea">
    <div class="buttonBar">
      <NewLogEntryDialog />
    </div>
    <LogEntry
      v-for="entry in visibleEntries"
      :key="entry.id"
      :entryData="entry"
    />
  </div>
</template>

<script>
import LogEntry from "./LogEntry.vue";
import NewLogEntryDialog from "./NewLogEntryDialog.vue";

export default {
  name: "LogArea",
  components: {
    LogEntry,
    NewLogEntryDialog,
  },
  computed: {
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
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
div.buttonBar {
  text-align: center;
}
</style>
