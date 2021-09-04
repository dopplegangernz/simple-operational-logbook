<template>
  <div class="calendar">
    <v-date-picker
      v-model="selectedDate"
      :max-date="new Date()"
      :attributes="calendarAttributes"
      :is-required="true"
      is-inline
    ></v-date-picker>
  </div>
</template>

<script>
export default {
  name: "DatePicker",
  computed: {
    selectedDate: {
      get() {
        return this.$store.state.selectedDate;
      },
      set(value) {
        this.$store.commit("setSelectedDate", value);
        this.$store
          .dispatch("fetchEntriesByDate", value)
          .catch(function(reason) {
            alert(reason);
          });
      }
    },
  },
  data() {
    return {
      calendarAttributes: [
        {
          key: "today",
          highlight: "red",
          dates: new Date()
        }
      ]
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">

</style>
