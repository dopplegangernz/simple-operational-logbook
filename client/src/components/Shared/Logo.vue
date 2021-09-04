<template>
    <div class="logo">
      <img alt="Logo" width="250" v-bind:src="Logo" />
    </div>
</template>

<script>
export default {
  name: "Logo",
  computed: {
    Logo() {
      return this.$store.state.logo;
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">

</style>
