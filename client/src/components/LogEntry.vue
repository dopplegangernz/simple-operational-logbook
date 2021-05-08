<template>
  <div class="logEntry">
    <div class="metadata">
      <div class="timestamp">
        {{ entryData.timestamp.toLocaleDateString() }}
        {{ entryData.timestamp.toLocaleTimeString() }}
        <SearchIcon
          action="fetchEntriesByDate"
          v-bind:payload="entryData.timestamp"
        />
      </div>
      <div class="author">
        {{ entryData.author_name }}
        <SearchIcon
          action="fetchEntriesByAuthor"
          v-bind:payload="entryData.author_name"
        />
      </div>
    </div>
    <div class="content">
      <div class="title">
        <span v-if="ActiveGroup === 'All'">[{{ entryData.group_name }}]</span>
        <span 
          action="">
          {{ entryData.subject }}
        </span>
        <SearchIcon
          action="fetchEntriesBySubject"
          v-bind:payload="entryData.subject"
        />
      </div>
      <div class="text">
        <markdown-it-vue-light class="md-body" :content="entryData.text" />
      </div>
    </div>
  </div>
</template>

<script>
import SearchIcon from "./SearchIcon.vue";
import MarkdownItVueLight from "markdown-it-vue/dist/markdown-it-vue-light.umd.min.js";
import "markdown-it-vue/dist/markdown-it-vue-light.css";

export default {
  name: "LogEntry",
  components: { SearchIcon, MarkdownItVueLight },
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
.logEntry {
  width: 100%;
  border-top: @lightBorder;
}
.metadata {
  display: inline-block;
  border-right: @lightBorder;
  padding-right: 15px;
  padding-top: @mediumPadding;
  padding-bottom: @mediumPadding;
  width: 257px;
}
.content {
  display: inline-block;
  padding-left: 15px;
  width: calc(100vw - 350px);
}
.title {
  width: 100%;
  background: @lightColour;
}
</style>
