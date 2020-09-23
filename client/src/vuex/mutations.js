module.exports = {
  setSearchString(state, searchString) {
    state.searchString = searchString;
    state.fetchBy = "searchString";
  },
  setSelectedDate(state, selectedDate) {
    state.selectedDate = selectedDate;
    state.fetchBy = "date";
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
  defaultUserDetails(state) {
    state.user.username = null;
    state.user.email = null;
    state.user.group = "All";
    state.user.id = null;
    state.user.authKey = null;
    state.user.isAdmin = false;
  },
  setGroups(state, groups) {
    groups.unshift({
      name: "All",
      description: "All groups",
      is: 1,
    });
    state.groups = groups;
  },
};
