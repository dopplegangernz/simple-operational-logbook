module.exports = {
  setSearchString(state, searchString) {
    state.searchString = searchString;
  },
  setSelectedDate(state, selectedDate) {
    state.selectedDate = selectedDate;
  },
  selectGroup(state, group) {
    state.activeGroup = group;
  },
  saveEntry(state, newEntry) {
    state.entries.push(newEntry);
  },
  setUserDetails(state, userDetails) {
    state.user.username = userDetails.username;
    state.user.email = userDetails.email;
    state.user.group = userDetails.group;
    state.user.id = userDetails.id;
    state.user.authKey = userDetails.Authorization;
    state.user.isAdmin = userDetails.isAdmin;
  },
};
