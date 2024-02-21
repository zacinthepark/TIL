"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
var axios_1 = __importDefault(require("axios"));
axios_1.default
    .get("https://jsonplaceholder.typicode.com/users/1")
    .then(function (res) {
    console.log("WOO!!!");
    printUser(res.data);
})
    .catch(function (e) {
    console.log("ERROR!", e);
});
axios_1.default
    .get("https://jsonplaceholder.typicode.com/users")
    .then(function (res) {
    console.log("WOO!!!");
    res.data.forEach(printUser);
})
    .catch(function (e) {
    console.log("ERROR!", e);
});
function printUser(user) {
    console.log(user.name);
    console.log(user.email);
    console.log(user.phone);
}
