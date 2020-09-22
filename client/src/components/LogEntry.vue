<template>
  <div class="sol-logEntry">
    <div class="sol-logEntry-metadata">
      <div class="sol-logEntry-timestamp">
        {{ entryData.timestamp.toLocaleDateString() }}
        {{ entryData.timestamp.toLocaleTimeString() }}
      </div>
      <div class="sol-logEntry-author">{{ entryData.author_name }}</div>
    </div>
    <div class="sol-logEntry-content ">
      <div class="sol-logEntry-title">
        <span v-if="ActiveGroup === 'All'"> [{{ entryData.group_name }}]</span>
        {{ entryData.subject }}
      </div>
      <div class="sol-logEntry-text">
        {{ entryData.text }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LogEntry",
  computed: {
    ActiveGroup() {
      return this.$store.state.activeGroup;
    },
  },
  props: {
    entryData: Object,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
.sol-logEntry {
  width: 100%;
  border-top: 1px solid rgb(#ddd);
}
.sol-logEntry-metadata {
  display: inline-block;
  border-right: 1px solid rgb(#ddd);
  padding-right: 1em;
  padding-top: 6px;
  padding-bottom: 6px;
  width: 15%;
}
.sol-logEntry-content {
  display: inline-block;
  padding-left: 1em;
  width: 80%;
}
.sol-logEntry-title {
  width: 100%;
  background: rgb(#ddd);
}
</style>
