<template>
  <div class="header">
    <div class="logo">
      <img alt="Logo" v-bind:src="Logo" />
    </div>
    <div class="title">
      <h1>{{ Name }}</h1>
    </div>
    <div class="calendar">
      <v-date-picker
        v-model="selectedDate"
        :max-date="new Date()"
        :attributes="calendarAttributes"
        :is-required="true"
      >
      </v-date-picker>
    </div>
  </div>
</template>

<script>
export default {
  name: "Header",
  data() {
    return {
      calendarAttributes: [
        {
          key: "today",
          highlight: "red",
          dates: new Date(),
        },
      ],
    };
  },
  computed: {
    selectedDate: {
      get() {
        return this.$store.state.selectedDate;
      },
      set(value) {
        this.$store.commit("setSelectedDate", value);
      },
    },
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
  display: table;
  overflow: hidden;
  border-bottom: solid 1px rgb(#aaa);
}
div.logo {
  display: table-cell;
  margin-left: 1em;
  width: 200px;
}
div.title {
  display: table-cell;
  text-align: center;
}
div.calendar {
  width: 300px;
  display: table-cell;
}
</style>
<style lang="less">
div.calendar input {
  width: 14em;
}
div.calendar .vc-text-sm {
  font-size: 12px;
}
</style>
