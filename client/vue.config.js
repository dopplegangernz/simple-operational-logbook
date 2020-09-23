const path = require("path");

module.exports = {
  chainWebpack: (config) => {
    const types = ["vue-modules", "vue"];
    types.forEach((type) =>
      addStyleResource(config.module.rule("less").oneOf(type))
    );
  },
};

function addStyleResource(rule) {
  rule
    .use("style-resource")
    .loader("style-resources-loader")
    .options({
      patterns: [path.resolve(__dirname, "./src/styles/variables/*.less")],
    });
}
