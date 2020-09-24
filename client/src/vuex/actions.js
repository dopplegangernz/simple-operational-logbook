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
        .get(
          `/entries/${previousMidnight(selectedDate)}/${followingMidnight(
            selectedDate
          )}`,
          axiosConfig
        )
        .then(function(response) {
          const data = response.data;

          if (response.status === 200) {
            data.forEach((element) => {
              element.timestamp = new Date(element.timestamp + "Z");
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
              element.timestamp = new Date(element.timestamp + "Z");
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
              element.timestamp = new Date(element.timestamp + "Z");
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

function previousMidnight(dateObj) {
  const midnight = new Date(dateObj.getTime());
  midnight.setHours(0);
  midnight.setMinutes(0);
  midnight.setSeconds(0);
  midnight.setMilliseconds(0);

  return toTimeStamp(midnight);
}
function followingMidnight(dateObj) {
  const midnight = new Date(dateObj.getTime());
  midnight.setHours(23);
  midnight.setMinutes(59);
  midnight.setSeconds(59);
  midnight.setMilliseconds(999);

  return toTimeStamp(midnight);
}
function toTimeStamp(dateObj) {
  const year = dateObj.getUTCFullYear();
  const month = (dateObj.getUTCMonth() + 1).toString().padStart(2, "0");
  const day = dateObj
    .getUTCDate()
    .toString()
    .padStart(2, "0");
  const hour = dateObj
    .getUTCHours()
    .toString()
    .padStart(2, "0");
  const minutes = dateObj
    .getUTCMinutes()
    .toString()
    .padStart(2, "0");
  const seconds = dateObj
    .getUTCSeconds()
    .toString()
    .padStart(2, "0");

  return `${year}-${month}-${day}T${hour}:${minutes}:${seconds}Z`;
}
