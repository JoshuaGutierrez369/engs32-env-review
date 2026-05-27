const fs = require("fs");
const path = require("path");
const vm = require("vm");
const root = path.join(__dirname, "..");
const code = fs.readFileSync(path.join(root, "questions.js"), "utf8");
const sandbox = { window: {} };
vm.runInNewContext(code, sandbox);
const out = {
  version: "materials-2026-05-27-v9-lec51",
  questions: sandbox.window.ENVS_QB,
  essays: sandbox.window.ENVS_ESSAYS,
};
fs.writeFileSync(path.join(root, "bank.json"), JSON.stringify(out));
console.log("wrote bank.json", out.questions.length, "questions");
