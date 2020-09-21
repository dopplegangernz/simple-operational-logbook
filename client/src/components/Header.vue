<template>
  <div class="header">
    <div class="logo">
      <img alt="Logo" v-bind:src="Logo" />
    </div>
    <div class="title">
      <h1>{{ Name }}</h1>
    </div>
    <div class="calendar">
      <v-calendar></v-calendar><v-date-picker v-model="selectedDate" />
    </div>
  </div>
</template>

<script>
export default {
  name: "Header",
  computed: {
    Name() {
      return this.$store.state.appName;
    },
    Logo() {
      return this.$store.state.logo;
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
div.header {
  width: 100%;
  text-align: center;
  overflow: hidden;
  border-bottom: solid 1px rgb(#aaa);
}
div.logo {
  float: left;
  margin-left: 1em;
  width: 100px;
}
div.title {
  display: inline-block;
}
div.calendar {
  float: right;
  margin-right: 1em;
  width: 100px;
}
</style>
