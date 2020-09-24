const axios = require("axios").default;

const axiosConfig = {
  baseURL: "http://localhost:5000",
  headers: {
    "Content-Type": "application/json",
  },
};

module.exports = {
  saveEntry(context, newEntry) {
    return new Promise((resolve, reject) => {
      axios.post("/entry/", newEntry, axiosConfig).then(function(response) {
        const data = response.data;

        console.log(response);
        if (data.status === "success") {
          newEntry.timestamp = new Date();
          newEntry.author_name = context.state.user.username;
          newEntry.id = data.id;

          context.commit("saveEntry", newEntry);
          resolve();
        } else {
          reject(data.message);
        }
      });
    });
  },
  processLogin(context, loginDetails) {
    return new Promise((resolve, reject) => {
      axios
        .post("/auth/login", loginDetails, axiosConfig)
        .then(function(response) {
          const data = response.data;
          console.log(response);
          if (data.status === "success") {
            context.commit("setUserDetails", data);
            axiosConfig.headers.authorization = data.Authorization;
            resolve();
          } else {
            reject(data.message);
          }
        });
    });
  },
  processLogout(context) {
    return new Promise((resolve, reject) => {
      axios.post("/auth/logout", {}, axiosConfig).then(function(response) {
        const data = response.data;
        console.log(response);
        if (data.status === "success") {
          context.commit("defaultUserDetails");
          axiosConfig.headers.authorization = undefined;
          resolve();
        } else {
          reject(data.message);
        }
      });
    });
  },
  fetchGroups(context) {
    return new Promise((resolve, reject) => {
      axios.get("/group/", axiosConfig).then(function(response) {
        const data = response.data;
        console.log(data);

        if (response.status === 200) {
          context.commit("setGroups", data);
          resolve();
        } else {
          reject(data.message);
        }
      });
    });
  },
  fetchEntriesByDate(context, selectedDate) {
    return new Promise((resolve, reject) => {
      axios
        .get("/entries/" + selectedDate.toISOString().slice(0, 10), axiosConfig)
        .then(function(response) {
          const data = response.data;

          if (response.status === 200) {
            data.forEach((element) => {
              element.timestamp = new Date(element.timestamp);
            });

            context.commit("setEntries", data);
            resolve();
          } else {
            reject(data.message);
          }
        });
    });
  },
  fetchEntriesBySubject(context, subject) {
    return new Promise((resolve, reject) => {
      axios
        .get("/entries/search/subject/" + subject, axiosConfig)
        .then(function(response) {
          const data = response.data;

          console.log(data);

          if (response.status === 200) {
            data.forEach((element) => {
              element.timestamp = new Date(element.timestamp);
            });

            context.commit("setEntries", data);
            context.commit("setSelectedDate", null);
            resolve();
          } else {
            reject(data.message);
          }
        });
    });
  },
  fetchEntriesBySearchString(context, searchString) {
    return new Promise((resolve, reject) => {
      axios
        .get("/entries/search/string/" + searchString, axiosConfig)
        .then(function(response) {
          const data = response.data;

          if (response.status === 200) {
            data.forEach((element) => {
              element.timestamp = new Date(element.timestamp);
            });

            context.commit("setEntries", data);
            context.commit("setSelectedDate", null);
            resolve();
          } else {
            reject(data.message);
          }
        });
    });
  },
};
