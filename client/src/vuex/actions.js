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
            resolve();
          } else {
            reject(data.message);
          }
        });
    });
  },
};
