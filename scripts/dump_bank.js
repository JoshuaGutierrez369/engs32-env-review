const fs = require("fs");
const vm = require("vm");
const code = fs.readFileSync(require("path").join(__dirname, "../questions.js"), "utf8");
const sandbox = { window: {} };
vm.runInNewContext(code, sandbox);
fs.writeFileSync(
  require("path").join(__dirname, "bank.json"),
  JSON.stringify(sandbox.window.ENVS_QB, null, 0)
);
console.log(sandbox.window.ENVS_QB.length);
