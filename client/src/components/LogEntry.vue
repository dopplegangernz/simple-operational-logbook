<template>
  <div class="sol-logEntry">
    <div class="sol-logEntry-metadata">
      <div class="sol-logEntry-timestamp">
        {{ entryData.timestamp.toLocaleDateString() }}
        {{ entryData.timestamp.toLocaleTimeString() }}
      </div>
      <div class="sol-logEntry-author">{{ entryData.author_name }}</div>
    </div>
    <div class="sol-logEntry-content">
      <div class="sol-logEntry-title">
        <span v-if="ActiveGroup === 'All'">[{{ entryData.group_name }}]</span>
        {{ entryData.subject }}
        <svg
          v-on:click="searchBySubject"
          class="magnifyingGlass"
          width="18"
          height="18"
          xmlns="http://www.w3.org/2000/svg"
        >
          <g>
            <title>Magnifying glass</title>
            <ellipse ry="6" rx="6" cy="8" cx="8" stroke-width="2" fill="none" />
            <line stroke-linecap="round" y2="18" x2="18" y1="14" x1="14" stroke-width="3" />
          </g>
        </svg>
      </div>
      <div class="sol-logEntry-text">{{ entryData.text }}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LogEntry",
  computed: {
    ActiveGroup() {
      return this.$store.state.activeGroup;
    }
  },
  methods: {
    searchBySubject() {
      this.$store
        .dispatch("fetchEntriesBySubject", this.entryData.subject)
        .catch(function(message) {
          alert(message);
        });
    }
  },
  props: {
    entryData: Object
  }
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
  padding-right: 1em;
  padding-top: @mediumPadding;
  padding-bottom: @mediumPadding;
  width: 15%;
}
.sol-logEntry-content {
  display: inline-block;
  padding-left: 1em;
  width: 80%;
}
.sol-logEntry-title {
  width: 100%;
  background: @lightColour;
}
.magnifyingGlass {
  stroke: @darkColour;
  position: absolute;
  margin-left: @mediumPadding;
  cursor: pointer;
}
</style>
