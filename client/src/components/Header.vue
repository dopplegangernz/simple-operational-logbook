<template>
  <div class="header">
    <div class="logo">
      <img alt="Logo" v-bind:src="Logo" />
    </div>
    <div class="title">
      <h1>{{ Name }}</h1>
    </div>
    <div class="calendar">Calendar goes here</div>
  </div>
</template>

<script>
export default {
  name: "Header",
  props: {
    Name: String,
    Logo: String
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
div.header {
  width: 100%;
  text-align: center;
  overflow: hidden;
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
