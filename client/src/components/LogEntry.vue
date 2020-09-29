<template>
  <div class="sol-logEntry">
    <div class="sol-logEntry-metadata">
      <div class="sol-logEntry-timestamp">
        {{ entryData.timestamp.toLocaleDateString() }}
        {{ entryData.timestamp.toLocaleTimeString() }}
        <SearchIcon
          action="fetchEntriesByDate"
          v-bind:payload="entryData.timestamp"
        />
      </div>
      <div class="sol-logEntry-author">
        {{ entryData.author_name }}
        <SearchIcon
          action="fetchEntriesByAuthor"
          v-bind:payload="entryData.author_name"
        />
      </div>
    </div>
    <div class="sol-logEntry-content">
      <div class="sol-logEntry-title">
        <span v-if="ActiveGroup === 'All'">[{{ entryData.group_name }}]</span>
        {{ entryData.subject }}
        <SearchIcon
          action="fetchEntriesBySubject"
          v-bind:payload="entryData.subject"
        />
      </div>
      <div class="sol-logEntry-text">
        <markdown-it-vue class="md-body" :content="entryData.text" />
      </div>
    </div>
  </div>
</template>

<script>
import SearchIcon from "./SearchIcon.vue";
import MarkdownItVue from "markdown-it-vue";
import "markdown-it-vue/dist/markdown-it-vue.css";

export default {
  name: "LogEntry",
  components: { SearchIcon, MarkdownItVue },
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
  border-top: @lightBorder;
}
.sol-logEntry-metadata {
  display: inline-block;
  border-right: @lightBorder;
  padding-right: 15px;
  padding-top: @mediumPadding;
  padding-bottom: @mediumPadding;
  width: 257px;
}
.sol-logEntry-content {
  display: inline-block;
  padding-left: 15px;
  width: calc(100vw - 350px);
}
.sol-logEntry-title {
  width: 100%;
  background: @lightColour;
}
</style>
