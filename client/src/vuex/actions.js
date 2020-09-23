const axios = require("axios").default;

const axiosConfig = {
  baseURL: "http://localhost:5000",
  headers: {
    "Content-Type": "application/json",
  },
};

module.exports = {
  saveEntry(context, newEntry) {
    newEntry.timestamp = new Date();
    newEntry.author_name = context.state.user.username;

    context.commit("saveEntry", newEntry);
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
};
